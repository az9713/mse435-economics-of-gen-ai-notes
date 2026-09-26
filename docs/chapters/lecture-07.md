# 7. Coding agents: from generated software to dependable services

Guillermo Rauch argues that making software easier to create expands the need for infrastructure that can deploy, run, and maintain it. His account of Vercel begins with developer experience and open-source tools, then moves to long-running agents, gateways, sandboxes, customized interfaces, and automated operations. The most important distinction is between a pile of generated code and a useful service that another person can actually use.

Meridian, our invented documentation company, wants to let customers create a tailored review portal with a coding agent. The portal must connect to authoritative records, run document-processing jobs, survive interruptions, and expose results through a usable interface. Its generated source code is only one artifact in that process. We will follow this service through creation, deployment, operation, and change.

## 7.1 Developer experience expands the population of creators [00:10](https://www.youtube.com/watch?v=HA7lZd7zk3M&t=10s)

Rauch's biography supplies the motivation for accessible tools: learning to code in Argentina, using available documentation, and building within an open-source ecosystem. His business account begins with frustration at how difficult it was to deploy a modern website even for an experienced engineer. The opportunity was to let people who could build a compelling front end obtain dependable infrastructure without becoming experts in every underlying layer.

### Deployment closes a learning loop

Writing code, running it locally, deploying it, and delivering value are different stages. A local program may depend on undeclared files, credentials, services, or environment assumptions. A deployed application must expose a stable interface, manage state, and operate under real users and failures. User feedback then reveals requirements that a source repository alone cannot test.

For Meridian, the first generated portal may look persuasive while failing to enforce access restrictions or handle an interrupted document upload. A real trial must observe the complete user path. The relevant unit of output is an accepted task in the deployed service, not lines of code or the number of files generated.

Define lifecycle cost as $C=C_{create}+C_{verify}+C_{deploy}+C_{operate}+C_{change}$ over a specified horizon. These terms cover creation, verification, deployment, operation, and later changes. They are a decomposition for analysis; in practice, responsibilities and accounting categories overlap and must be assigned consistently.

Suppose a small service originally costs 6,000 to create, 2,000 to verify, 600 to deploy, 3,000 to operate, and 1,000 to change during its first year: 12,600 total. AI reduces creation to 1,000 and deployment to 200, while verification rises to 2,500, operation falls to 2,000, and change to 500. Total becomes 6,200, a reduction of about 50.8%. Creation fell much more sharply, but the lifecycle saving is the economically relevant figure.

### More creators can mean more demand for infrastructure

Rauch reports rapid growth in deployments associated with stronger coding agents and describes the expansion from trained developers to a broader population of software creators. Those platform observations remain attributed; they do not establish a universal number of new developers or a measured global productivity effect.

Let $N$ be creators, $a$ projects per creator per period, and $r$ infrastructure consumption per project. Total resource demand is $D=Nar$. If creation becomes cheaper, both $N$ and $a$ may rise, while better efficiency lowers $r$. The total direction depends on their product. A tenfold expansion in projects with a fivefold decline in resource use per project doubles demand.

This is the software-creation counterpart of the rebound mechanism in Chapter 2. It does not imply every generated project remains active or valuable. Some are experiments, demonstrations, or abandoned drafts. Providers need to distinguish deployment counts from sustained usage, revenue, and customer outcomes.

### Measure productivity in the population actually served

The source's account of rapid creation should be read alongside empirical variation. METR's [early-2025 randomized study](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf) found that experienced open-source developers working on familiar mature repositories took about 19% longer with the tested AI tools. That is a specific population, task set, and tool period; it does not establish that all coding assistance slows everyone.

METR's [February 2026 update](https://metr.org/blog/2026-02-24-uplift-update/) discusses selection difficulties in measuring newer tools and explains why its newer observations do not support a clean general estimate. The research lesson is to distinguish prototype creation, mature-code maintenance, novice enablement, and expert work. Meridian should measure its own accepted changes and total effort rather than infer productivity from enthusiasm or benchmark scores alone.

## 7.2 Pages become long-running, stateful workflows [08:20](https://www.youtube.com/watch?v=HA7lZd7zk3M&t=500s)

