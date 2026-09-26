# 2. The GPU economy: from memory traffic to the demand for intelligence

Brad Gerstner and Sunny Madra connect two scales of argument: the engineering of inference and the possibility of a large increase in economically useful computation. Their concrete case is Groq's move from selling a distinctive chip architecture to offering inference through a cloud interface, followed by collaboration with NVIDIA. Their broader thesis is that cheaper computation and more capable agents can expand demand faster than efficiency improves.

The distinction between those scales matters. A measured hardware improvement does not establish a macroeconomic forecast. Rapid revenue growth does not prove that every capital commitment will be profitable. This chapter preserves the speakers' optimism, their technical mechanisms, and the audience's questions while deriving models that reveal what each claim would require.

Meridian, our invented documentation company, must now choose a serving system. Its customers care about an accurate finished document delivered on time. The platform team must translate that outcome into prompt processing, token generation, memory capacity, power, and cost. The same example will connect hardware choices to demand and margins.

## 2.1 Productivity, abundance, and the unit being produced [05:00](https://www.youtube.com/watch?v=BBl8bNJP6ds&t=300s)

### The economic ambition and its evidential limits

The opening introductions describe Gerstner's investing background, Madra's entrepreneurial path, and Gerstner's interest in broadening participation in economic ownership. His introductory slides link long-run technological progress to higher output and living standards. He argues that AI could accelerate this process and that users should learn to work effectively with the new tools.

GDP per person is a measure of average economic production, not a complete measure of well-being or its distribution. Health, leisure, environmental costs, inequality, and political freedom cannot be read directly from one GDP curve. Historical correlations between prosperity and social outcomes do not identify a single causal mechanism. The useful economic proposition is narrower: technologies that allow more valuable output from available resources can expand society's feasible opportunities.

Let $Y$ denote real output and $L$ labor hours over the same period. Average labor productivity is $Y/L$. It can rise because workers have better tools, more capital, improved skills, or better organization. A rise in output per hour does not say who receives the additional income or whether every affected worker benefits. This distinction anticipates the closing discussion of displacement and distribution.

If output per person grows at a constant annual rate $g>0$, its doubling time $T$ solves $(1+g)^T=2$, giving

$$
T=\frac{\ln 2}{\ln(1+g)}.
$$

At 2% growth, doubling takes about 35 years; at 4%, about 18. These are mathematical illustrations, not estimates of AI's effect. A temporary improvement in one sector's productivity is not equivalent to permanently doubling economy-wide growth. Adoption, complementary investment, resource constraints, and the size of the affected sector determine the aggregate consequence.

### Tokens are an engineering unit, not a conserved unit of value

The speakers describe tokens as the output of an intelligence factory. A **token** is a unit in a model's encoded sequence, often corresponding to a word fragment or other symbol. Token counts are useful for scheduling and billing, but their economic value varies with tokenizer, modality, task, model quality, and whether the output is accepted.

Meridian can produce a thousand fluent tokens that misstate a customer's requirements, or a hundred correct tokens that resolve the problem. The first consumes more computation while delivering less value. Thus a hardware comparison may legitimately measure tokens per second, but a business comparison must eventually measure cost per acceptable task under the required latency and reliability.

Define $C$ as total cost of a trial workload, $A$ as the number of accepted tasks, and $n$ as tasks attempted. When $A>0$, cost per accepted task is $C/A$. Acceptance rate is $A/n$. Reporting both prevents a service from appearing efficient merely by producing cheap failures. If acceptance depends on deadline, include that deadline in the criterion before benchmarking.

For example, system A spends ten dollars on one hundred attempts and delivers ninety acceptable results; system B spends eight and delivers sixty. Their costs per accepted task are about 0.111 and 0.133 dollars. B is cheaper per attempt but more expensive per success. If failed tasks also require human remediation, its disadvantage can be larger. This distinction will remain important when the lecture moves from token throughput to willingness to pay.

