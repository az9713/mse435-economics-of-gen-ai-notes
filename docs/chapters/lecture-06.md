# 6. Enterprise learning: objectives, verifiers, specialization, and feedback

Yash Patil's central question is how a generally capable model becomes good at a particular organization's work. His account moves from representation learning and pretraining to post-training, verifiable rewards, evaluation, enterprise specialization, and continual learning. The concrete examples are menu extraction, rapid code-bug detection, and learning from production interactions. Their common feature is that useful improvement requires an operational definition of good output.

Meridian, our invented documentation service, now receives scanned customer forms and must convert them into structured records under each customer's rules. Its current model produces plausible text but sometimes attaches a field to the wrong entity or overlooks an exception. We will use this task to connect the lecture's learning methods to a single decision: how should Meridian improve accepted outcomes without losing reliability, speed, or cost control?

## 6.1 From learned representations to a usable assistant [00:10](https://www.youtube.com/watch?v=LRGX-gTegVA&t=10s)

Patil recounts student projects, joining OpenAI through a research pathway, working on evaluations, and later helping develop long-horizon agent research. His advice to take on difficult, neglected evaluation work is connected to the chapter's technical argument: deciding what good behavior looks like can determine the direction of a training program.

He describes enterprise models as generally intelligent systems that lack knowledge of a particular business. This complements Ghodsi's preceding argument about context, while adding another intervention: change the model's behavior through task-specific training. Retrieval, prompting, tool design, and weight updates solve different parts of the problem and should be compared rather than treated as mutually exclusive doctrines.

### Representation learning changes what is hand-designed

A **representation** is an internal encoding of input information used to support prediction or action. In representation learning, training adjusts that encoding along with other parameters rather than relying entirely on manually designed features. This does not mean that researchers understand nothing about a model, as the conversation rhetorically suggests. Architecture, objective, and many behaviors are known; a complete causal account of all internal computations is much harder.

The original [AlexNet paper](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) is a primary example of combining a deep convolutional network, large labeled image data, and GPU computation to improve image classification. The lecture uses it as a pivotal historical moment, not the literal invention of neural networks or learned representations.