Rauch contrasts the web's short request-response pattern with agents that may work for seconds, minutes, hours, or longer. He identifies three infrastructure roles: infrastructure used by coding agents, infrastructure that hosts agents, and infrastructure operated by agents. These roles overlap but impose different requirements.

### An agent needs a state model

For Meridian, let workflow state at step $t$ be $s_t$, action $a_t$, and observed result $o_{t+1}$. A transition rule updates state through $s_{t+1}=F(s_t,a_t,o_{t+1})$. State includes the task goal, completed steps, references to artifacts, relevant context, and the status of pending operations. The model's conversational text may be part of that state, but it is not necessarily a sufficient operational record.

A document job might move through received, validated, extracted, drafted, reviewed, and delivered states. If a process restarts after drafting, the service should know whether the draft exists and whether delivery already occurred. Otherwise it may lose progress, duplicate work, or repeat an external action.

**Durable execution** preserves enough state to resume a workflow across process failures or long waits. The [Vercel Workflow repository](https://github.com/vercel/workflow) provides a primary implementation reference for this programming model. Durability does not make each external action automatically safe to repeat; the action's semantics still matter.

### Long sequences amplify small failure probabilities

If a workflow requires $n$ independent stages, each succeeding with probability $p$, success probability is $p^n$. At $p=0.99$ and $n=20$, the result is about 81.79%. At $p=0.995$ and fifty stages, it is about 77.83%. High component reliability can still yield disappointing end-to-end completion.

The independence assumption is often optimistic or simply wrong. A common credential failure can break many stages together. Conversely, recovery mechanisms can allow a failed stage to be retried without restarting everything. The equation is a starting point for identifying why stage-level scores are insufficient.

If each transient attempt fails independently with probability $q$ and at most $k$ attempts are allowed, eventual stage failure is $q^k$. But repeated retries do not fix a persistent permission error, a malformed request, or an impossible task. A retry policy should distinguish transient conditions from errors requiring a changed plan or human input.

### Waiting is a state, not necessarily active compute

A workflow can wait for a customer approval without occupying a continuously running expensive model or worker. Separating durable waiting from active execution can improve economics. It also supports resumption when the user's decision arrives later or through another interface.

Let active computation cost $c_a$ per second and waiting-resource cost $c_w$ per second. For active time $T_a$ and waiting time $T_w$, cost is $c_aT_a+c_wT_w$. If a naive design uses the active resource throughout, cost becomes $c_a(T_a+T_w)$. The difference is $(c_a-c_w)T_w$, which can be large when human response time dominates.

Meridian should therefore record the pending decision and release unnecessary resources while waiting. The system still needs expiry rules, cancellation, authorization, and handling of stale decisions. Long-lived workflows change the service contract: a browser tab closing should not silently destroy a paid task, and a late approval should not execute an obsolete action.

Rauch also expects rich human-facing experiences to remain important. Agents do not eliminate the need to understand results. A well-designed portal can expose status, evidence, uncertainty, and controls in ways that a raw stream of tokens cannot. The interface is part of dependable operation, not merely decoration added after the agent finishes.

## 7.3 Gateways, sandboxes, and the agent's computer [14:00](https://www.youtube.com/watch?v=HA7lZd7zk3M&t=840s)

The lecture explains why reusable building blocks matter to coding agents, then discusses Vercel's support agent, model gateway, sandbox infrastructure, and the analogy with earlier cloud primitives. Rauch reports that the support agent handles a large share of inquiries and expands access to support. That percentage describes his platform's account and task mix, not a transferable guarantee for every support organization.

### A gateway coordinates access to models

A **gateway** sits between an application and one or more model providers, offering a common place for routing, credentials, observation, and failure handling. The [Vercel AI Gateway documentation](https://vercel.com/docs/ai-gateway) is primary evidence of this product category and its supported functions. The analogy to a content-delivery network is helpful for mediation and delivery, but generated model responses are not always interchangeable cacheable objects.

Meridian might route simple classification to a small model and difficult synthesis to a larger one. If the small model costs $c_s$ per request and fraction $r$ of requests then require a larger model costing $c_l$, expected sequential cost is $c_s+rc_l$. At 0.002, 0.15, and 0.020 respectively, expected cost is 0.005 dollars. This is cheaper than always using the larger model only if quality, latency, and downstream effects remain acceptable.

Routing needs a decision signal. A low confidence score is useful only if it predicts relevant failures. A confident wrong answer can bypass escalation. Evaluation must therefore examine the conditional error distribution among the cases left on the cheap path, not merely average model accuracy.

Let an extra routing error occur with probability $e$ and impose expected loss $L$. A simplified economic comparison adds $eL$ per request to routing cost. Saving 0.015 in inference is unattractive if $e=0.01$ and $L=10$, producing 0.10 in expected error loss. If the error violates a hard contractual constraint, expected-value pricing is insufficient regardless of the amount.

### Semantic similarity is not enough for safe reuse

An exact cache returns a prior result for the same defined input and relevant state. A semantic cache may reuse a result for a similar input. Similar wording can conceal different customers, permissions, policy versions, dates, or desired actions. Meridian must include those distinctions in any reuse rule.

Suppose two users ask “show the latest contract.” Their words are identical but their authorized records differ. Caching solely by text could return the wrong customer's document. Likewise, a policy answer cached before a rule change may be stale even for the same user. The safe cache key follows the task's dependency boundary, not just its surface language.

Rauch's “thanks” example illustrates that not every interaction needs the most expensive model. It should not be interpreted as a measured GPU count for a particular courtesy response. The economic principle is task-sensitive allocation; the implementation needs evidence that a cheaper path preserves the intended behavior.

### A sandbox permits action within an explicit boundary

A **sandbox** is an isolated execution environment with defined access and resource limits. Giving an agent a computer lets it inspect files, execute code, and test outputs, expanding what it can do beyond generating text. The [Vercel Sandbox documentation](https://vercel.com/docs/sandbox) describes an implementation of isolated execution for this class of workload.

Isolation does not automatically prevent every harmful action. If a sandbox receives credentials with broad access or unrestricted network permissions, the agent can still affect reachable systems. The boundary must specify which files, secrets, network destinations, and operations are available. Untrusted documents can also contain instructions that should not acquire authority merely because the agent reads them.

For Meridian, a document-processing sandbox should receive only the relevant inputs and the narrow capabilities needed for the task. Producing a draft and sending it externally are different permissions. This is a concrete operational consequence of the lecture's discussion of agent security, not an invitation to burden every harmless computation with unnecessary approval steps.

## 7.4 Operating the cloud and preserving the system of record [21:00](https://www.youtube.com/watch?v=HA7lZd7zk3M&t=1260s)

Rauch describes a future in which agents monitor, optimize, and repair infrastructure, reducing the burden of on-call operations. He then gives customer examples and discusses customized software replacing or augmenting standardized SaaS interfaces. The Salesforce example includes a crucial qualification: Vercel retained underlying Salesforce workflows and databases while generating a tailored presentation layer.

His Meta example concerns engineers using generated internal tools and deployment infrastructure to move faster; he also attributes part of Meta.AI's delivery speed to that infrastructure. His Notion example concerns adding agent capabilities, including a hypothetical class-transcription agent. These are customer accounts from Vercel's founder, not independent measurements of the counterfactual delivery time. They illustrate two routes to demand: enabling a new AI product and helping an established software product add agent behavior.

### An operational agent needs a feedback loop with limits

Monitoring observes a system; diagnosis proposes a cause; remediation changes it; verification checks whether the change helped. Combining these steps creates a feedback controller, but its observations may be incomplete and its actions can affect the system being measured.

Let service state be $x_t$, an operational action $u_t$, and measurement $y_t$. An abstract system evolves as $x_{t+1}=f(x_t,u_t,w_t)$ and measurement is $y_t=g(x_t)+v_t$, where $w_t$ and $v_t$ represent disturbances and measurement error. A controller chooses $u_t$ from available observations. This formalism emphasizes partial information: a plausible diagnosis is not the same as knowledge of the true state.

For Meridian, an agent noticing high latency might add workers. If the actual bottleneck is a rate-limited downstream API, more workers could increase retries and cost without improving throughput. A useful remediation policy tests a causal hypothesis, changes a bounded part of the system, and measures the result against a baseline.

The lecture's vision of self-operating infrastructure is therefore an ambition, not a claim that all operations are solved. Rauch explicitly acknowledges remaining human monitoring and difficult engineering. Reversible changes can be automated more broadly than actions with irreversible external consequences; the deployment policy should reflect that difference.

### The authoritative record survives a replaceable interface

A **system of record** is the authoritative source for a defined class of business data. A **presentation layer** exposes that data and actions through an interface. Replacing the latter can improve user experience while preserving the former's integrity, access control, and workflows.

Meridian might generate a customer-specific portal over an existing contract database. The portal can rearrange views and automate routine preparation, while the database remains authoritative for contract versions and approvals. This can create substantial value without rebuilding every underlying function.

Rauch's parking-lot software anecdote illustrates a different case: a narrow application may be simple enough to replace more completely. The correct scope depends on the existing service's responsibilities. A small scheduling tool and a large enterprise system have different hidden requirements even if both have a simple visible screen.

The [Model Context Protocol specification](https://modelcontextprotocol.io/specification/2025-11-25) provides a primary example of a standardized interface for exposing tools and resources to model applications. APIs and command-line interfaces can serve related integration roles. An interface makes access possible; authorization and domain semantics still determine what an agent may safely and correctly do.

### Idempotency handles a common failure boundary

An operation is **idempotent** if repeating it has the same intended effect as performing it once. Setting a record's status to “reviewed” can be idempotent under an appropriate definition; appending a new payment or sending another message may not be. Long-running agents must handle the possibility that an action succeeded but its acknowledgment was lost.

For Meridian, retrying document delivery after a timeout could send duplicates. A durable operation identifier and a destination that recognizes already-completed operations can prevent duplicate effects. The identifier must represent the same intended action, and recording completion must be coordinated with the effect. An in-memory flag alone does not survive a crash or solve distributed atomicity.

This is why dependable agent operation draws on established distributed-systems ideas. The novelty of language-driven planning does not remove the need for state, consistency, retries, and recovery. The application becomes easier to generate, while its operational obligations remain real.

## 7.5 Disposable prototypes and composable building blocks [28:30](https://www.youtube.com/watch?v=HA7lZd7zk3M&t=1710s)

The interviewer asks whether customized software remains useful after its initial creation. Rauch describes both short-lived sales demonstrations and long-lived infrastructure. He also describes a new support pattern: customers may arrive through an agent without understanding the underlying platform, so the execution trace becomes essential for diagnosing what happened.

### Short lifetime can be economically rational

A demonstration used for one customer conversation can be valuable if it improves communication or reduces uncertainty enough to justify its cost. Its short life does not make it a failure. Conversely, generating many abandoned applications is not automatically productive merely because creation was cheap.

Let a prototype cost $C_p$, improve the probability of a valuable decision by $\Delta p$, and let the incremental value of that decision be $V$. In a simplified expected-value comparison, the prototype is worthwhile when $\Delta pV>C_p$. At cost 200, a two-percentage-point improvement in a 20,000-dollar opportunity has expected value 400. The model requires a causal estimate of the improvement, not just a compelling demo.

Long-lived infrastructure has a different criterion: correctness, maintainability, security, and compatibility across many uses. Rauch notes that difficult code can still require multiple agents and experienced humans to inspect a small change. Treating every software artifact as disposable would discard the very reliability on which rapid creation depends.

Meridian should label a generated portal as a demonstration or a production service with an explicit support horizon. A prototype's success can justify further investment, but it should not silently acquire production responsibilities because a user likes the interface.

### Agent traces become part of support evidence

When a coding agent chooses tools, edits files, and deploys a service, the user may not know which step introduced a problem. A useful trace records actions, inputs or safe references to them, versions, errors, and outcomes. It should avoid exposing unnecessary secrets or unrelated customer data.

The trace can become an evaluation case after review. A recurrent deployment failure might indicate misleading documentation, an ambiguous tool schema, a platform bug, or a model error. Those require different fixes. Training on a final error message without the relevant path may conceal the cause.

This connects directly to Chapter 6: useful feedback is structured evidence about a task, not simply a thumbs-up or a deployment count. The platform and the agent can improve together when failures are attributed to the correct layer.

### Local reasoning reduces the context needed for a change

Rauch attributes some agent preference for his ecosystem to documentation, existing code, composability, and APIs that let a developer reason locally. The [React documentation](https://react.dev/learn/thinking-in-react) illustrates component decomposition and explicit data flow. The relevant principle is to make a unit's responsibilities and dependencies understandable without inspecting every unrelated part of the application.

Suppose a change requires understanding $k$ modules with interface descriptions of average length $b$, plus local implementation of length $l$. A rough context burden is $kb+l$. If hidden cross-module dependencies force reading an entire codebase of size $B$, the burden can approach $B$ instead. This is a heuristic model of information needed, not a measured token law or proof that any framework always yields better agent performance.

A well-defined component can be reused because its inputs, outputs, state, and effects are constrained. Tailwind's local styling and React's component structure are examples discussed in the lecture. They do not make arbitrary components automatically portable: global styles, dependencies, environment assumptions, and accessibility still need attention.

The reported “86 out of 86” deployment choices and component-share figures describe a particular report or sample mentioned by the speaker. They are not a census of all coding agents or the global market. Training exposure, retrieval, task selection, available tools, and commercial integrations can all influence choices. The source itself says the preference is not permanently fixed.

## 7.6 Platform scope, reuse, and value capture [36:30](https://www.youtube.com/watch?v=HA7lZd7zk3M&t=2190s)

Asked why Vercel builds across many categories, Rauch emphasizes using its own platform and reusing existing infrastructure. The gateway reuses parts of a global delivery and compute system; sandboxes reuse virtualization expertise developed for deployments. He also describes discarding or deprioritizing products rather than treating every experiment as a permanent commitment.

### Scope can be economical when assets are shared

An **economy of scope** exists when producing two services together costs less than producing them separately at comparable outputs. Let separate costs be $C_A$ and $C_B$, and joint cost be $C_{AB}$. Scope economies exist when $C_{AB}<C_A+C_B$. Shared fixed infrastructure, operations, and distribution can create the difference.

For a constructed example, two standalone services each need four million of platform infrastructure and two million of specific development. Separate cost is twelve million. If a shared platform costs five million and each service still requires two, joint cost is nine million, saving three. Integration can also create coordination costs, common failure risks, or product constraints, so the inequality is an empirical question.

The lecture's reported percentage of reused infrastructure is an operating claim, not a measured universal saving. Reusing code does not mean reusing every reliability requirement or avoiding all new engineering. A token gateway and a web-content delivery system share mechanisms while differing in state, provider semantics, cost, and generated-output behavior.

For Meridian, an existing authentication and workflow platform may make a new customer portal economical. But shared infrastructure can transmit failures across products. The design should identify which components can be shared and which boundaries must remain isolated. Cost efficiency and concentration risk should be reported separately.

### Infrastructure value follows useful completion

Rauch argues that model-generated software still needs deployment, a runtime, domains, and security. These are complements that turn an idea into something users can reach and trust. A model becoming better can increase demand for such complements rather than eliminate them.

This is the concrete basis for his value-capture thesis. An infrastructure provider benefits when it makes useful deployment easier and more dependable. It does not necessarily capture all the value it creates: competitors, open-source alternatives, customer bargaining, and underlying cloud costs constrain margins.

Meridian can apply the same reasoning to its own product. If it merely forwards a prompt, its contribution may be easy to replace. If it reliably integrates customer evidence, checks outputs, handles long-running jobs, and provides an accountable review process, it supplies a broader service. The durability of that advantage still depends on continued execution and the alternatives customers can choose.

### Security and operations can grow with creation

Lower creation cost can increase the number of deployed systems, each with credentials, dependencies, data, and potential maintenance needs. That expands the importance of inventory, access control, patching, and observation. It also creates opportunities to automate those functions, as Rauch's self-operating-cloud vision suggests.

The economic question is whether automation reduces total operational burden faster than the installed base grows. Let $N$ be services and $m$ maintenance effort per service. Total effort is $Nm$. A fourfold increase in services with a twofold reduction in effort per service still doubles total effort. This identity explains why easier coding can coexist with continued demand for experienced engineers.

The final energy discussion makes the physical complement explicit: compute services still consume power. Software abundance changes demand and allocation; it does not abolish material constraints. The course's hardware and facility chapters remain relevant even at the application end of the stack.

## 7.7 Consumption pricing, quotas, and reliable action [44:00](https://www.youtube.com/watch?v=HA7lZd7zk3M&t=2640s)

The closing questions ask which businesses are exposed and which can serve the new demand. Rauch criticizes static content businesses, restrictive builders, and slow access to products, while favoring interfaces that agents can use directly. He provocatively calls for removing arbitrary rate limits, then immediately preserves the need for operational controls and protection against abuse and unaffordable consumption.

### A quota is a product decision and a control mechanism

A **rate limit** bounds activity over a time window; a **budget** bounds cumulative expenditure or another resource. They solve related but different problems. A customer can remain under a per-minute limit while accumulating a large monthly bill. A budget alone may not prevent a short burst from overwhelming a service.

Let a request consume expected cost $c$ and arrive at rate $\lambda$ requests per second. Expected spending rate is $c\lambda$ dollars per second under stable averages. If a customer has remaining budget $B$, a naive expected exhaustion time is $B/(c\lambda)$. Variable request size, retries, and model choice can make actual consumption diverge, so practical controls meter or reserve resources rather than rely only on an average.

At cost 0.02 per request and fifty requests per second, spending is one dollar per second. A 3,600-dollar budget lasts one hour under the simplified model. If an agent begins generating ten times as much work per request, a request-count limit no longer represents the same resource boundary.

Rauch's point is that limits based on old human production rates can unnecessarily constrain legitimate agent demand. Removing them blindly would be a different mistake. The useful design supports explicit customer budgets, scalable capacity, visible usage, and limits tied to real operational constraints.

### Retry semantics belong in the economic model

A failed acknowledgment can cause repeated work and repeated billing unless the system tracks logical operations. Meridian should separate an attempt identifier from an operation identifier: several attempts may belong to one intended document delivery. The following in-memory teaching example makes that distinction visible.

Inputs are an operation key, content, and two dictionaries representing stored results and delivered records. It returns the same result for a repeated identical operation and rejects reuse of the key with different content. The only effects are mutations of those supplied dictionaries. It does not send messages, persist data, or provide crash-safe distributed execution.

```python
def deliver_once(key, content, results, delivered):
    if key in results:
        old_content, receipt = results[key]
        if old_content != content:
            raise ValueError("operation key reused for different content")
        return receipt
    receipt = f"receipt-{len(delivered) + 1}"
    delivered[receipt] = content
    results[key] = (content, receipt)
    return receipt


results, delivered = {}, {}
first = deliver_once("job-1", "approved draft", results, delivered)
retry = deliver_once("job-1", "approved draft", results, delivered)
assert first == retry and len(delivered) == 1
try:
    deliver_once("job-1", "changed draft", results, delivered)
except ValueError:
    pass
else:
    raise AssertionError("conflicting operation was not rejected")
```

There is an intentional boundary: if a real external effect occurs and the process crashes before the completion record is durable, this pattern alone can still duplicate the effect after restart. Production requires a transaction, a destination-supported idempotency mechanism, or another protocol suited to the action. A working toy example is not a proof of exactly-once effects across a network.

The chapter's economic model is now complete enough to guide a deployment decision. Creation cost, workflow reliability, routing, runtime, authoritative state, operational maintenance, and consumption controls all affect cost per accepted service outcome. Coding agents can reduce important costs and expand what people build, while making these remaining responsibilities more—not less—important to understand.

## Exercises

1. **Compute lifecycle savings.** Creation, verification, deployment, and first-year operation cost 8,000, 3,000, 1,000, and 4,000. AI reduces creation by 75% and deployment by 50%, raises verification by 20%, and leaves operation unchanged. Find the total saving and compare it with the creation-only percentage.
2. **Derive a reliability target.** A fifty-stage workflow must succeed with probability at least 95%. Under independent identical stages, find the required stage success probability. Give a common-cause failure that invalidates the independence model.
3. **Evaluate routing.** A cheap model costs 0.003 and escalates 20% of cases to a model costing 0.025. Find expected model cost. If routing introduces additional error probability 0.002 with loss ten dollars, compare total expected cost with always using the larger model, assuming its baseline loss is already common to both.
4. **Distinguish interfaces from records.** A team recreates a sales dashboard in two days while continuing to use the original CRM database, permissions, and workflows. State exactly what has been replaced and design a test for a claimed full replacement.
5. **Find the crash gap.** In the code example, place a hypothetical crash after the external effect but before recording completion. Explain the duplicate risk and propose a destination-supported idempotency design. What should happen if the same key is reused for changed content?
6. **Price disposable software.** A one-use prototype costs 300 and may increase the probability of winning a 50,000-dollar contribution opportunity. Derive the minimum causal probability improvement needed to justify it. Explain why comparing customers who chose to use prototypes with those who did not may overstate the benefit.

## Solutions and discussion

1. Original total is 16,000. New cost is $2{,}000+3{,}600+500+4{,}000=10{,}100$, saving 5,900 or 36.875%. Creation alone fell 75%, but the other obligations remain and verification became more expensive. The comparison assumes equivalent quality and support scope; if generated code creates later maintenance costs, the first-year horizon may omit an important consequence.

2. Require $p^{50}\geq0.95$, so $p\geq0.95^{1/50}\approx0.998975$, or about 99.8975%. A shared authentication outage can fail every stage together, making independent multiplication inappropriate. Recovery and alternative paths can also change the structure. End-to-end measurement is needed alongside the component target.

3. Model cost is $0.003+0.2(0.025)=0.008$. Additional expected error cost is $0.002(10)=0.020$, giving 0.028, which exceeds the larger model's 0.025 by 0.003. The cheap route saves inference expense but loses on this expected-loss comparison. If errors have hard acceptance limits, the decision should enforce those separately.

4. The team replaced a presentation and interaction layer. A full replacement would also need to reproduce authoritative data behavior, access rules, business workflows, integrations, reporting, reliability, and migration. A test should enumerate those responsibilities and run representative authorized and unauthorized actions, concurrent updates, failures, and recovery. Visual similarity or a fast prototype does not establish functional equivalence.

5. The destination may have performed the action while the caller has no durable record of success. Retrying can repeat it. A destination that stores the operation key with the result atomically can return the prior result for the same key rather than perform the effect again. It should reject a key reused with a different payload, because that represents a different logical operation. Retention and key scope must cover the retry window and customer boundary.

6. Require $50{,}000\Delta p>300$, hence $\Delta p>0.006$, a 0.6-percentage-point improvement. Users who choose prototypes may already have better opportunities, more motivated teams, or different customers. A randomized or carefully controlled comparison would better isolate the prototype's causal contribution. The expected-value model also needs the opportunity value to be contribution rather than gross revenue if delivery costs remain.

## Primary-source references

- Guillermo Rauch, [original coding-AI conversation](https://www.youtube.com/watch?v=HA7lZd7zk3M), Spring 2026. Source of platform accounts, examples, strategic claims, and Q&A.
- React, [Thinking in React](https://react.dev/learn/thinking-in-react). Primary explanation of component structure and data flow.
- Vercel, [AI Gateway documentation](https://vercel.com/docs/ai-gateway) and [Sandbox documentation](https://vercel.com/docs/sandbox). Primary product and implementation descriptions.
- Vercel, [Workflow repository](https://github.com/vercel/workflow). Primary reference for durable workflow infrastructure.
- Model Context Protocol, [2025-11-25 specification](https://modelcontextprotocol.io/specification/2025-11-25). Versioned primary interface specification.
- METR, [Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity](https://metr.org/Early_2025_AI_Experienced_OS_Devs_Study-paper.pdf), 2025, and [experiment-design update](https://metr.org/blog/2026-02-24-uplift-update/), February 2026. Scoped evidence and limitations on productivity measurement.

**Coverage boundary.** The full caption sequence informs the chapter: biography and open source, developer experience, deployment and creator expansion, long-running agents, rich interfaces, three infrastructure roles, support/gateway/sandbox products, autonomous operations, Meta and Notion examples, parking software, the qualified Salesforce example, disposable demonstrations, agent traces, component selection and composability, platform reuse, value capture, security, consumption pricing, rate-limit qualification, and energy/space interests. Company statistics and sample-choice percentages remain attributed. No unseen chart or platform behavior is independently benchmarked here; Meridian and all calculations are teaching constructions.