## 2.2 Groq's architecture and the cloud distribution decision [08:30](https://www.youtube.com/watch?v=BBl8bNJP6ds&t=510s)

Madra recounts Groq's origins around Jonathan Ross and describes a dataflow architecture paired with a compiler that schedules operations in advance. He argues that a developer-facing inference API made the hardware easier to adopt than asking customers to buy and integrate an unfamiliar system. The reported growth in developer usage is his operating account, not an independently audited comparison with NVIDIA's developer population.

### Deterministic execution is a scoped property

In the architectural discussion, **determinism** means that the compiled computation has a predictable execution schedule under specified conditions. It does not mean every internet request completes in identical time, that generated language is always identical, or that the service cannot fail. Network delays, queuing, model sampling, input lengths, and external tools remain separate sources of variability.

That distinction helps Meridian evaluate a latency claim. A device may provide predictable kernel execution while the end-to-end service waits behind other requests. Conversely, a service can provide a useful latency objective with hardware whose internal execution is not statically scheduled in the same way. Architectural properties must be connected to measured application behavior.

The API decision lowers an adoption barrier by hiding much of the device-specific integration. A customer can send a request to a familiar interface without first becoming an expert in the compiler or fabric. That shifts responsibilities to the provider: capacity acquisition, model compatibility, service operations, and reliability become part of the offering. A hardware business has become, in part, a service business.

This is not perfect fungibility. Even compatible APIs can differ in supported models, numerical precision, tokenization, rate limits, streaming behavior, context length, data terms, and failure modes. Meridian needs an acceptance test and a migration path. The interface reduces a class of switching costs; it does not erase all technical and commercial differences.

### Correct the token-computation shorthand

The lecture informally describes token computation as parameter count multiplied by squared context length. That is not a general complexity formula for cached autoregressive inference. The distinction between processing a prompt and producing the next token is essential.

For a simplified dense transformer, let $P$ be the number of participating model parameters, $L$ the number of layers, $n$ prompt tokens, and $d$ the attention representation width. Ignore architecture-specific constants, embedding costs, and mixture-of-experts sparsity. Processing the prompt involves parameterized projections and feed-forward operations of order $nP$, plus dense attention work of order $Ln^2d$. These are additive contributions, not generally their product.

During **prefill**, many prompt positions are processed together. During **decode**, a new token is generated after the preceding token, with cached keys and values from earlier positions. A rough next-token arithmetic model is order $P+Lnd$, because the new query attends to existing positions rather than recomputing every old token's representations. Without a cache, or with a different attention architecture, the calculation changes.

The **key-value cache** stores attention keys and values needed by subsequent tokens. If there are $h_{kv}$ key-value heads per layer, head width $d_h$, $n$ cached positions, and $b$ bytes per scalar, an idealized cache size for one sequence is

$$
M_{KV}=2Lnh_{kv}d_hb\quad\text{bytes}.
$$

The factor two accounts for keys and values. With 32 layers, eight key-value heads, width 128, 8,192 positions, and two-byte values, the cache occupies 1,073,741,824 bytes, or one GiB. Thirty-two such sequences need roughly 32 GiB before accounting for weights, activations, allocator overhead, and other state. A model can fit in memory while the desired serving batch does not.

