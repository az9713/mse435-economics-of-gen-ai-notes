# 4. Enterprise AI: context, competition, and the redesign of work

Ali Ghodsi challenges the idea that another jump in model capability is the main missing ingredient in enterprise adoption. His claim is that organizations have not supplied the context or redesigned the processes that would let existing capabilities do useful work. He also rejects the inference that cheaper software creation makes software businesses disappear. Lower entry barriers and lower switching costs increase competitive pressure, but data, scale, trust, and organizational execution remain consequential.

This chapter treats those as distinct propositions. The first concerns a production bottleneck inside an organization; the second concerns how competition distributes value outside it. The strongest concrete source example joins them: Databricks reportedly improved connector delivery far more by changing requirements, testing, and team organization than by accelerating code writing alone.

Meridian, our invented documentation company, provides the recurring case. It wants to connect to a customer's systems, interpret current policy correctly, and deliver approved documents. A strong language model is necessary for some steps, but the entire workflow depends on access, meaning, authority, feedback, and coordination. The chapter's constructed examples make those dependencies explicit.

## 4.1 Capability without organizational context [00:09](https://www.youtube.com/watch?v=sRvrXL83N-c&t=9s)

Ghodsi begins by urging students not to make rushed career decisions from fear of missing an imminent technological transition. He then provocatively says that AGI is already present under the expectations he recalls from earlier AI research. His audience poll and conversations with former colleagues support an account of changing definitions, not a standardized empirical proof that every relevant capability has been achieved.

### Turn an undefined capability claim into a task claim

Terms such as AGI and superintelligence require operational definitions before they can decide an enterprise deployment. Comparing a model with a person's performance on selected intellectual tasks does not establish reliability on all tasks, long-horizon autonomy, or access to private information. Conversely, a failure on one awkward task does not establish that the model cannot be economically useful elsewhere.

For Meridian, the practical question is narrower: can this system produce a correct document from the permitted evidence, under the customer's current rules, before the deadline? That question has an input distribution, acceptance criteria, and measurable failure modes. It can be investigated without resolving a universal intelligence label.

Ghodsi contrasts strong general models with organizations that still operate through conventional human handoffs. He cites a widely discussed high failure rate for AI pilots but explicitly questions the precise percentage. We do not retain “95%” as a settled measurement. The argument is that adoption can underperform technical capability; identifying how often, in which population, and by what definition would require the underlying study and a careful denominator.

### Context is a structured set of dependencies

The lecture's memorable example is the experienced colleague whom everyone consults because essential organizational knowledge resides in that person's head. Some of this knowledge is factual: which system contains the authoritative record. Some is procedural: which approval is required. Some concerns exceptions, relationships, or recent changes that never became formal documentation.

Define a task instance by observable request $x$, relevant organizational state $z$, permitted action set $\mathcal A(z)$, and an outcome-loss function $L(a,x,z)$ for action $a$. A useful system needs enough information about $z$ to choose an action with acceptable loss, and it must remain within $\mathcal A(z)$. General knowledge about the world cannot supply facts that are absent from its inputs or inaccessible tools.

Imagine Meridian drafting a purchasing request. A general model knows how procurement usually works, but this customer requires three bids above a threshold, except for a named emergency procedure with a particular approver. The example is invented. A fluent document following generic policy can still be wrong because the task depends on current local rules. Better reasoning over missing premises cannot recover a unique correct answer when several policies are consistent with the observed request.

Formally, suppose the same observed $x$ is compatible with two states $z_1$ and $z_2$ that require different actions. Any deterministic decision using only $x$ must return the same action in both cases and therefore fail in at least one. The missing information is an identification problem, not necessarily a reasoning failure. The remedy may be retrieval, a tool query, clarification, or abstention.

### More context is not automatically better context

An organization can possess extensive documents without having a usable source of truth. Conflicting versions, missing ownership, stale permissions, and ambiguous terms can make more retrieved text less helpful. Meridian needs provenance, effective dates, access rules, and a way to resolve conflicts. The system must also distinguish instructions from quoted material and preserve the customer's authority over actions.