The [transformer paper](https://arxiv.org/abs/1706.03762) introduced an attention-based sequence architecture that exposed useful parallelism during training. Its relevance here is architectural: the arrangement of computation can make larger-scale learning feasible. Autoregressive generation still proceeds through dependencies between output tokens, so training parallelism should not be confused with producing every future token independently at once.

### Define the model and the objective before choosing an algorithm

Let $x$ be an input task including permitted context, $y$ an output sequence or structured record, and $\pi_\theta(y\mid x)$ a model's conditional distribution parameterized by weights $\theta$. Meridian ultimately cares about a task loss $L(y,x)$, which measures errors under the customer's rules. Training objectives are procedures for adjusting $\theta$; they are not automatically identical to this business loss.

For next-token pretraining, let a sequence contain tokens $w_1,\ldots,w_T$. Its average negative log-likelihood is

$$
\mathcal L_{NLL}(\theta)
=-\frac{1}{T}\sum_{t=1}^{T}
\log \pi_\theta(w_t\mid w_1,\ldots,w_{t-1}).
$$

The logarithm is natural here, so loss is measured in nats per token. A token assigned probability one contributes zero; probability 0.5 contributes about 0.693; a very low probability incurs a large penalty. Training encourages the model to assign more probability to observed continuations. It does not directly require it to follow an instruction, respect a customer's policy, or admit that relevant information is missing.

Patil's dinner-invitation example makes this distinction concrete. Continuing text with plausible names is not the same as asking whom the user knows or whom they want to invite. Post-training can teach a conversational response pattern and preferences about helpfulness. Yet the model still needs the actual guest information to give a grounded answer.

For Meridian, this means that linguistic plausibility is only an initial capability. The service must identify entities, relationships, missing evidence, and applicable rules. Its acceptance criterion should be specified before deciding whether the next improvement comes from more context, a different prompt, a new model, or task-specific training.

## 6.2 Scaling, post-training, and verifiable rewards [08:45](https://www.youtube.com/watch?v=LRGX-gTegVA&t=525s)

The lecture describes pretraining scale, compute-optimal allocation, human-feedback methods, and reasoning models as successive developments. It also argues that coding and mathematics are attractive because parts of their outputs can be checked automatically. The important distinction is between generating a candidate and obtaining a trustworthy learning signal about it.

### Different training stages optimize different evidence

The [Chinchilla study](https://arxiv.org/abs/2203.15556) examines how model size and training data should scale together under a pretraining budget. It supports a resource-allocation lesson: increasing parameters while neglecting data can be inefficient. It does not imply that all valuable data is public internet text or that the same relation governs every downstream task.

**Supervised fine-tuning**, or SFT, trains on examples of desired outputs, often using a conditional likelihood objective. **Reinforcement learning from human feedback**, or RLHF, uses human judgments to guide optimization, commonly through a learned reward model. Ouyang and colleagues' [InstructGPT paper](https://arxiv.org/abs/2203.02155) describes a sequence of demonstrations, preference comparisons, and reinforcement learning. Its findings concern evaluated behavior on its prompt distribution, not a guarantee of truth or safety in every context.

**Reinforcement learning with verifiable rewards**, or RLVR, uses a reward that can be computed from a check such as a test result or a mathematically checkable answer. The verifier need not be perfect merely because it is deterministic. A program can pass incomplete tests while violating the specification, and a mathematical final answer can be correct for the wrong reason or under an unintended interpretation.

Patil describes reasoning behaviors emerging under reward-based training. That should not be read as a universal claim that no reasoning model ever uses supervised examples, demonstrations, or other training stages. The [DeepSeek-R1 report](https://arxiv.org/abs/2501.12948) distinguishes specific training variants and stages. The defensible claim is that optimizing appropriate rewards can produce useful behaviors that were not explicitly scripted token by token.

### Expected reward connects sampled behavior to learning

For a fixed input $x$ and finite set of possible outputs, let reward be $R(y,x)$ and define expected reward

$$
J(\theta\mid x)=\sum_y\pi_\theta(y\mid x)R(y,x).
$$

Assume the reward does not directly depend on $\theta$ and probabilities are differentiable. Differentiating and using $\nabla_\theta\pi_\theta=\pi_\theta\nabla_\theta\log\pi_\theta$ where probabilities are positive yields

$$
\nabla_\theta J
=\sum_y\pi_\theta(y\mid x)R(y,x)
\nabla_\theta\log\pi_\theta(y\mid x).
$$

The gradient $\nabla_\theta$ is the vector of partial derivatives with respect to weights. This identity explains why sampled outputs with rewards can estimate a direction of improvement. Practical methods need variance reduction, stable optimization, constraints, and careful handling of long trajectories; the equation is not a complete training recipe.

If a model produces a correct record with probability 0.3 and the reward is one for correctness and zero otherwise, expected reward is 0.3. Increasing probability of truly correct outputs improves the objective. If the verifier instead rewards a superficial formatting trick, optimization can improve the measured objective while worsening the business task. The alignment between reward and intended outcome is therefore central.

### Code is a useful interface but not a universal oracle

The source notes that code can create slides, operate tools, and express many workflows. Executing code can verify structural properties: a file exists, a table has required columns, or a function passes specified tests. It cannot by itself establish that a slide is persuasive, a claim is true, or the chosen business action is appropriate.

For a slide-generation task, one could combine a structural score with a human-preference model. Let $R_s$ measure structural validity and $R_a$ aesthetic preference, and define $R=\alpha R_s+\beta R_a$ with explicit nonnegative weights. The weights encode a tradeoff. If structural validity is mandatory, it may be better represented as a hard constraint rather than a score that aesthetics can compensate for.

Meridian faces the same issue. A well-formatted record with the wrong customer identifier should not pass because other fields look good. Some errors require rejection regardless of average quality. Defining that boundary is part of the product, not an afterthought to training.

## 6.3 Data scarcity, environments, and evaluations [17:15](https://www.youtube.com/watch?v=LRGX-gTegVA&t=1035s)

The conversation distinguishes internet-scale pretraining data from interactive environments that let a model try a task repeatedly and receive feedback. Patil describes synthetic data, richer use of existing documents, and the importance of evaluations that define a research or enterprise objective.

### Repeated trials add experience, not necessarily independent information

An **environment** supplies task state, permitted actions, transitions, and feedback. In a code environment, the agent might edit a repository, run tests, inspect failures, and revise. A **rollout** is one trajectory through those interactions. Running many rollouts can reveal which strategies succeed, provided the feedback is informative.

If independent attempts succeed with probability $p$, the probability of at least one success in $k$ attempts is $1-(1-p)^k$. With $p=0.1$ and $k=20$, this is about 87.84%. That calculation describes search success, not learning. Updating a model from those attempts is a separate process, and selecting the good attempt requires a reliable verifier.

Attempts may also be highly correlated. If all repeat the same mistaken interpretation, the independence formula overstates the benefit. Synthetic variations of a document can expand token count without adding new facts. Useful data expansion changes the learning signal, coverage, or representation of relevant structure; raw volume alone is not enough.

The lecture's “data wall” should therefore be understood as a constraint on useful accessible training material under a particular method, not the assertion that no new human or experimental information will ever exist. Enterprise feedback, scientific experiments, and interaction can supply different information, with their own costs, rights, and quality problems.

### A verifier has its own error distribution

Let $C$ denote an actually correct candidate and $V$ a verifier accepting it. Suppose the base correctness rate is $\Pr(C)=0.2$, verifier sensitivity is $\Pr(V\mid C)=0.95$, and false-accept rate is $\Pr(V\mid\neg C)=0.1$. Then

$$
\Pr(C\mid V)=
\frac{0.95(0.2)}{0.95(0.2)+0.1(0.8)}
\approx0.7037.
$$

Despite high sensitivity, nearly 30% of accepted outputs are wrong under this constructed distribution. The base rate and false accepts matter. Increasing the number of generated candidates can produce more accepted errors as well as more accepted successes.

For Meridian, a schema validator can prove that a record has the required form, but not that the source document supports each field. Separate checks are needed for structure, entity linkage, factual extraction, and policy compliance. Human review can help establish labels, but reviewers also need guidance and disagreement handling.

### Evaluation defines the target and can be overfit

The captions name “Cinebench” in a discussion of coding issue resolution; the context strongly indicates SWE-bench. The [original SWE-bench paper](https://arxiv.org/abs/2310.06770) evaluates systems on real repository issues with corresponding tests. We correct the likely caption error while avoiding the broader claim that one benchmark alone caused an entire research field's development.

An **evaluation set** is a collection of tasks and scoring rules used to assess a system. A **training set** supplies optimization examples; a **development set** supports iteration and selection; a genuinely held-out test set estimates performance after those choices. Repeatedly inspecting test outcomes and adapting to them turns the test into another development signal.

Patil's statement that evaluations set the roadmap captures both their value and their danger. A clear target coordinates research, but optimizing a narrow metric can miss important behavior. Two enterprises may legitimately require different outputs for superficially similar tasks. Evaluation should encode those differences explicitly rather than treating one public score as a sufficient statistic.

Meridian should partition data by source entity or time where leakage is plausible. If pages from the same form template appear in both training and test data, the model may benefit from near-duplicate structure. A separate test on new customers, changed policies, and unusual layouts can reveal whether it learned transferable behavior or memorized familiar cases.

## 6.4 Enterprise specialization: the menu is a relational object [26:00](https://www.youtube.com/watch?v=LRGX-gTegVA&t=1560s)

Patil explains Applied Compute's specialization thesis through DoorDash menu ingestion. He describes merchants supplying unstructured information and menus that must become a storefront with specific rules for items, modifiers, add-ons, and combinations. The difficult part is not merely reading characters; it is reconstructing the relationships and customer-specific semantics.

### Extraction differs from transcription

**Optical character recognition**, or OCR, identifies text from an image. A **vision-language model**, or VLM, combines visual input with language processing. Either can supply useful components, but the business task may require a structured interpretation beyond the recognized text.

Consider an invented menu with “sandwich,” “add cheese,” and “choice of side.” A flat list of those strings loses which options belong to which item, which are mutually exclusive, and which change price. Similarly, Meridian's forms may contain names, dates, and amounts that are individually read correctly but attached to the wrong account or event.

Represent the desired output as entities $E$ and typed relationships $G\subseteq E\times\mathcal R\times E$, where $\mathcal R$ is the set of relationship types. For example, an option can be linked to an item by an “allowed modifier” relation. Attribute values and constraints supplement this graph. Correctness must assess both entities and relationships.

A simple task loss can be written

$$
L=\alpha N_{missing}+\beta N_{wrong}+\gamma N_{relation}
+\delta N_{constraint},
$$

where the four counts measure omitted required fields, incorrect values, incorrect relationships, and violated constraints. The nonnegative weights reflect task consequences. This is a teaching model; a real product may require normalized rates, severity categories, or hard rejection for particular errors. The choice of loss determines which corrections training will prioritize.

Suppose one output has no missing fields but two incorrect modifier links, while another misses one optional description but has all relationships correct. A character-accuracy metric could prefer the first even though it produces a worse storefront. The loss should reflect the actual customer outcome rather than the easiest available proxy.

### Human correction can become a training signal

The source describes humans correcting model outputs and using the difference from desired output to define error or reward. This can convert domain expertise into repeated feedback. It requires a stable representation, consistent annotation, and enough information to distinguish model error from ambiguous source material.

Meridian should record the original input, relevant policy version, model output, correction, and reason. If a reviewer silently applies knowledge absent from the input, training may ask the model to infer an impossible answer. The correct response might instead be to request missing information. This is where Chapter 4's context problem and Chapter 6's optimization problem meet.

The speaker argues that directly optimizing the desired outcome can outperform repeated prompting for a specialized task. That does not establish that prompting is never useful or that every enterprise needs its own weights. The alternatives should be compared under the same held-out evaluation and operational constraints. Retrieval may solve missing facts; structured output constraints may solve formatting; post-training may solve a recurring behavior pattern.

### Waiting for the next frontier model has an opportunity cost

The interviewer asks whether a future general model could make specialization unnecessary. Patil emphasizes time to value and the continuing specificity of enterprise requirements. The economic decision compares the benefit available now with specialization cost, maintenance, and the chance that a later model reduces the advantage.

Let specialization cost be $F$, monthly net benefit be $B$, and the expected useful window before a required redesign be $m$ months. Ignoring discounting and uncertainty, net benefit is $mB-F$. If $F=120{,}000$, $B=30{,}000$, and the window is six months, the result is positive 60,000. If the window is two months, it is negative 60,000. The calculation makes the timing assumption visible rather than assuming either perpetual advantage or immediate obsolescence.

Benefits can include lower error-remediation cost, faster delivery, or higher revenue, not only cheaper inference. Maintenance includes collecting new labels, re-evaluating on policy changes, and rebasing on a new foundation model. A specialization program should preserve portable evaluations and data definitions even if the current model is later replaced.

## 6.5 Small specialists, compute budgets, and system co-design [30:45](https://www.youtube.com/watch?v=LRGX-gTegVA&t=1845s)

The lecture compares pretraining and post-training compute, then describes a fast bug-catching model and an ensemble in which a general model orchestrates specialized components. The common theme is matching the model to a narrow task under a cost and latency constraint.

### A compute ratio needs matched accounting

Patil offers an approximate DeepSeek-based comparison suggesting a small post-training fraction and immediately notes that reinforcement-learning expenditure is increasing. We do not treat the quoted 5% as a verified universal ratio. The [DeepSeek-V3 technical report](https://arxiv.org/abs/2412.19437) reports 2.788 million H800 GPU-hours for its stated full-training accounting. That number is not, by itself, a complete research-program cost or a directly matched denominator for every later R1 training claim.

A fair comparison specifies hardware, useful utilization, which training stages are included, data generation, experiments that failed, evaluation, engineering, and the model version. GPU-hours on different devices are not equivalent units of effective computation. A ratio can be informative only after its numerator and denominator share a meaningful boundary.

The economic insight survives the accounting uncertainty: a company may adapt an existing model without paying the full cost of foundational pretraining, while increasing investment in post-training if additional rewards remain valuable. Low adaptation cost is an opportunity, not a fixed law that adaptation will always remain a tiny fraction of total compute.

### The Pareto frontier is task-specific

For a fixed task distribution, describe a system by quality $q$, cost $c$, and latency $t$. A system is **Pareto dominated** if another has at least as much quality, no more cost, and no more latency, with one strict improvement. The Pareto frontier contains systems not dominated in that comparison set. Choosing among them requires preferences or constraints.

Patil's bug-detection example targets feedback fast enough to be useful when a developer saves a file. A large general model may have strong average reasoning but miss the latency budget. A smaller trained specialist may provide better useful performance on that narrow task. The source's production and speed claims remain attributed; these notes do not reproduce a private benchmark.

He gives Ramp's spreadsheet search as another example, describing reinforcement learning used to improve a narrow operation within a larger product. The point is that specialized components need not replace the general model: a general orchestrator can call a fast search or detection model. This is a practitioner account of the product's approach, not an independently reproduced performance comparison. The appropriate evaluation asks whether the whole workflow becomes faster and more accurate on representative spreadsheets, including cases where the specialist should defer.

Meridian could similarly use a specialist to detect missing signatures or inconsistent identifiers before a larger model drafts the final document. If the specialist is cheap and fast, it may reduce expensive retries. But a missed critical error must not be hidden by an attractive average score. The component needs evaluation within the full workflow.

Let a fast check cost $c_s$ and route fraction $r$ of cases to a general model costing $c_g$. Expected model cost is $c_s+rc_g$ if the check always runs and the general model runs only on routed cases. With $c_s=0.002$, $c_g=0.02$, and $r=0.15$, cost is 0.005 per case. The saving is meaningful only if the unrouted cases meet the acceptance criterion and the routed cases can be resolved.

### Model, harness, and context interact

The lecture emphasizes that optimizing one layer alone can miss the product. A better harness can supply relevant information, constrain actions, and stop unproductive loops. A specialist can exploit a task-specific distribution. A general model can handle coordination and unusual cases. These roles should be tested rather than assigned by label.

A component improvement can even make the system worse if it changes routing or user behavior. For example, a detector that flags many more possible errors may improve recall while overwhelming reviewers. The relevant metric includes downstream workload and false alarms. Meridian should evaluate both component-level scores and end-to-end outcomes, with a trace showing where each failure originated.

## 6.6 Continual learning from sparse and ambiguous feedback [35:40](https://www.youtube.com/watch?v=LRGX-gTegVA&t=2140s)

Patil presents continual learning as improving a deployed system from its interactions and consequences. He describes examples involving accepted or reverted code suggestions and offline extraction of useful context from past documents and traces. He expects progress through several mechanisms rather than one sudden discovery.

### Persistence, context updates, and weight updates differ

Saving a conversation makes information available later; it does not necessarily change model weights. Retrieving a lesson from previous work changes the next input. Updating a prompt or tool policy changes the harness. A gradient update changes parameters. All can improve future behavior, but they have different failure and rollback properties.

For Meridian, a corrected customer address may belong in a governed record store, not in a broad model-weight update. A recurring extraction error may justify training. A rule about when to ask for clarification may be better expressed in the workflow. The learning system should place information where it can be updated, audited, and restricted appropriately.

The lecture's examples of production training are practitioner descriptions, including uncertainty about timing. We retain the mechanism without treating a chart's unspecified step count as an exact number of hours. In production, interactions are dynamic and not freely replayable like a controlled training environment.

### Acceptance is an imperfect reward

Let $A$ denote user acceptance and $C$ actual correctness. In general, $\Pr(A\mid C)$ and $\Pr(A\mid\neg C)$ both depend on the user, task, interface, and opportunity to inspect the output. A user can accept a plausible error or reject a correct but inconvenient suggestion. A later reversion may reflect changed requirements rather than an original mistake.

Optimizing acceptance alone can favor outputs that are easy to approve rather than outputs that are correct. Meridian needs delayed outcomes and sampled audits where practical, plus error categories that distinguish model, context, workflow, and reviewer failures. Sparse feedback is valuable, but its meaning must be inferred carefully.

Suppose ten percent of documents contain a serious error, and users notice only half of those before acceptance. An apparently high acceptance rate can coexist with five percent of all documents carrying unnoticed errors. The numbers are illustrative, but the mechanism shows why production telemetry needs calibration against independently reviewed cases.

### Large batches reduce noise, not systematic bias

If independent feedback-derived gradient estimates have variance $\sigma^2$, averaging $n$ of them gives variance $\sigma^2/n$. The standard deviation falls as $1/\sqrt n$. This is the mathematical motivation for using larger batches to stabilize noisy learning signals.

The independence assumption matters. Correlated interactions reduce the effective sample size. More importantly, averaging cannot remove a systematic error in the reward. If every reviewer consistently overlooks the same failure mode, a million observations can estimate the wrong objective very precisely.

Continual updates can also harm previously learned behavior, often called **catastrophic forgetting** when the loss is substantial. Evaluation should include both new cases and a retained suite of important old capabilities. A gradual rollout, versioned datasets, model versions, and rollback criteria let the organization discover regressions before they affect the entire service.

For Meridian, a reasonable update cycle separates data collection, label review, candidate training, offline evaluation, limited deployment, and broader release. This is an original operational extension of the lecture's feedback argument. It does not require continuous unreviewed weight changes in response to every user action.

## 6.7 Architecture choices and the economics of the next evaluation [40:00](https://www.youtube.com/watch?v=LRGX-gTegVA&t=2400s)

The closing discussion considers alternatives to transformers, hardware co-design, compute scarcity, custom chips, and the changing data market. Patil favors continuing to scale an approach that works while acknowledging researchers who seek more data-efficient alternatives. He then argues that evaluation and data suppliers must adapt as models become capable of solving earlier tasks.

### An alternative architecture must be compared on a workload

The [Mamba paper](https://arxiv.org/abs/2312.00752) develops selective state-space sequence modeling, offering a primary example of research beyond standard attention-only designs. Its relevance is that architectures make different tradeoffs in sequence processing and state. It is not evidence that one design universally dominates every transformer on every task.

A simplified recurrent state model writes $h_t=f_\theta(h_{t-1},x_t)$ and output $y_t=g_\theta(h_t)$, where $h_t$ is a maintained state and $x_t$ the current input. If state size and per-step work are fixed, processing $T$ steps has work proportional to $T$. But compressing history into a fixed state can make some retrieval behaviors difficult. Complexity, representational capacity, optimization, and actual hardware efficiency must be considered together.

The lecture's point about existing infrastructure is economic: software, chips, skills, and investment create momentum around established architectures. That momentum can make a technically promising alternative harder to deploy. It does not prove the incumbent architecture is optimal, nor does an elegant asymptotic bound establish product superiority.

For Meridian, architecture matters through accepted quality, latency, memory, cost, and maintainability. It should not retrain its product merely because a new architecture has an appealing label. A representative benchmark can determine whether the proposed tradeoff helps its actual long-document and extraction workloads.

### Custom hardware changes the make-or-buy calculation

Patil's enthusiasm for NVIDIA and chip suppliers coexists with concern that their largest customers might build more hardware internally. He connects that possibility to compute scarcity, supplier margins, and the ability to coordinate model architecture with chip design. His margin figure and proposed investment scale are conversational estimates, not a current financial analysis.

The arithmetic in his example needs a small correction: hardware delivering 80% of another device's useful throughput requires $1/0.8=1.25$ times as many devices to match throughput, before accounting for memory, communication, power, or reliability. The caption's approximate 1.2 multiplier is not exact. If the alternative is cheap enough, lower device performance can still be economical; if electricity or space is the binding constraint, additional devices can erase the saving. In-house design also adds fixed engineering expense, schedule risk, and software obligations. This is the same total-system comparison developed in Chapters 2 and 5, now applied to the model developer's procurement decision.

### The frontier moves for data suppliers too

Patil describes a challenge for companies building training tasks: after a model learns today's tasks, tomorrow's tasks may be harder and more expensive to construct. Synthetic generation and automated verification can also replace portions of manual work. He does not claim that all data businesses disappear; he expects the valuable data and environment categories to change.

The **generator–verifier gap** is the difference between the difficulty of producing a solution and checking one. A task can be hard to generate but relatively easy to verify, making repeated search and reward useful. If verification itself is unreliable or expensive, the economics change. Hidden tests help prevent direct exploitation, but they must actually represent the specification.

Meridian's proprietary advantage could lie less in raw form volume than in a maintained evaluation suite, reviewed corrections, policy history, and access to meaningful outcomes. That advantage requires ongoing work. Once the model solves the common cases, the remaining failures may be rarer, more ambiguous, and more consequential. Data collection should follow those errors rather than merely add more examples of what already works.

Patil closes with a personal preference for image generation as a learning aid: turning a paper or syllabus into a visual explanation. The useful connection to evaluation is that a compelling diagram still needs checking against its source. These notes preserve the use case without inferring the contents or correctness of an unseen generated slide.

### A small verifier should expose what it does not check

The following teaching code compares a predicted menu-item record with a reviewed reference. It checks selected fields and modifiers, returns a zero-to-one agreement score, and rejects a missing schema. It makes no network calls and does not train a model. The tests demonstrate both a detected error and a critical limitation: omitted fields outside the chosen schema are invisible to this verifier.

```python
def record_score(predicted, reference):
    required = {"name", "price_cents", "modifiers"}
    if not required <= predicted.keys() or not required <= reference.keys():
        raise ValueError("missing required field")
    matches = [
        predicted["name"] == reference["name"],
        predicted["price_cents"] == reference["price_cents"],
        set(predicted["modifiers"]) == set(reference["modifiers"]),
    ]
    return sum(matches) / len(matches)


truth = {"name": "Sandwich", "price_cents": 800, "modifiers": ["Cheese"]}
wrong = {"name": "Sandwich", "price_cents": 800, "modifiers": []}
assert record_score(truth, truth) == 1
assert abs(record_score(wrong, truth) - 2 / 3) < 1e-12
unexamined = dict(truth, allergen_statement="incorrect")
assert record_score(unexamined, truth) == 1
```

The last assertion is deliberately a verifier counterexample, not a desired production behavior. It shows why a high reward can coexist with an important unmeasured mistake. A real system needs a schema and scoring policy aligned with its complete acceptance criteria, including hard constraints where appropriate.

## Exercises

1. **Compare objectives.** A model assigns probabilities 0.8, 0.5, and 0.1 to three observed next tokens. Compute mean negative log-likelihood in nats. Explain why lowering this number does not alone prove better performance on Meridian's structured-record task.
2. **Audit a verifier.** Correct candidates occur 10% of the time. A verifier accepts 90% of correct and 5% of incorrect candidates. Find correctness among accepted outputs. What false-accept rate is required to reach at least 90% correctness among accepted outputs at the same base rate and sensitivity?
3. **Analyze repeated search.** Independent attempts succeed with probability 0.2. Find success probability after five attempts. Give a correlated-failure construction where the formula overstates improvement, and explain why searching is not the same as training.
4. **Price specialization.** A task-specific system costs 90,000 to develop and 5,000 monthly to maintain. It saves 0.03 per accepted task at matched quality. Derive annual break-even volume and explain how an expected additional error cost of 0.01 per task changes it.
5. **Repair the verifier.** Identify two properties missing from the example score besides the explicitly unexamined field. Propose a hard constraint and a separate graded metric, explaining why they should not automatically be averaged together.
6. **Design continual evaluation.** Meridian observes rising acceptance after an update. Design a test that could distinguish improved correctness from easier approval of plausible errors. Include old capabilities, delayed outcomes, and a rollback condition.

## Solutions and discussion

1. Loss is $-[\ln(0.8)+\ln(0.5)+\ln(0.1)]/3\approx1.0730$ nats. This evaluates probability assigned to those observed continuations. Structured-record correctness also depends on entity relationships, customer rules, missing information, and the deployment distribution. A model can improve text prediction while leaving the consequential extraction errors unchanged.

2. Correct accepted mass is $0.1(0.9)=0.09$ and incorrect accepted mass is $0.9(0.05)=0.045$, giving posterior $2/3$. For false-accept rate $f$, require $0.09/(0.09+0.9f)\geq0.9$. Rearranging gives $f\leq1/90\approx0.01111$, or about 1.11%. High sensitivity alone is insufficient when correct candidates are rare.

3. The probability is $1-0.8^5=0.67232$. If a latent task property makes the system either always succeed or always repeat the same error, with 20% of tasks in the first category, five attempts still succeed on only 20% of tasks. Repeated search samples outputs; training changes the distribution used for future outputs. A verifier and an update procedure are additional requirements for learning.

4. Annual fixed expense is $90{,}000+12(5{,}000)=150{,}000$. At 0.03 net saving, break-even is five million accepted tasks. With additional expected error cost 0.01, net saving is 0.02 and the threshold rises to 7.5 million. The comparison assumes the error can be represented as expected monetary loss; an unacceptable error category should instead be constrained directly.

5. The score ignores duplicate modifiers because it converts lists to sets, and it does not validate types, modifier prices, allowed combinations, or relationships to other items. A hard constraint could require every modifier link to reference an existing permitted item. A graded metric could measure description-text fidelity. Averaging them could let excellent prose compensate for an invalid relationship, which would violate the intended service boundary.

6. Randomly sample comparable tasks for blinded review against authoritative sources, separating correctness from user acceptance. Include difficult new cases and a retained suite of old task categories. Track delayed corrections, reversions with reasons, and downstream outcomes rather than treating every click as ground truth. Define rollback if serious-error rate exceeds a predeclared bound or an essential capability regresses, even if acceptance rises. Version the model, context, and harness so the source of the change can be investigated.

## Primary-source references

- Yash Patil, [original enterprise-learning lecture](https://www.youtube.com/watch?v=LRGX-gTegVA), Spring 2026. Source of the history, company examples, specialization thesis, and Q&A.
- Krizhevsky, Sutskever, and Hinton, [ImageNet Classification with Deep Convolutional Neural Networks](https://papers.nips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html), 2012.
- Vaswani et al., [Attention Is All You Need](https://arxiv.org/abs/1706.03762), 2017.
- Hoffmann et al., [Training Compute-Optimal Large Language Models](https://arxiv.org/abs/2203.15556), 2022.
- Ouyang et al., [Training language models to follow instructions with human feedback](https://arxiv.org/abs/2203.02155), 2022.
- DeepSeek-AI, [DeepSeek-R1](https://arxiv.org/abs/2501.12948), 2025, and [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437), 2024–2025. Distinct training reports with distinct accounting boundaries.
- Jimenez et al., [SWE-bench](https://arxiv.org/abs/2310.06770), 2023. Primary repository-issue benchmark description.
- Gu and Dao, [Mamba: Linear-Time Sequence Modeling with Selective State Spaces](https://arxiv.org/abs/2312.00752), 2023. Primary alternative-architecture research.

**Coverage boundary.** The full caption sequence is represented: career and evaluation work, representation learning, transformers, pretraining and scaling, post-training, code and slide rewards, data environments, evaluation design, DoorDash relational extraction, specialization timing, compute ratios, fast bug detection and model ensembles, continual learning, architecture debate, hardware opportunities, changing data markets, and visual-learning product preference. The final image-product anecdote illustrates a preferred learning aid; no unseen generated slide is analyzed. Company performance and private training details remain attributed. Meridian, mathematics, verifier, and exercises are independent constructions.
