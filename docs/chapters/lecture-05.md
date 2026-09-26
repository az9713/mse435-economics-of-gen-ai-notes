# 5. Industrial compute: delivering capacity in time for useful work

Sachin Katti describes industrial compute as the problem of assembling an entire supply chain into usable capacity: chips, memory, networking, power, cooling, buildings, and operations. The key word is usable. A contract for future equipment is not a running service, and installed hardware is not necessarily performing at its intended rate. The lecture connects this physical problem to increasingly complex agents that alternate between model inference and ordinary computation.

Meridian's next decision is to expand its documentation agent. It could reserve a large distant cluster, use smaller nearby deployments, or combine resources specialized for different parts of the workflow. It needs enough capacity for customer work while maintaining room for evaluation and improvement. This invented case lets us develop the lecture's recurring decision: which resource, delivered when, improves the actual outcome?

## 5.1 Compute, revenue, and the distinction between capacity and demand [02:30](https://www.youtube.com/watch?v=4k53z3Ysjg0&t=150s)

The opening introduces Katti's background in networking, Intel, and OpenAI. He attributes renewed CPU relevance to agents and discusses manufacturing capacity as a strategic constraint. The interviewer then presents OpenAI's published comparison between compute growth and revenue growth. Katti describes revenue as following available, utilized capacity under the demand conditions his company has observed.

### Correlation becomes useful when its mechanism is specified

OpenAI's [January 2026 business statement](https://openai.com/index/a-business-that-scales-with-the-value-of-intelligence/) reports parallel growth in available compute and annualized revenue and describes research and product capacity as linked. This is primary evidence of management's account, not an independent causal estimate. Demand, pricing, capability, and capacity all changed during the period, so the chart alone cannot isolate the effect of adding a gigawatt.

Let $K$ be installed equivalent serving capacity in device-hours per period, $a\in[0,1]$ its operational availability, $u\in[0,1]$ productive utilization while available, and $q$ accepted tasks per productive device-hour under a fixed workload. Supply of accepted tasks is approximately $Kauq$. Let demand at price $p$ be $D(p)$ tasks per period. Delivered quantity is bounded by

$$
Q\leq\min\{Kauq,D(p)\},\qquad R=pQ.
$$

The capacity-revenue relationship is nearly proportional only while demand exceeds the usable supply and the other factors remain stable. Once demand is limiting, more capacity can lower utilization rather than increase revenue. If a stronger model changes both task value and resource requirements, $q$ and $p$ can move in opposite directions.

Suppose Meridian doubles capacity, but utilization falls from 80% to 60%, accepted throughput per device-hour rises 20%, and price per accepted task falls 30%, with availability unchanged. The revenue ratio under sufficient demand is

$$
\frac{R_2}{R_1}=2\left(\frac{0.6}{0.8}\right)(1.2)(0.7)=1.26.
$$

Revenue grows 26%, not 100%. The identity identifies what must be measured before extrapolating a capacity chart. It also shows how falling price can coexist with rising revenue if quantity grows sufficiently.

### Installed, contracted, and operational are different states

Katti describes the thirty-gigawatt figure in the conversation as an aspiration split between research and products. It should not be read as operational capacity at the time of the lecture. The same distinction applies to industry-wide plans, future purchases, and supplier announcements.

For Meridian, a capacity register should separate planned, contracted, under construction, installed, commissioned, and service-ready resources. A project can have completed the financial transaction while still waiting for power or cooling. A commissioned cluster can still require software work before it serves the intended model efficiently.

Even the unit “gigawatt of compute” needs a boundary. It is a power-related description, not a direct measure of completed tasks or floating-point operations. Device generations, cooling overhead, workload, precision, and utilization determine what it produces. The lecture's approximate GPU counts per gigawatt are context-specific conversions, not universal physical constants.

### Access limits are one manifestation of scarcity

Katti connects capacity to the ability to make a capable model broadly available and offer generous usage. His product-limit descriptions are source-era statements, not current entitlement documentation. The general mechanism is that a company unable to serve all demand may ration through price, queues, usage limits, restricted availability, or lower-cost routing.

Meridian faces the same tradeoff on a smaller scale. A low subscription price that attracts more work than its service can deliver may lead to long queues and dissatisfied customers. Capacity planning, pricing, and product promises must therefore be designed together. A technically excellent model that cannot be delivered within the promised service envelope does not complete the product.