The [PagedAttention paper](https://arxiv.org/abs/2309.06180) provides a specific research extension: managing dynamically growing key-value caches in blocks can reduce fragmentation and unnecessary duplication, enabling more efficient serving. Its reported gains belong to its evaluated workloads and baselines. The mechanism explains why software memory management can improve throughput without changing the chip's nominal arithmetic rate.

## 2.3 Prefill, decode, and complementary hardware [15:40](https://www.youtube.com/watch?v=BBl8bNJP6ds&t=940s)

Madra explains that inference can be decomposed into phases and, within decode, into functions with different arithmetic and memory demands. He contrasts GPU compute and external high-bandwidth memory with Groq's use of on-chip SRAM and argues that a combined system can outperform either treated as a universal solution. He describes an approach involving NVIDIA's interconnect ecosystem and a working cross-company prototype.

### Derive the bandwidth constraint

Let a kernel require $F$ floating-point operations and transfer $B$ bytes through the limiting memory interface. Let peak usable arithmetic capacity be $C$ operations per second and usable memory bandwidth $W$ bytes per second. Even under ideal overlap, execution time cannot be less than either resource requirement:

$$
t\geq\max\left(\frac{F}{C},\frac{B}{W}\right).
$$

Define arithmetic intensity $I=F/B$ in operations per byte. Dividing $F$ by the time bound gives the **roofline bound**

$$
\frac{F}{t}\leq\min(C,WI).
$$

The hinge is that data movement and arithmetic are separate constraints. Doubling arithmetic capacity does little for a workload whose data cannot arrive fast enough. The model is an upper bound; synchronization, communication, instruction overhead, and imperfect overlap can make actual performance lower. [NERSC's roofline documentation](https://docs.nersc.gov/tools/performance/roofline/) develops this measurement-based approach for identifying the limiting resource.

Suppose a hypothetical device offers 100 trillion operations per second and two trillion bytes per second of bandwidth. At intensity ten operations per byte, the bandwidth ceiling is twenty trillion operations per second. At intensity one hundred, the bandwidth ceiling is two hundred trillion and the arithmetic ceiling of one hundred becomes active. This explains why the same device can look underused on one workload and saturated on another.

Low-batch decode often has limited reuse of weights across simultaneous tokens, making memory traffic consequential. Larger batches can amortize weight movement but require more memory and may increase waiting time. Prefill often exposes larger matrix operations with more reuse. These are tendencies to profile, not universal laws that every prefill is compute-bound and every decode is bandwidth-bound.

### Disaggregation trades specialization against communication

**Disaggregation** assigns different phases or functions to distinct resources. It allows each resource pool to be sized and optimized for its workload, but introduces communication and coordination. For prefill/decode separation, the state needed by decode must be available at the destination. If the transfer is too slow or the pools are poorly balanced, the separation can worsen completion time.

The [DistServe study](https://arxiv.org/abs/2401.09670) explicitly separates prefill and decode while optimizing resource allocation under time-to-first-token and per-output-token constraints. This supports the lecture's mechanism: serving efficiency depends on satisfying latency objectives, not simply maximizing unconstrained token throughput. It does not independently verify the lecture's proposed hybrid system or its claimed multiplier.

The speakers report roughly 2.5 times more tokens for the same power footprint from combining complementary approaches. Treat that as their system claim. To evaluate it, Meridian would need the model, precision, sequence lengths, batch and arrival distribution, acceptance criteria, latency percentiles, power measurement boundary, and comparison baseline. “Same power” must specify whether it includes only chips or the whole facility.

### Amdahl's law disciplines component claims

Let fraction $f$ of the original serial runtime be accelerated by factor $s\geq1$, with the remainder unchanged and no new overhead. Normalizing original runtime to one gives new runtime $(1-f)+f/s$, so total speedup is

$$
S=\frac{1}{(1-f)+f/s}.
$$

If 60% of Meridian's processing time becomes four times faster, end-to-end speedup is $1/(0.4+0.6/4)\approx1.82$, not four. Adding transfer overhead equal to 0.1 of the original runtime reduces it to about 1.54. This calculation is intentionally simple; a queued service may respond nonlinearly when capacity changes. It nevertheless exposes why a fast kernel is insufficient evidence for an equally large application improvement.

The partnership story also needs precise transaction language. The introductions repeatedly describe NVIDIA as buying Groq. Groq's [24 December 2025 announcement](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale) describes a **non-exclusive inference-technology licensing agreement**, with personnel moving and Groq continuing independently. These notes use that primary description rather than converting the conversation's shorthand into a conventional whole-company acquisition claim.

## 2.4 Power, packaging, model growth, and the cost frontier [21:30](https://www.youtube.com/watch?v=BBl8bNJP6ds&t=1290s)

The discussion moves from architecture to supply-chain innovation, packaging, lithography, power, quantization, and larger models. Madra's point is that efficiency gains arrive from several interacting parts of the system while model complexity and demand also change. A quoted decline in “inference cost” needs a fixed comparison: the same workload and quality, or a clearly described quality adjustment.

### Translate power into a service constraint

Let $P_f$ be facility power available to the relevant serving system in watts and $\eta$ accepted tokens per joule under a specified workload. Since one watt is one joule per second, maximum accepted-token throughput under that simplified power boundary is

$$
q=P_f\eta\quad\text{tokens per second}.
$$

If a facility has one megawatt and efficiency is two accepted tokens per joule, the implied throughput is two million accepted tokens per second. Increasing efficiency by 2.5 times raises that bound to five million at unchanged power. But memory, networking, available chips, and service-level constraints can become tighter bottlenecks before the power bound is reached.

A power limit is distinct from energy cost. A site may be unable to draw more instantaneous power even when it could afford a higher electricity bill. Conversely, a site may have sufficient connection capacity but face unfavorable energy prices or unreliable delivery. The next lecture follows those distinctions into physical construction and financing.

### Quantization and larger systems change the feasible set

**Quantization** represents numerical quantities with fewer or differently encoded bits. It can reduce weight storage and data movement and sometimes improve arithmetic throughput. The economic benefit depends on supported kernels, conversion overhead, numerical behavior, and quality after quantization. Halving bytes per parameter does not automatically halve total service cost because not all memory or execution time scales with weight precision.

Larger packages and systems can place more silicon, memory, and interconnect capability into a coordinated unit. This can improve communication and usable capacity while increasing manufacturing, cooling, yield, and integration challenges. The lecture's references to wafer-scale designs, packaging, and circuit innovation belong to that system-level argument; they should not be reduced to a single transistor-shrink story.

The parameter-count forecasts in the conversation also require care. In a mixture-of-experts model, total stored parameters and parameters active for a particular token differ. Context, routing, memory access, and communication affect the result. Comparing models solely by total parameter count can therefore misstate both arithmetic cost and serving memory requirements.

For Meridian, the right procurement experiment fixes a task distribution and acceptance threshold, then measures delivered cost across candidates. It should include warm-up, realistic prompts, retries, and latency. If a new system supports a better model that changes acceptance, report both the fixed-quality comparison and the capability gain. Otherwise cost decline and product improvement are mixed into one ambiguous number.

### Supply scarcity can coexist with technical deflation

The speakers report rising prices for some older hardware while describing rapid improvements in inference efficiency. Those statements are not logically inconsistent. Engineering efficiency describes resources required per unit of a specified output. Market price depends on demand, supply, contracts, location, and timing. If demand grows faster than available capacity, the rental price of an older device can rise even while newer architectures improve the technological frontier.

The resale or rental value of old training hardware also depends on whether it can perform useful inference economically. Repurposing is possible, as Madra notes in the later Q&A, but not automatic: memory capacity, power efficiency, fabric, software support, and the available workload determine its usefulness. An asset's accounting life and its competitive economic life need not coincide.

## 2.5 Agents, elasticity, and willingness to pay [25:30](https://www.youtube.com/watch?v=BBl8bNJP6ds&t=1530s)

Gerstner argues that early products produced answers while later agents can complete valuable actions. Madra adds that the surrounding **harness**—the software that manages tools, state, retries, and continuation—can keep a model working across many steps. They describe coding tools, continuous assistants, and enterprise systems connected to communications and files. Reported spending anecdotes and revenue accelerations are evidence of their experience and thesis, not a representative sample or audited financial series.

### More output can consume more total resources after an efficiency gain

Let $p>0$ be price per comparable accepted task and $Q(p)$ the number demanded per period. Define local price elasticity of demand as

$$
\varepsilon=-\frac{d\ln Q}{d\ln p}.
$$

A convenient illustrative demand curve is $Q(p)=Ap^{-\varepsilon}$, with $A>0$ and constant $\varepsilon>0$. Expenditure is then $pQ(p)=Ap^{1-\varepsilon}$. When $\varepsilon>1$, lowering price increases expenditure because quantity rises more than proportionally. This is one possible rebound mechanism; it is not an empirical law that every AI market has elasticity above one.

If price halves and elasticity is 1.5, quantity multiplies by $2^{1.5}\approx2.83$ and expenditure by about 1.41. If resource use per task also halves, aggregate resource use still rises by about 1.41, under the assumption that the demand response is driven by the same price reduction. If elasticity is 0.5 instead, quantity rises only 1.41 times and aggregate resource use falls to about 0.707 of its prior level.

Real agents introduce another channel: the task itself changes. A one-turn answer may become a workflow with search, code execution, tests, corrections, and a final deliverable. Let $N$ be users, $a$ tasks per user, $k$ model calls per task, and $t$ tokens per call over a specified period. Total tokens are

$$
D=Nakt.
$$

This identity separates adoption, task frequency, workflow depth, and per-call size. If each factor doubles, total demand increases sixteenfold. It does not predict that they will double, and the factors need not be independent. Better tools can reduce $k$ through fewer retries even as users delegate more tasks.

### Value and cost must be measured at the same boundary

Suppose Meridian previously charged ten cents for a short suggestion costing two cents. It now completes a document for two dollars at a cost of fifty cents. Cost per job increased twenty-five times, yet contribution increased from eight cents to 1.50 dollars. The customer's willingness to pay can support greater computation when the outcome changes substantially.

That example does not establish that any particular agent is profitable. It requires the completed document to be accepted, errors and remediation to be counted, and customers actually to pay. The lecture's anecdotes about expensive continuous agents illustrate potential demand, but expensive use can reflect experimentation, subsidized budgets, or inefficient loops as well as productive work.

A model may also cross a capability threshold: a task previously requiring extensive human intervention becomes reliable enough to delegate. The economic response can then be discontinuous even if benchmark scores improve gradually. For Meridian, a modest reduction in serious errors might make an entire customer segment willing to adopt. Conversely, a small regression on a critical case can invalidate a large average improvement.

### Revenue acceleration does not remove financing arithmetic

The conversation contrasts large future compute commitments with much smaller then-current revenue and describes rising demand as a reason for greater confidence. The numerical revenue statements are sometimes phrased as annualized additions and sometimes as monthly figures. These notes do not silently reinterpret them into recognized monthly sales. Annualized run rate, annual revenue, booking commitments, and cash receipts must be separated.

A financing analysis needs the timing and enforceability of commitments, gross contribution, operating expense, working capital, available financing, and the ability to change the plan. Describing a commitment as a “call option” is economically justified only to the extent that its terms actually provide optionality. A contractual payment obligation cannot be wished into a free option because demand is uncertain.

Thus the speakers' evidence supports a testable thesis: improving capability can raise willingness to pay while systems engineering lowers cost at a fixed task. The conclusion that a particular multiyear expansion is adequately funded still requires a cash-flow model. Chapter 1's distinction between technological success and asset-level return remains intact.

## 2.6 Recursive improvement, employment, and distribution [35:00](https://www.youtube.com/watch?v=BBl8bNJP6ds&t=2100s)

The speakers anticipate continued hardware and model improvement and describe using AI in chip design. Gerstner recounts conversations with leading executives who believe very advanced capabilities are close or already present. Those are attributed judgments, not an operationally defined demonstration of AGI. A benchmark, a compelling demonstration, and a claim about broad autonomous competence answer different questions.

### Feedback is a mechanism, not an unlimited multiplier

AI-assisted design could improve the systems used to train and run future AI. That creates a feedback loop: better tools improve research or engineering, which improves tools. But the loop still includes experiments, fabrication, validation, human decisions, and physical supply. Faster software work does not make every stage instantaneous.

Let a development cycle take total time $T=T_s+T_p$, where $T_s$ is software or design time and $T_p$ is physical fabrication and validation time. If AI reduces $T_s$ by factor $s$, new time is $T_s/s+T_p$. With six months of design and eighteen months of fabrication and validation, a sixfold design acceleration changes the cycle from twenty-four to nineteen months. This is a time-domain application of the same bottleneck logic as Amdahl's law.

The model does not deny large improvements. It identifies where additional progress must occur to sustain them. Better simulation, reusable designs, or altered fabrication methods may change $T_p$, but those are further innovations with their own evidence. A claim of recursive acceleration should specify which stages improve and how the improved output is validated.

### Displacement and aggregate opportunity can coexist

In the career Q&A, Gerstner compares industrial displacement with the creation of new service occupations. He advises students to use tools effectively and emphasizes persuasion, relationships, team formation, and judgment. Madra adds the prospect of faster scientific discovery. The optimistic hypothesis is that cheaper access to useful expertise expands activity and creates new needs.

Historical adaptation does not guarantee a painless transition for particular people, locations, or generations. A worker's task can lose market value before a new opportunity becomes accessible. Retraining takes time, income support and mobility differ, and ownership affects who receives returns from automation. That is why Gerstner's discussion of broader economic participation is substantively connected to the technology argument rather than an unrelated political aside.

For a task-level model, let a job contain activities with time shares $w_i$, summing to one. If AI changes each activity's time by factor $r_i$ and the job's output and quality are held constant, total time changes by $\sum_i w_i r_i$. This does not predict employment: firms may expand output, redesign the job, change prices, or shift work toward activities that remain scarce. It does clarify why “the model can do this task” is not equivalent to “the entire occupation disappears.”

Meridian's users may spend less time formatting documents and more time checking substantive claims or consulting customers. Whether that is a productivity gain depends on outcomes and total effort, including correction. The practical career lesson is to learn both tool use and the domain standards needed to judge its output. Delegating work without the ability to detect consequential failure can create a new bottleneck in verification.

## 2.7 Edge devices, risk communication, and competition [45:00](https://www.youtube.com/watch?v=BBl8bNJP6ds&t=2700s)

The final questions address Apple's device strategy, cloud versus local computation, executive risk messaging, training hardware reused for inference, and NVIDIA's long-run margins. These questions qualify the growth thesis by asking where physical constraints, trust, and competition intervene.

### Privacy, latency, and energy create a placement problem

The speakers describe the appeal of local processing and the constraints of phone-scale compute and battery capacity. The anecdote about a small model rapidly exhausting a phone is not a standardized battery benchmark. A useful analysis instead begins with the workload, device, duty cycle, thermal limit, and measurement boundary.

Let battery energy be $E$ watt-hours and additional sustained inference power $P$ watts. Ignoring all other consumption and conversion losses, the maximum runtime attributable to that budget is $E/P$ hours. A fifteen-watt-hour battery supplying five watts supports three hours under this idealization; at fifteen watts, one hour. Real runtime is shorter when screen, radios, background tasks, and thermal behavior are included.

Cloud execution moves much computation off the device but adds network dependence, transport energy, latency, and data-governance considerations. Hybrid designs may process some data locally and send selected work remotely. Privacy is not determined solely by physical location: access controls, retention, encryption, model behavior, and application permissions also matter. Meridian should place computation according to its actual confidentiality and latency requirements, not an unconditional slogan about edge or cloud.

### Powerful capabilities require evidence-specific claims

The risk-messaging discussion includes reports of unreleased models finding software vulnerabilities and the speakers' support for controlled testing and coordinated remediation. We preserve that position without treating every reported result as independently replicated. The economic issue is dual use: the same capability can improve defense and lower the cost of harmful actions.

A useful evaluation specifies the capability demonstrated, the conditions, the failure modes, and the consequences of wider access. Optimism about beneficial applications and concern about misuse can both be rational. Claims that restrictions merely protect incumbents, or that every restriction is technically necessary, require evidence about the particular policy. The lecture itself raises both genuine risk and regulatory-capture concerns.

For Meridian, a concrete analogue is an agent allowed to inspect internal documents and send messages. A successful benchmark on writing quality does not establish that it should act without bounds across all customer systems. Permission design, auditability, evaluation, and recovery are part of the service's production cost. These are operational implications of the discussion, not a claim that the lecture supplied a complete security architecture.

### Competition can operate through quality or price

The final exchange asks whether NVIDIA can retain margins while alternatives improve. Gerstner's answer is that it must deliver something customers value more or compete on price. His valuation multiples, booked-sales figures, and future market-capitalization prediction remain source-era investor claims; they are not current investment advice or independently verified figures in this chapter.

A supplier can lose share while growing if the overall market expands sufficiently. If total market spending is $M$ and share is $s$, revenue is $sM$. A move from 80% of a 100-unit market to 60% of a 200-unit market raises revenue from eighty to 120 despite share loss. Profit still depends on price, cost, and expense. The arithmetic explains why successful custom accelerators and a growing incumbent are compatible outcomes.

The central procurement lesson is to compare complete systems under the same useful workload. Meridian's preferred supplier may change as models, demand, power prices, and software support change. A defensible choice records those conditions and the evidence that would reverse it.

### Executable checks of the engineering argument

These functions implement the roofline bound and serial speedup model already derived. The first returns operations per second; the second returns a dimensionless speedup. They assume positive capacities and nonnegative overhead, perform no hardware measurement, and reject invalid inputs. The final calculation checks the elasticity example.

```python
def roofline(compute, bandwidth, intensity):
    if min(compute, bandwidth, intensity) <= 0:
        raise ValueError("capacities and intensity must be positive")
    return min(compute, bandwidth * intensity)


def speedup(fraction, acceleration, overhead=0):
    if not 0 <= fraction <= 1 or acceleration < 1 or overhead < 0:
        raise ValueError("invalid runtime model")
    return 1 / (1 - fraction + fraction / acceleration + overhead)


assert roofline(100e12, 2e12, 10) == 20e12
assert abs(speedup(0.6, 4) - 1.818181818) < 1e-8
assert abs(speedup(0.6, 4, 0.1) - 1.538461538) < 1e-8
quantity_ratio = 0.5 ** -1.5
assert abs(0.5 * quantity_ratio - 2 ** 0.5) < 1e-12
```

## Exercises

1. **Derive a memory budget.** Use the chapter's cache formula for 40 layers, eight key-value heads, width 128, 16,384 positions, and two-byte values. Give bytes and GiB per sequence. How many such caches fit in 40 GiB reserved exclusively for caches?
2. **Find the bottleneck.** A device provides 120 trillion operations per second and three trillion bytes per second. Compute the roofline bound at intensities ten and sixty. What intensity marks the transition? Explain why measured performance can be lower.
3. **Test a hybrid claim.** A component occupying 70% of runtime becomes five times faster. Communication adds 8% of original runtime. Derive total speedup and compare it with the component multiplier. Identify one reason the serial model may fail for a production service.
4. **Distinguish rebound from capability change.** Price falls to one quarter with elasticity 0.75. Calculate quantity and expenditure ratios. Then explain why a new autonomous workflow cannot necessarily be analyzed using the old task's elasticity alone.
5. **Design a fair benchmark.** Two providers claim superior tokens per watt. Specify a matched experiment for Meridian and a counterexample in which the higher figure produces worse economics.
6. **Stress the growth thesis.** Construct a scenario where an incumbent loses share but grows revenue, and a different scenario where growing revenue coexists with falling operating profit. Explain which lecture claims these examples support and which they leave unresolved.

## Solutions and discussion

1. The size is $2(40)(16{,}384)(8)(128)(2)=2{,}684{,}354{,}560$ bytes, or 2.5 GiB. Forty GiB accommodates sixteen such caches under the idealized reservation. If allocator overhead, variable lengths, shared prefixes, quantized cache storage, or additional state are introduced, the answer changes. It is a capacity calculation, not a throughput prediction: fitting sixteen sequences does not establish a latency target.

2. At intensity ten, the bandwidth ceiling is thirty trillion operations per second; at sixty it is 180 trillion, so the arithmetic ceiling limits the result to 120 trillion. The transition is $I=C/W=40$ operations per byte. Synchronization, communication, instruction mix, and inefficient kernels can leave performance below either ideal ceiling. A roofline identifies a possible limiting resource rather than promising attainable peak performance.

3. New normalized runtime is $0.30+0.70/5+0.08=0.52$, giving speedup about 1.923. It is far below five because unchanged work and communication remain. In a production queue, changing service capacity can change waiting time nonlinearly; parallel overlap and changing batch size can also violate the serial decomposition. The appropriate follow-up is an end-to-end workload test.

4. Quantity multiplies by $0.25^{-0.75}=2\sqrt{2}\approx2.828$. Expenditure multiplies by $0.25(2.828)\approx0.707$. Aggregate expenditure falls in this fixed-task model. A new workflow may deliver a different outcome, involve more calls, and attract different users, shifting the demand curve itself. Applying the old elasticity without defining the new task would conflate a price response with product change.

5. Fix model or matched acceptance quality, prompt and output distributions, arrival pattern, deadlines, precision, cache conditions, and the power boundary. Measure accepted-task rate, completion-time percentiles, energy, total cost, and failures. A system generating many low-quality tokens efficiently can have worse cost per accepted document. A system with excellent steady-state throughput can also miss interactive deadlines because it relies on large batches.

6. An incumbent's 80% share of a 100-unit market yields eighty; 60% of a 200-unit market yields 120. For the second scenario, revenue rises from one hundred to 120 while gross contribution falls from forty to thirty and operating expense rises from thirty to thirty-five. Operating profit changes from ten to negative five. These examples support the logical compatibility of share loss with revenue growth and of growth with poor economics. They do not predict actual demand, margins, or valuation for any company.

## Primary-source references

- Brad Gerstner and Sunny Madra, [original GPU-economy conversation](https://www.youtube.com/watch?v=BBl8bNJP6ds), Spring 2026. Source of the architecture account, commercial thesis, forecasts, and Q&A.
- Groq, [non-exclusive inference-technology licensing announcement](https://groq.com/newsroom/groq-and-nvidia-enter-non-exclusive-inference-technology-licensing-agreement-to-accelerate-ai-inference-at-global-scale), 24 December 2025. Primary transaction description.
- NERSC, [Roofline Performance Model](https://docs.nersc.gov/tools/performance/roofline/). Primary technical documentation for arithmetic-intensity analysis.
- Kwon et al., [Efficient Memory Management for Large Language Model Serving with PagedAttention](https://arxiv.org/abs/2309.06180), SOSP 2023. Research on key-value cache allocation and serving throughput.
- Zhong et al., [DistServe](https://arxiv.org/abs/2401.09670), OSDI 2024. Research on separated prefill/decode serving under latency constraints.

**Coverage boundary.** The complete caption sequence informs the chapter, including the opening productivity and ownership framing, Groq's API strategy, hybrid architecture, supply-chain and power arguments, agents and revenue claims, recursive engineering, employment, edge devices, risk communication, hardware reuse, and final competition question. Biographical banter and poker jokes are condensed. Unseen slides and unreleased-model reports are not independently verified. The cached-inference formula and transaction description are corrected against technical reasoning and primary evidence. Meridian and all numerical models are teaching additions.