The [retrieval-augmented generation paper](https://arxiv.org/abs/2005.11401) supplies one technical mechanism for conditioning generation on retrieved information. It does not solve organizational governance by itself. Retrieval can provide a relevant passage while leaving unresolved whether the passage is current, applicable, authorized, or sufficient for the decision.

A falsifiable version of Ghodsi's thesis would hold the model fixed and improve context quality, then measure task outcomes. Another experiment would hold context fixed and change the model. Their effects may interact. The lecture emphasizes the first path, but it does not logically establish that model improvements never matter. A careful enterprise program measures both rather than turning a useful corrective into a universal slogan.

## 4.2 Cheaper software changes competition and switching [07:20](https://www.youtube.com/watch?v=sRvrXL83N-c&t=440s)

Asked whether software is dead, Ghodsi points out that model companies and chip-design companies also rely heavily on software. The literal claim is incoherent. His more precise argument is that software becomes easier to create and interfaces become easier to change, weakening some defenses while leaving others intact.

### Lower entry barriers benefit entrants and incumbents

An **entry barrier** is an obstacle that makes it difficult for a new supplier to compete effectively. Code-writing expense is one such obstacle for some products. Distribution, customer trust, access to data, regulatory requirements, support, and integration can remain substantial even when a prototype becomes cheap.

Meridian can use AI to build a new integration faster, but so can a larger competitor. The effect on relative advantage depends on what else each firm possesses. An incumbent may have established customer relationships and production data; an entrant may avoid legacy architecture and organizational constraints. Neither advantage guarantees the result.

Let total lifecycle cost of a software product be $C=C_b+C_i+C_v+C_o$, representing building, integration, validation, and operation. If AI reduces $C_b$ by fraction $a$ while other costs remain unchanged, total cost falls by fraction $aC_b/C$. If building is 20% of lifecycle cost and becomes 80% cheaper, total cost falls only 16%. This does not diminish the tool's benefit; it locates the remaining work.

The model also explains why Ghodsi declines the suggestion that every company should rebuild its own core software. A cheap local imitation may replace a user interface while leaving data migration, security, permissions, reliability, and ongoing maintenance unsolved. The build-versus-buy comparison must include the service obligation over time.

### Agent interfaces can remove one switching cost

A **switching cost** is a cost incurred by changing suppliers or systems. Ghodsi's phone and enterprise-interface examples focus on learning a different UI. If an agent mediates interactions, the human may no longer need to learn every application's interface, reducing that component.

Write total switching cost as $S=S_u+S_d+S_w+S_r$, where the terms denote interface learning, data migration, workflow integration, and risk or validation. These categories can overlap in practice, so the decomposition should be used consistently rather than double counted. Reducing $S_u$ to zero does not imply $S=0$.

Suppose Meridian's customer would save 4,000 dollars monthly by switching. Interface learning costs 5,000 once, data migration 12,000, integration 18,000, and validation 13,000. Total switching cost is 48,000, giving a simple twelve-month recovery time. Eliminating interface learning lowers it to 43,000 and recovery to 10.75 months. The change matters, but the service is not frictionlessly interchangeable.

If the expected remaining contract horizon is six months, neither version pays back under this simplified model. If migration also risks a costly outage, the expected benefit is lower. If the new service improves quality or enables new revenue, the benefit is higher. The arithmetic disciplines the claim that a conversational front end alone dissolves all enterprise lock-in.

### The remaining defenses need mechanisms

Ghodsi names scale, brand, trust, special data, and other capabilities as possible defenses, and recommends Hamilton Helmer's framework. The useful analytical habit is to identify why an advantage persists. Scale may spread fixed cost across more customers; exclusive lawful data access may improve a product; a history of reliable operation may reduce perceived purchasing risk.

For scale, let fixed annual cost be $F$ and variable cost per customer $c$. Average cost at $N$ customers is $F/N+c$. As $N$ grows, the fixed-cost component declines. That is an economy of scale under the model. It is not a guarantee of monopoly: congestion, support complexity, organizational cost, and differentiated needs may limit the advantage.

Data is similarly conditional. A large archive with no relevance, permissions, or reliable labels can be less valuable than a small, well-curated task dataset. A data advantage becomes defensible when it improves outcomes that customers value and is difficult for rivals to reproduce through legitimate alternatives. The next enterprise-knowledge lecture explores how that information enters training and feedback loops.

Ghodsi expects non-innovating incumbents to face pressure and argues that established firms can respond through better products, pricing, and cost structure. This is a contingent strategic judgment. The mechanism is more useful than a blanket prediction that either startups or incumbents must win.

## 4.3 The jagged frontier and the selection problem in support [13:35](https://www.youtube.com/watch?v=sRvrXL83N-c&t=815s)

The interviewer introduces the idea that model capability is uneven across tasks. Ghodsi's support example then gives a reason why an apparently familiar task category can be unusually difficult: Databricks customers often contact support only after technically sophisticated users have already tried to solve the problem.

### A category average can conceal a hard conditional distribution

Let $H$ denote a hard case and $E$ an easy case, and let $S$ denote escalation to support. Suppose 10% of all cases are hard, 80% of hard cases escalate, and 5% of easy cases escalate. Bayes' rule gives

$$
\Pr(H\mid S)=
\frac{\Pr(S\mid H)\Pr(H)}
{\Pr(S\mid H)\Pr(H)+\Pr(S\mid E)\Pr(E)}
=\frac{0.8(0.1)}{0.8(0.1)+0.05(0.9)}=0.64.
$$

Thus a population that is only 10% hard becomes 64% hard after selection into support. A benchmark drawn from ordinary questions can substantially overstate performance on the actual escalation queue. These probabilities are constructed to explain the mechanism; they are not measurements of Databricks support.

The speaker describes problems involving advanced data science and model performance, not merely password resets or routine product questions. Resolving them can require configuration history, logs, customer data constraints, and knowledge of interactions among systems. His report that generic support-automation vendors could not meet that need is an account of his company's experience, not a proof that support automation is ineffective everywhere.

### Assistance and replacement are different interventions

Brynjolfsson, Li, and Raymond's [Generative AI at Work](https://www.nber.org/papers/w31161) studies AI assistance for customer-support workers. The 2023 working-paper evidence reports about a 14% average increase in issues resolved per hour, with heterogeneous benefits. The intervention supports humans in a particular setting; it is not evidence that an autonomous system can replace every support function.

Dell'Acqua and colleagues' [jagged-frontier experiment](https://www.hbs.edu/ris/download.aspx?name=24-013.pdf) likewise shows that effects depend on whether tasks fall within the tested model's capabilities. Its relevance is the need for task-specific evaluation and attention to errors outside the frontier, not a universal productivity multiplier transferable to every organization.

For Meridian, an assistant that drafts a response for review and an agent that sends the response and changes records have different risk and cost profiles. The first may improve throughput even when autonomous acceptance is too low. Human review is not free, however. If checking a plausible but wrong answer takes longer than solving the problem, apparent drafting speed can be misleading.

Let unaided human time be $T_h$, assisted generation and interaction time $T_g$, review time $T_r$, and expected correction time $T_c$. Assistance saves time only if $T_g+T_r+T_c<T_h$, holding quality constant. At ten minutes unaided, one minute generation, two minutes review, and three minutes expected correction, the gain is four minutes. If correction rises to eight, the assisted process takes eleven minutes and loses time.

### Automation changes the remaining human workload

If AI resolves easy cases, the human queue can become harder even while total demand for human effort falls. Average handling time may rise because the mix changes, not because workers became less productive. A manager who evaluates the remaining team using the old average can misinterpret success as deterioration.

Suppose one thousand cases contain nine hundred easy cases requiring two minutes and one hundred hard cases requiring twenty. Total work is 3,800 minutes and average handling time 3.8 minutes. Automating eight hundred easy cases leaves one hundred easy and one hundred hard, totaling 2,200 minutes but averaging eleven minutes each. Human workload fell about 42%, while average time per remaining case nearly tripled.

The evaluation should therefore report case mix, total workload, quality, escalation, and resolution outcomes. It should also examine learning: removing all easy cases may change how novice staff acquire expertise. That is a possible organizational consequence to investigate, not an established result of the source anecdote.

## 4.4 Reorganizing the factory, then the software team [16:55](https://www.youtube.com/watch?v=sRvrXL83N-c&t=1015s)

Ghodsi invokes the delayed productivity effects of electrification and computing. His point is that replacing one tool while preserving the old organization can leave most of the potential unused. He then supplies the connector example that makes the analogy concrete.

### The historical analogy concerns complementary invention

Paul David's work on the dynamo and computer examines the importance of organizational and technical complements to new infrastructure. The [1989 working-paper precursor](https://ageconsearch.umn.edu/record/268373) supports the general analogy developed in his later 1990 essay. Electrification enabled different factory layouts and distributed drives; merely substituting an electric motor into an old arrangement did not exploit every opportunity.

The captions misname the economist associated with the famous computer-productivity observation; the standard attribution is Robert Solow. More importantly, the historical lag is not a universal clock predicting exactly how long AI adoption must take. Technologies, organizations, and measurement differ. The research connection explains why complementary change matters without prescribing a forty-year delay.

For Meridian, replacing a writer with a drafting tool while retaining every approval queue, duplicate entry, and handoff can yield only a modest improvement. Some constraints exist for good reasons; others are artifacts of slow earlier tools. Process redesign must distinguish them. Removing a necessary validation step to claim speed is not the same as making validation more effective.

### The nine-month connector story

Ghodsi reports that production-ready connectors took about nine months. A quick AI-assisted prototype suggested a dramatic improvement, but the team initially estimated only a reduction to seven and a half months because code writing was not the whole process. Production required requirements, testing against external systems, security, feedback, and dependable operation.

The later redesign reportedly delivered seven connectors in a quarter. The source identifies three concrete changes: collect an initial requirements set quickly and iterate; outsource difficult test-environment setup to specialists working in parallel; and organize people across connectors rather than assigning one isolated owner to each. The last change reduced dependence on a single person's availability, often called a bus-factor problem.

The reported delivery improvement is not a controlled experiment. Team size, scope, accumulated knowledge, and quality assurance must be comparable before assigning a precise causal multiplier. Still, the mechanism is much more informative than a generic claim of “AI productivity”: cheaper iteration made a different requirements strategy feasible, while parallelization and shared ownership removed other delays.

### Model the workflow as a dependency graph

Represent activities as nodes in a directed acyclic graph, with edges indicating prerequisites. Let $d_i$ be activity duration. Under unlimited resources and deterministic durations, project completion time is the length of the longest prerequisite path, the **critical path**. Resource conflicts and uncertain durations make actual scheduling more complex, but the graph reveals where local acceleration cannot change the finish date.

Suppose requirements take twelve weeks; code takes eight after requirements; test-environment preparation takes ten after requirements; and final validation takes four after both code and the environment are ready. Completion time is $12+\max(8,10)+4=26$ weeks. Halving coding time leaves it at twenty-six because environment setup remains the longer parallel branch.

If requirements become two weeks, environment preparation becomes three, and coding four, then completion becomes $2+\max(4,3)+4=10$ weeks. The large gain requires changing several constraints. This constructed graph differs from Databricks' exact internal process, which is not fully specified in the recording; it demonstrates the causal logic of the account.

### Faster iteration changes the value of early precision

When revisions are expensive, an organization may rationally invest heavily in requirements before implementation. When revisions become cheap, it can become better to build an early version, learn, and revise. This is not permission to ignore requirements that protect customers; it is a change in the economics of resolving uncertainty.

Let $C_d$ be the cost of delaying a decision for more information, $p$ the probability that an early decision needs revision, and $C_r$ the revision cost. In a very simple comparison, acting early has expected revision expense $pC_r$; waiting is attractive if the information's expected reduction in revision and other losses exceeds $C_d$. Lower $C_r$ can shift the balance toward earlier experimentation.

For Meridian, a reversible formatting choice may be cheap to revise, while an incorrect external disclosure may be irreversible. The workflow should therefore distinguish reversible drafts from consequential actions. Faster code generation can justify faster learning without justifying weaker controls on the latter.

## 4.5 Where value accrues when the bottleneck moves [24:45](https://www.youtube.com/watch?v=sRvrXL83N-c&t=1485s)

Asked where he would allocate capital across the AI stack, Ghodsi favors applications while repeatedly emphasizing that he is offering a technologist's view rather than investment advice. His historical example is his own work on efficient multicast: a difficult infrastructure problem became less commercially urgent as bandwidth costs fell and supply expanded.

### A technically hard problem can lose its economic scarcity

The multicast story is not a claim that multicast or networking research has no use. It is a retrospective account that the particular opportunity he pursued did not develop as expected. The lesson is that the value of solving a constraint depends on whether the constraint remains binding when the solution reaches customers.

Suppose Meridian can reduce a scarce input's consumption by 50%. If that input initially costs one hundred per task, the saving is fifty. If its price falls to two before the product ships, the same technical improvement saves only one. The engineering achievement is unchanged; the commercial value proposition is different.

This is why a founder should test both technical feasibility and the durability of the bottleneck. Alternatives can improve, customers can change workflows, or a complement can become abundant. A market forecast that assumes today's scarcity persists through development and adoption should state that assumption explicitly.

Ghodsi contrasts infrastructure preoccupations with later internet applications such as commerce, transportation, accommodation, and communication. He suggests healthcare and education as examples where valuable outcomes, substantial need, and task-specific data could support important applications. Those are hypotheses about opportunity, not evidence that a particular product is clinically effective, educationally effective, or commercially defensible.

### Willingness to pay is necessary but not sufficient

Customers may care deeply about an outcome while the supplier still struggles to earn revenue. The buyer, user, payer, and beneficiary can differ. Procurement, regulation, evidence requirements, distribution, and budget constraints shape actual transactions. A powerful need does not automatically translate into a frictionless market.

For an application, let customer benefit be $V$, price $P$, and full incremental delivery cost $C$. A transaction can create surplus when $V>C$, but a feasible price must satisfy $C<P<V$ if both sides require positive surplus before fixed costs. If the party experiencing $V$ cannot authorize payment, or if benefits are uncertain and difficult to verify, the transaction may not occur despite a favorable theoretical interval.

Meridian may save employees time while procurement evaluates only direct departmental spending. Demonstrating the gain in a measurable workflow can matter as much as generating a good document. The application must fit the institution that buys and uses it. That is another form of organizational context.

### Moving up the stack is a tendency, not a theorem

Ghodsi predicts value will move toward applications as lower layers commoditize. The opening lecture is more uncertain about timing and eventual structure. Keeping this disagreement visible is important: the course contains competing judgments, not one settled forecast repeated by different speakers.

An upstream supplier can remain valuable if its capability is hard to substitute, its scale lowers cost, or demand expands faster than competition erodes margins. An application can face strong competition if its differentiation is easy to copy. Technical position in a stack does not determine profit without considering market structure.

For Meridian, the actionable question is what durable customer problem it solves and what evidence makes its solution preferable. Owning a fashionable interface is weaker than reliably completing a difficult workflow with relevant data, permissions, and support. Yet even a strong product must continue adapting as its underlying models and competitors improve.

## 4.6 Open models, token factories, and a long time horizon [32:15](https://www.youtube.com/watch?v=sRvrXL83N-c&t=1935s)

The final discussion argues that improving open models can pressure proprietary-model pricing while leaving a substantial business in centralized serving. Ghodsi rejects the implication that access to model weights means every customer will operate a personal data center. He expects scale and operational efficiency to matter in what he calls token factories.

### Openness and operating cost are different questions

Access to model weights can make deployment, modification, and supplier substitution possible, subject to the license and other conditions. It does not remove the need for compute, software, evaluation, updates, and operations. “Free weights” is not equivalent to free service. Nor is every model with downloadable weights open source under a broader definition of the system and its freedoms.

The recording's comparisons between newly released models and earlier frontier systems are time-specific speaker judgments. These notes do not turn them into a current leaderboard. A relevant comparison for Meridian fixes its task distribution and acceptance criteria. An older general model may be sufficient, while a newer frontier model may remain preferable for a difficult class of requests.

Let managed service cost per year be $C_m=pQ$, with request price $p$ and annual volume $Q$. Let self-operated cost be $C_s=F+cQ$, where $F$ covers annualized setup, staffing, and fixed capacity, and $c$ variable cost per request. If $p>c$, self-operation becomes cheaper in this simplified model when

$$
Q>\frac{F}{p-c}.
$$

With fixed annual expense 180,000, managed price 0.02, and variable self-operated cost 0.008, the threshold is fifteen million requests. Quality, latency, utilization, failure, and staff opportunity cost must be comparable. If the self-operated service does not meet the customer's requirements, a favorable threshold is irrelevant.

Scale can therefore support large centralized providers even when the underlying model is widely available. At the same time, portability and alternative providers may constrain their prices. The eventual margin depends on competition, service differentiation, supply scarcity, and cost. The lecture's prediction of thin margins is a thesis to test, not a mathematical consequence of open weights.

### Product choice and career advice return to the same principle

In the rapid-fire questions, Ghodsi describes using coding tools and Databricks' own analytical product for quantitative business decisions. This distinguishes code generation from querying governed organizational data. Different tools solve different parts of the enterprise problem, and the useful interface depends on the decision.

His closing advice is to take a long view and look for important problems rather than chase whichever technical topic attracts the most attention. The retrospective examples of internet companies illustrate that applications can emerge years after enabling infrastructure. Exact founding-date shorthand is not needed for the argument: useful ideas and organizational execution can lag technical availability.

Meridian's research program should consequently measure a few durable outcomes: accepted documents, end-to-end completion time, customer retention, total human effort, and error consequences. Model choice and code-generation speed are inputs to those outcomes. Keeping that hierarchy explicit helps prevent an organization from optimizing a visible local metric while the actual service remains unchanged.

### Execute the selection and scheduling models

This code computes the hard-case share after escalation and the two-branch project duration already derived. Probabilities must lie in the unit interval; an impossible escalation event has no defined posterior. Durations are nonnegative weeks. The functions have no external effects and return a probability and a duration.

```python
def hard_share(prior, hard_escalation, easy_escalation):
    if not all(0 <= p <= 1 for p in
               (prior, hard_escalation, easy_escalation)):
        raise ValueError("invalid probability")
    hard = prior * hard_escalation
    total = hard + (1 - prior) * easy_escalation
    if total == 0:
        raise ValueError("conditioning event has zero probability")
    return hard / total


def delivery_weeks(requirements, coding, environment, validation):
    if min(requirements, coding, environment, validation) < 0:
        raise ValueError("durations must be nonnegative")
    return requirements + max(coding, environment) + validation


assert abs(hard_share(0.1, 0.8, 0.05) - 0.64) < 1e-12
assert delivery_weeks(12, 8, 10, 4) == 26
assert delivery_weeks(12, 4, 10, 4) == 26
assert delivery_weeks(2, 4, 3, 4) == 10
```

The executable boundary matters: returning a posterior when no case can escalate would hide an undefined conditional probability. Likewise, the schedule function is intentionally limited to the stated graph. It does not pretend to optimize staffing, estimate unknown durations, or reproduce Databricks' internal project plan.

## Exercises

1. **Prove a context limitation.** Construct two organizational policies consistent with the same user request but requiring different actions. Show why a deterministic system receiving only that request must fail in at least one state. Identify the smallest additional question or tool result that resolves the ambiguity.
2. **Calculate a switching decision.** A new service saves 3,000 monthly. Migration costs 15,000, workflow integration 12,000, validation 9,000, and UI learning 6,000. Compute recovery time before and after an agent removes UI learning. Include a 20% chance of a 15,000 transition loss and recompute the second result.
3. **Analyze support selection.** Hard cases are 20% of arrivals; 60% of hard and 10% of easy cases escalate. Find the hard fraction in support. Explain why measuring only the original population can mislead deployment.
4. **Redesign a critical path.** Requirements take eight weeks, parallel coding and environment setup take six and ten, and final validation takes three. Find delivery time. Compare eliminating coding entirely with reducing requirements to two and environment setup to four while coding remains six.
5. **Separate local and organizational productivity.** A task took twenty minutes unaided. AI generation takes two, review four, and correction takes fifteen minutes with probability 0.4. Find expected assisted time and saving. Propose an outcome measure that would detect a quality regression hidden by this average.
6. **Evaluate the application thesis.** Design a small experiment for Meridian that distinguishes missing context from insufficient model capability. Specify treatment conditions, held-out cases, measurements, and one result that would contradict a context-only explanation.

## Solutions and discussion

1. The request “approve this purchase” can refer to a policy allowing the requester to approve small purchases or one requiring a separate budget owner's approval. If the amount and role are absent, the same observed text can require different actions. A deterministic function of that text returns one action and cannot be correct under both incompatible requirements. Querying the applicable policy, purchase amount, and current authority can resolve the ambiguity. If the task permits asking rather than acting, clarification is itself a valid response rather than a failure.

2. Total initial cost is 42,000, giving fourteen months at 3,000 monthly savings. Removing UI learning leaves 36,000 and twelve months. Expected transition loss adds $0.2(15{,}000)=3{,}000$, producing 39,000 and thirteen months. This undiscounted calculation assumes the savings persist and that expected loss adequately represents the decision-maker's risk tolerance. A rare unacceptable loss may require a hard constraint instead.

3. The hard contribution to escalations is $0.2(0.6)=0.12$ and easy contribution is $0.8(0.1)=0.08$. The posterior is $0.12/0.20=60\%$. The support queue therefore has three times the original hard-case fraction. Evaluation should sample the actual deployment population and preserve relevant case categories, rather than applying an overall accuracy measured before selection.

4. Original duration is $8+\max(6,10)+3=21$ weeks. Eliminating coding still leaves twenty-one because environment setup controls the parallel branch. Reducing requirements and setup gives $2+\max(6,4)+3=11$ weeks. The example shows why local code speed can have zero effect on delivery while process changes matter greatly. Resource contention or dependencies between coding and setup would require a different graph.

5. Expected assisted time is $2+4+0.4(15)=12$ minutes, a saving of eight or 40%. Measure accepted task quality and consequential error rate on a held-out set, including delayed corrections and downstream effects. A lower average time can conceal a small number of severe errors or transferred work outside the measured team. The comparison needs a common outcome and full effort boundary.

6. Use a factorial comparison: current versus improved governed context, crossed with current versus stronger model, while holding tools, permissions, and evaluation cases fixed. Measure acceptance, serious errors, clarification frequency, total human effort, latency, and cost. Include cases requiring private current facts and cases with adequate context but difficult reasoning. If the stronger model substantially improves adequately contextualized cases while context improvements alone do not, that contradicts a context-only explanation. Improvements from both factors support a complementary account.

## Primary-source references

- Ali Ghodsi, [original enterprise-AI conversation](https://www.youtube.com/watch?v=sRvrXL83N-c), Spring 2026. Source of the context thesis, connector account, strategic judgments, and career advice.
- Lewis et al., [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401), 2020. Technical mechanism for conditioning generation on retrieved evidence.
- Paul A. David, [Computer and Dynamo: The Modern Productivity Paradox in a Not-Too Distant Mirror](https://ageconsearch.umn.edu/record/268373), 1989 working paper. Primary precursor to the historical argument discussed in the lecture.
- Brynjolfsson, Li, and Raymond, [Generative AI at Work](https://www.nber.org/papers/w31161), 2023 working paper. Evidence about human assistance in a specific support setting.
- Dell'Acqua et al., [Navigating the Jagged Technological Frontier](https://www.hbs.edu/ris/download.aspx?name=24-013.pdf), 2023. Experimental evidence on task-dependent effects of AI assistance.

**Coverage boundary.** The chapter includes the opening AGI and career framing, enterprise-context argument, software competition and switching costs, moats, difficult support cases, historical analogy, complete connector redesign, application-value thesis, multicast lesson, healthcare and education examples, open-model economics, product use, and closing long-term advice. Speaker forecasts remain judgments. The connector account is not treated as a controlled experiment; organizational policies and Meridian calculations are invented teaching examples. No unseen slide content is claimed as inspected.