## 5.2 Training increasingly contains inference [05:40](https://www.youtube.com/watch?v=4k53z3Ysjg0&t=340s)

The interview asks how compute divides between training and inference. Katti explains that post-training, reinforcement-learning rollouts, and synthetic-data generation can consume large amounts of inference. He expects inference to dominate more strongly, but emphasizes that inference does not mean only externally monetized product traffic.

### Separate computational operation from economic purpose

**Inference** evaluates a model with its current parameters. **Training** changes parameters using an optimization procedure. A research pipeline can alternate between generating outputs, scoring them, and updating parameters. The generation step is inference computationally while belonging to training economically.

For Meridian, define three compute accounts over one planning period: $C_P$ for parameter updates and other training operations, $C_R$ for research inference such as candidate generation and evaluation, and $C_U$ for user-serving inference. Total is

$$
C_{total}=C_P+C_R+C_U.
$$

The inference share is $(C_R+C_U)/C_{total}$, while the product-serving share is $C_U/C_{total}$. They are equal only if $C_R=0$. A rising inference share therefore does not imply that the same fraction of compute immediately earns customer revenue.

As a numerical example, consider twenty units of parameter-update compute, fifty of research inference, and thirty of user serving. Inference is 80% of the total, but direct product serving is 30%. The remaining work may create valuable future capability; its return is delayed and uncertain. The accounting needs to reflect that horizon rather than treating research tokens as failed monetization.

### Scaling laws have a domain of validity

The [Chinchilla study](https://arxiv.org/abs/2203.15556) investigates allocation between parameter count and training data under a pretraining-compute budget. Its relevant lesson is that scaling one input alone can be inefficient when another is underprovided. It does not supply a universal formula for all post-training, agent execution, or customer value.

The [DeepSeek-R1 paper](https://arxiv.org/abs/2501.12948) offers a separate primary example of reinforcement-learning-based reasoning development. It supports the existence of important training pipelines involving generated trajectories and rewards. It does not establish that arbitrary extra inference will reliably improve every task or that every reward measures the intended outcome.

Katti's statement that scaling extends across the model lifecycle should thus be understood as a research and planning perspective. Each stage needs its own empirical relationship among compute, data, objective, and resulting capability. Combining them into one undifferentiated “more compute gives more intelligence” curve would conceal important constraints.

### Three efficiency goals can conflict or reinforce one another

The source identifies three directions: make tokens cheaper, improve what a token accomplishes, and reduce tokens needed for a task through a better harness. Let $c_t$ be cost per generated token, $n_t$ expected tokens per attempt, and $s$ probability that an attempt yields an accepted result. Under independent repeated attempts with constant parameters and no additional costs, expected inference cost per success is

$$
C_{success}=\frac{c_tn_t}{s}.
$$

The factor $1/s$ is the expected number of geometric trials until success. It is inappropriate when failures are correlated or a task is fundamentally unsolvable by the system. Nevertheless, it shows why cheaper tokens, shorter trajectories, and higher acceptance all affect the same economic outcome.

Suppose a workflow spends 0.10 dollars per attempt and succeeds with probability 0.5. Expected cost is 0.20 per success under the model. A more capable version costs 0.15 per attempt but succeeds with probability 0.9, reducing expected cost to about 0.167. The apparently more expensive model can be economically better. If its latency is unacceptable, however, cost alone cannot choose it.

Meridian should keep quality, cost, and completion time separate until it states a decision rule. A hard deadline or error constraint cannot be traded away implicitly because a blended score looks better. The lecture's focus on making intelligence widely usable requires those outcomes to improve together or to be managed explicitly.

## 5.3 Orchestrating a supply chain and valuing time to compute [09:00](https://www.youtube.com/watch?v=4k53z3Ysjg0&t=540s)

Katti says much of the difficult work begins after contracts are signed. Equipment must arrive together, systems must function at scale, and power and cooling fluctuations must not prevent the hardware from delivering its intended performance. He also discusses grid effects, geographic concentration, generation options, and the societal implications of very large loads.

### The completion date follows the last necessary dependency

Let readiness times for buildings, power, cooling, chips, and networking be $T_b,T_p,T_c,T_g,T_n$. In a simplified parallel procurement model, with integration and commissioning time $T_i$, service readiness is

$$
T_{ready}=\max(T_b,T_p,T_c,T_g,T_n)+T_i.
$$

The maximum appears because all required components must be ready. If chips arrive in six months but power in eighteen, accelerating chips to four months does not advance readiness unless it changes another dependency. A cheap component with a long lead time can control the return on a much larger investment.

The model assumes parallel work and a single final integration stage. Real projects have dependencies within each category and may commission in phases. A more detailed schedule would represent those dependencies explicitly. The principle remains: optimizing the price or delivery of a nonbinding component may do little for time to useful capacity.

Suppose Meridian can obtain equivalent capacity from supplier A in six months or supplier B in twelve. B is three million dollars cheaper. If earlier access produces 0.8 million monthly incremental contribution for six months, the undiscounted timing benefit is 4.8 million. A can be economically preferable despite its higher purchase price. The comparison must include delivery risk, financing, contract terms, and whether the demand truly exists during those six months.

This explains the final Q&A's emphasis on time to compute rather than the largest announced total. Capacity that arrives after a critical research or product window can have lower value than less capacity available promptly. The optimal plan can change when timing uncertainty changes, even with identical long-run device prices.

### Synchronized workloads interact with the grid

The speaker describes large training jobs whose power demand changes in a coordinated way. He presents rapid changes in load as an engineering challenge for a grid not designed around such behavior. These are risk scenarios and design concerns, not evidence that a particular state actually experienced the hypothetical failure described.

Let load be $P(t)$ in MW. The ramp rate $dP/dt$ measures how quickly power demand changes, for example in MW per second. Two facilities can consume the same daily energy, $\int P(t)dt$, while imposing very different ramps. Energy accounting alone does not characterize the operational burden.

If a load rises by 100 MW for ten seconds while another resource cannot respond immediately, an idealized buffer must supply $100\times10=1{,}000$ MW-seconds, or about 0.278 MWh. It must also deliver 100 MW of power. A battery with enough energy but insufficient power rating cannot meet the requirement. Real buffer sizing includes efficiency, reserves, repeated events, state of charge, and control behavior.

The example links Chapter 3's energy/power distinction to dynamic operation. Large systems need coordinated design with the relevant grid and onsite equipment. Simply multiplying annual energy by an average price would miss the ramp problem and the cost of solving it.

### Diversifying brands does not necessarily diversify the bottleneck

Katti emphasizes concentrated manufacturing and memory supply and later points further upstream to lithography equipment. His view of foundry allocation is an industry interpretation: supporting multiple customers can encourage multiple accelerator designs, and large users may need to make several architectures productive.

If two chip brands depend on the same fabrication or packaging constraint, switching brands may not remove the shared supply risk. Conversely, different software stacks can make apparently diverse hardware difficult to substitute operationally. Meridian should trace the relevant dependency chain and test portability, not count vendors as if each were an independent supply source.

The lecture's broader ambition of one substantial compute resource per person is a scenario about possible scale, not a demand forecast. Translating such a scenario into power requires duty cycle, sharing, efficiency, and service requirements. A device's nameplate draw multiplied by population is an illustrative upper-level calculation, not a complete electricity forecast.

## 5.4 Agents make the compute graph heterogeneous [17:25](https://www.youtube.com/watch?v=4k53z3Ysjg0&t=1045s)

Katti distinguishes a chatbot response from an agent that tries actions, observes results, and revises its approach. A coding task may require reading files, generating code, running tests, examining failures, and trying again. Document work can require databases, search, spreadsheets, presentation software, and other tools. The model is one component of a larger computation.

### A workflow graph exposes different resource needs

Represent a finite execution trace as nodes $i$ with service time $t_i$, monetary cost $c_i$, and a required resource type. Edges specify prerequisite results. Some branches can run in parallel; others are sequential. The abstract agent may contain loops, but a completed finite trace can be unrolled into an acyclic dependency graph. This qualification matters because a general agent is not inherently a DAG merely because one execution can be represented that way.

Meridian's trace might retrieve a policy, query a customer record, draft a document, run deterministic format checks, request clarification, and revise. Retrieval may be storage- or network-sensitive; checks may use CPUs; drafting may use an accelerator; the human clarification can dominate elapsed time. Assigning every node to the fastest GPU would neither solve all constraints nor minimize cost.

For a fixed graph without resource contention, end-to-end latency is the longest path sum. Total direct resource cost is $\sum_i c_i$ across all executed nodes. The critical path and the cost sum are different aggregations. A parallel branch can add cost without lengthening completion, while a cheap sequential step can dominate delay.

Suppose two independent lookups take 0.2 and 0.5 seconds, followed by a 1.5-second draft and a 0.1-second check. Parallel lookup yields $\max(0.2,0.5)+1.5+0.1=2.1$ seconds. Sequential lookup yields 2.3. If the draft accelerates to 0.15 seconds, the parallel workflow becomes 0.75 seconds, and the longer lookup becomes much more visible.

### Hardware placement is a constrained optimization

Let $x_i$ select a resource type for node $i$. Resource choice changes service time $t_i(x_i)$ and cost $c_i(x_i)$. A simplified placement problem minimizes $\sum_i c_i(x_i)$ subject to a deadline on every source-to-output path, plus compatibility and capacity constraints. Moving a node can also add transfer time, so edge costs must be included where relevant.

This formulation explains the source's expectation of heterogeneous compute: a system optimized for very fast generation, large retained context, or general-purpose tool execution can be valuable for different nodes. It does not prove that every workload benefits from many architectures. Diversity increases integration, scheduling, and debugging complexity and can reduce pooling efficiency.

For Meridian, a sensible first step is to instrument the current workflow. Measure which nodes consume time, money, memory, and retries. Optimize the binding constraint before introducing a new resource type. An architecture selected from a generic benchmark can be wrong for the actual trace distribution.

### Human flow introduces a second queue

The lecture jokes that success would make the human the bottleneck because AI responses arrive quickly enough to sustain interaction. The more precise product goal is to preserve useful human flow. Interruptions, context switching, and repeated requests for decisions can impose cost even if the machine is fast.

If the agent asks for human input after every minor step, it can fragment attention. If it waits too long before asking about a consequential ambiguity, it can waste work or act incorrectly. The right interaction policy groups reversible work and asks at meaningful decision boundaries. That is a design implication of the source's flow objective, not a claim that low latency alone solves collaboration.

Meridian should measure total user effort and task completion, not only token speed. A fast stream of unusable drafts can be worse than a slightly slower coherent result. The economic objective remains accepted useful work within constraints.

## 5.5 Centralized scale, first-token latency, and the newly visible bottleneck [27:30](https://www.youtube.com/watch?v=4k53z3Ysjg0&t=1650s)

The interviewer asks whether an inference-heavy world requires small edge clusters. Katti argues that, under the workloads and costs he describes, construction scale and model-processing latency still favor large deployments. He expects the balance to evolve as models and systems change.

### Decompose latency before moving the server

For one model call, write time to first token as

$$
T_{first}=T_{network}+T_{queue}+T_{API}+T_{prefill}+T_{other}.
$$

Each term is elapsed time along the relevant critical path: network travel, waiting for service, API processing, model prompt processing, and remaining work. Some systems overlap stages, so a literal sum should be adjusted to the actual trace. The decomposition prevents attributing every delay to physical distance.

The recording cites a several-hundred-millisecond prompt-processing example and describes loading substantial context before generation. Those numbers are workload-specific, not universal model latency. Context caching, model architecture, batching, prompt length, hardware, and queue state change the result. Tokens are not directly interchangeable with bytes, and the caption's rough memory language should not become an exact storage calculation.

Suppose prefill takes 450 ms and other work 100 ms, including 60 ms of network time. Moving closer reduces network time to twenty, lowering total from 550 to 510 ms, about 7.3%. If a software improvement reduces prefill to fifty, the same forty-ms network saving reduces total from 150 to 110 ms, about 26.7%. The value of proximity changes as the dominant component changes.

This is the same moving-bottleneck principle seen in factories and enterprise processes. There is no permanent answer that the edge is always necessary or always irrelevant. The placement decision depends on the current workload, objective, and cost of operating distributed sites.

### Repeated overhead accumulates across an agent

An agent can make dozens of model and tool calls. Even modest per-call overhead matters when it lies on a long sequential chain. If $n$ calls each incur overhead $h$ seconds and useful processing time $s$ seconds, a serial simplified runtime is $n(h+s)$. Reducing $h$ can produce a meaningful gain without changing model inference.

OpenAI's [WebSocket engineering account](https://openai.com/index/speeding-up-agentic-workflows-with-websockets/) describes this exact class of problem: faster inference made repeated API processing and state reconstruction visible. The implementation used persistent connections and reuse of state to reduce redundant work. Its reported performance improvements apply to the measured deployments, not every agent or transport configuration.

For a constructed fifty-call trace, 100 ms overhead and 200 ms useful processing per call produce fifteen seconds total. Reducing overhead to twenty ms gives eleven seconds, a 26.7% reduction. If tool execution takes ten seconds per call instead, the same optimization has a much smaller proportional effect. Instrumentation tells us whether the change targets an important part of the actual path.

Persistent state also creates obligations: reconnect behavior, expiry, authorization, consistency, and recovery must be defined. A cache that makes a fast path quick but returns stale or cross-customer state can undermine the application. Performance and correctness need to be evaluated together.

### Scale economies are conditional on the service

The lecture argues that a large campus can spread labor mobilization and infrastructure costs over more capacity. That is a plausible project-level mechanism, not a universal claim that every large site is cheaper in every respect. Transmission, geography, redundancy, customer latency, and concentration risk can favor distribution.

Meridian's choice should therefore compare the full service cost at a common reliability and latency target. A central site with lower cost per device-hour can require expensive redundancy or suffer longer customer paths. A distributed design can provide proximity while losing utilization through small isolated pools. The optimal scale follows from those competing terms.

## 5.6 Memory architectures, co-design, and the pace of change [33:00](https://www.youtube.com/watch?v=4k53z3Ysjg0&t=1980s)

Asked what is misunderstood, Katti points to the relative simplicity of current accelerator memory systems compared with mature general-purpose memory hierarchies. He expects more sophisticated memory and software arrangements and describes using AI to help design subsequent hardware and low-level software. The motivation is that model changes occur much faster than traditional chip-development cycles.

### A memory hierarchy trades speed, capacity, and movement

A **memory hierarchy** places data across storage levels with different latency, bandwidth, capacity, and cost. A small fast level is useful when the right data can be reused there; a large slow level is useful for capacity but expensive to access repeatedly. The challenge is matching placement and movement to the workload.

For a simple two-level access model, let hit probability be $h$, fast access time $t_f$, and additional miss penalty $t_m$. Average access time is

$$
T_{access}=t_f+(1-h)t_m.
$$

If $t_f=10$ arbitrary time units and the extra miss penalty is ninety, a 90% hit rate gives nineteen; a 50% hit rate gives fifty-five. The fast memory's nominal speed alone does not determine performance. The access pattern and working-set size matter.

For models, weights, key-value caches, activations, and tool state have different reuse patterns. Chapter 2's [PagedAttention research](https://arxiv.org/abs/2309.06180) is one concrete example of software managing a dynamic memory object more efficiently. It does not solve every hierarchy problem, but it illustrates why memory organization can create useful capacity without simply adding arithmetic units.

Long context is especially relevant to Meridian because repeated work may use the same customer policies and document history. Retaining reusable state can save processing, but freshness and permissions constrain reuse. Data belonging to one customer cannot be made available to another merely because sharing improves cache efficiency.

### Co-design reduces mismatch but creates forecast risk

**Hardware–software co-design** chooses architectures and software together so that each exploits the other's strengths. The lecture imagines a tighter feedback loop in which model development helps specify the next system. This can reduce the mismatch between a device designed years earlier and the workload that eventually runs on it.

However, specialization commits resources to assumptions. If a chip optimizes a computation that later architectures reduce or replace, its advantage can shrink. A general-purpose design may sacrifice peak efficiency for flexibility. The correct tradeoff depends on development time, expected workload stability, reuse across tasks, and the cost of missing a new direction.

Let a specialized design save $s$ dollars per task on a compatible workload, require fixed development cost $F$, and serve expected compatible volume $Q$. Its simple net benefit is $sQ-F$. If only fraction $\theta$ of anticipated volume remains compatible after the design arrives, benefit is $s\theta Q-F$. The uncertainty in $\theta$ can dominate an impressive nominal saving.

For example, a ten-million development expense and one-cent saving require one billion compatible tasks. Forecasting two billion is sufficient only if at least half remain compatible under this model. The example ignores discounting and alternative uses of the team; adding them makes timing still more important. It explains why the source emphasizes shortening the time-compute cycle.

## 5.7 Durable opportunities and the final capacity questions [36:30](https://www.youtube.com/watch?v=4k53z3Ysjg0&t=2190s)

Katti expects some value to migrate toward platforms and applications, yet also sees durable opportunities in foundational infrastructure such as generation, transformers, batteries, cooling, materials, and manufacturing. Those views are compatible: multiple layers can create value, while the location of scarcity and profit changes over time.

### A thin interface is different from a completed outcome

The speaker is skeptical of a business that merely wraps a model without durable additional value. He also questions whether today's app boundaries will remain the dominant interface when users increasingly request outcomes. This is a strategic hypothesis about product organization, not a claim that all applications disappear or that model providers will necessarily own every workflow.

Meridian can test its own differentiation by asking what customers would still need if the underlying model became cheaper and more capable tomorrow. Governed integration, workflow-specific evaluation, dependable delivery, and domain relationships may remain useful. A cosmetic interface with no such contribution is more exposed to substitution.

The same test applies below the model. An infrastructure company can be valuable because it delivers a hard-to-replicate physical system on time, not merely because it resells an available component. Technical complexity becomes a commercial advantage only when it produces a result customers cannot obtain as effectively elsewhere.

### The Q&A separates short- and long-horizon improvements

The speaker expects near-term gains from harnesses and token efficiency, with memory architecture playing a larger role over longer periods. He qualifies this outlook by noting that a replacement for the transformer could change the compute-unit assumptions. That uncertainty should remain in any capacity plan.

On geographic project decisions, he emphasizes operational concentration and delivery time. The question mentions a specific UK project, but the answer supplies a general decision framework rather than a complete verified account of that project's status or reasons. These notes preserve what was actually explained and do not infer undisclosed contractual details.

On open-weight models, Katti acknowledges their role while defending continued investment at the frontier and the value of a temporary capability lead. This differs in emphasis from Ghodsi's expectation of strong commoditization pressure. Both can be true in parts of the market: a leading model may command value for difficult tasks while cheaper alternatives serve others. The empirical question is how large, durable, and monetizable each advantage is.

### A reproducible readiness and service model

The code below checks the capacity ratio and readiness logic. The first function returns relative revenue under sufficient demand and unchanged availability; the second returns a readiness time in the same units as its inputs. Neither forecasts demand or signs contracts. Invalid utilizations, rates, or times are rejected.

```python
def revenue_ratio(capacity_ratio, old_use, new_use, speed_ratio,
                  price_ratio):
    if not 0 < old_use <= 1 or not 0 <= new_use <= 1:
        raise ValueError("invalid utilization")
    if min(capacity_ratio, speed_ratio, price_ratio) < 0:
        raise ValueError("ratios must be nonnegative")
    return capacity_ratio * new_use / old_use * speed_ratio * price_ratio


def ready_time(component_times, commissioning):
    if not component_times or min(component_times) < 0 or commissioning < 0:
        raise ValueError("invalid readiness schedule")
    return max(component_times) + commissioning


assert abs(revenue_ratio(2, 0.8, 0.6, 1.2, 0.7) - 1.26) < 1e-12
assert ready_time([6, 18, 12, 9, 10], 2) == 20
assert ready_time([4, 18, 12, 9, 10], 2) == 20
```

The important planning artifact is not the largest number in a procurement spreadsheet. It is a traceable relationship from customer outcomes through workflow requirements to resources, readiness dates, and uncertainty. That relationship gives Meridian a basis for revising its plan when the bottleneck changes.

## Exercises

1. **Audit a capacity forecast.** Capacity grows 50%, availability falls from 98% to 95%, utilization rises from 60% to 75%, throughput per productive hour is unchanged, and price falls 20%. Derive the revenue ratio under sufficient demand. Explain what changes if demand is capped below the new supply.
2. **Classify compute.** A lab uses twenty units for parameter updates, forty for research rollouts, ten for research evaluation, and thirty for customer serving. Calculate inference share and direct serving share. State why a revenue-per-inference-unit metric could be misleading.
3. **Price delivery time.** A resource available four months earlier costs two million more. Expected incremental monthly contribution is 0.7 million, but early delivery succeeds with probability 0.6 and otherwise arrives at the later date. Compare the expected timing benefit with the premium under this simplified model.
4. **Locate the latency bottleneck.** A serial agent makes forty calls, each with 0.08 seconds API overhead, 0.12 inference, and 0.30 tool execution. Compare halving inference with reducing API overhead to 0.02. Then identify the largest remaining component.
5. **Design a buffer.** A load needs 150 MW of extra power for twenty seconds. Find ideal energy in MWh and explain why energy capacity alone is insufficient to specify a buffer. Include repeated-event and efficiency considerations.
6. **Test a heterogeneous deployment.** Propose an experiment deciding whether Meridian should move prefill, decode, and tool execution to separate resource pools. Specify compatibility, performance, cost, and failure measurements and a result that would favor keeping the simpler system.

## Solutions and discussion

1. The ratio is $1.5(0.95/0.98)(0.75/0.60)(0.8)\approx1.4541$, or about 45.4% growth. The calculation assumes all effective supply can be sold at the new price and quality remains comparable. If demand is capped, replace capacity-derived quantity with the smaller demand level before calculating revenue. Unused capacity then lowers realized utilization, so the assumed 75% may not be achievable.

2. Research rollouts and evaluation are inference if they evaluate fixed parameters during those steps. Inference is $(40+10+30)/100=80\%$; direct customer serving is 30%. Research inference may create future capability rather than immediate revenue. Dividing current revenue by all inference can obscure that distinction, while excluding research entirely from long-run profitability would omit a real cost.

3. Successful early delivery yields $4(0.7)=2.8$ million of extra contribution. Expected benefit is $0.6(2.8)=1.68$ million, below the two-million premium by 0.32 million. The late resource is preferable under these assumptions. A complete decision would consider discounting, contractual remedies, the distribution of demand, strategic deadlines, and whether failure of early delivery creates additional losses.

4. Baseline is $40(0.08+0.12+0.30)=20$ seconds. Halving inference gives $40(0.08+0.06+0.30)=17.6$. Reducing API overhead to 0.02 gives $40(0.02+0.12+0.30)=17.6$ as well. Both save 2.4 seconds because each removes 0.06 per call. Tool execution remains the largest component. Parallelization or caching might alter the graph, but cannot be assumed without checking dependencies and correctness.

5. Energy is $150(20)/3600\approx0.8333$ MWh, while the required power is 150 MW. A one-MWh battery unable to deliver that power is insufficient. Conversion losses require more stored energy, reserves restrict usable state of charge, and repeated events require enough recharge capacity and thermal capability. A real design also needs control response and coordination with the surrounding system.

6. Replay representative workloads with matched models or matched acceptance quality, sequence lengths, arrival bursts, and deadlines. Measure transfer volume, queueing, first-token time, output-token timing, completed-task latency, cost, and failures during resource loss or reconnect. Verify that state and permissions remain correct across pools. If communication, fragmentation, or operational complexity erases the gain under realistic load, retain the simpler deployment. A single favorable isolated kernel benchmark is insufficient evidence for separation.

## Primary-source references

- Sachin Katti, [original industrial-compute conversation](https://www.youtube.com/watch?v=4k53z3Ysjg0), Spring 2026. Source of capacity strategy, agent-workload analysis, supply-chain concerns, and Q&A.
- OpenAI, [A business that scales with the value of intelligence](https://openai.com/index/a-business-that-scales-with-the-value-of-intelligence/), January 2026. Primary management account of compute and business growth.
- Hoffmann et al., [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556), 2022. Pretraining resource-allocation research.
- DeepSeek-AI, [DeepSeek-R1](https://arxiv.org/abs/2501.12948), 2025. Primary example of reinforcement-learning-based reasoning development.
- OpenAI, [Speeding up agentic workflows with WebSockets in the Responses API](https://openai.com/index/speeding-up-agentic-workflows-with-websockets/), April 2026. Engineering account of reducing repeated API overhead.
- Kwon et al., [PagedAttention](https://arxiv.org/abs/2309.06180), 2023. Research example of memory-management improvements in model serving.

**Coverage boundary.** The chapter follows the complete caption discussion: Intel and CPUs, compute/revenue correlation, research versus product inference, supply-chain execution, grid implications, access limits, agent graphs, hardware diversity, foundry dependencies, scale versus edge latency, API redesign, memory and co-design, value capture, foundational infrastructure, wrappers, manufacturing concentration, time-to-compute, and open-weight models. Product limits, capacity targets, prices, and market forecasts remain source-era claims. Meridian's models and calculations are independent extensions; slides and private project details are not inferred.
