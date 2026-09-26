# 3. Building AI factories: electrons, cooling, construction, and capital recovery

Chase Lochmiller presents the data center as the physical system that makes AI services possible. The discussion follows an unusually complete chain: the production of useful computation, energy-first site selection, electrical and cooling systems, construction labor, server deployment, rental economics, managed services, modular facilities, and possible space infrastructure. Its central observation is that the bottleneck moves. Owning chips is not enough when there is nowhere ready to power, connect, and cool them.

To develop the economics, imagine **Aster**, a fictitious infrastructure provider considering a one-megawatt unit of IT capacity. Meridian, the documentation company from the preceding chapters, may buy a service from Aster. Aster's problem is to deliver useful capacity at a cost that customers can support over the assets' lives. The numbers used below are either clearly attributed lecture estimates or explicitly constructed calculations; they are not bids for an actual project.

## 3.1 Digital labor and a production function [03:00](https://www.youtube.com/watch?v=GcCGzfKdCd0&t=180s)

The opening describes AI infrastructure as a combination of data, algorithms, compute, energy, and buildings. Lochmiller then invokes the Cobb–Douglas production function and argues that AI can supply a form of digital labor. His company focuses on the physical and operational layers, attempting to remove constraints between energy development and delivered compute rather than designing chips or foundation models itself.

### What Cobb–Douglas actually says

Let output be $Y$, a capital-services input be $K>0$, human labor input be $L>0$, and technology or efficiency be $A>0$. A simple constant-returns Cobb–Douglas function is

$$
Y=AK^{\alpha}L^{1-\alpha},\qquad 0<\alpha<1.
$$

The units of $A$ depend on how the inputs and output are measured. The expression is a model of production, not an accounting identity and not a claim that all economies have the same substitution possibilities. Taking logarithms and differentiating gives the growth decomposition

$$
\frac{\dot Y}{Y}=\frac{\dot A}{A}
+\alpha\frac{\dot K}{K}
+(1-\alpha)\frac{\dot L}{L}.
$$

This is the precise sense in which growth rates can be decomposed into contributions from technology, capital, and labor under the model. Levels are multiplied in the production function; they are not simply added. The dot denotes change with respect to time. The weights are model parameters, not automatically measured causal effects in every setting.

Lochmiller's digital-labor interpretation raises a modeling choice. If an AI system performs tasks previously done by people, we might introduce effective labor $L_{eff}=L+\theta D$, where $D$ is digital task capacity and $\theta$ converts it into comparable effective units. But that additive form assumes strong substitutability. It fails when human judgment, authorization, physical action, or complementary workflow design remains essential.

Alternatively, AI may increase $A$, change the productivity of capital, or alter the task structure entirely. One should not count the same AI investment as additional capital, additional labor, and an independent technology gain without defining the channels. The lecture supplies a powerful intuition about scalable task capacity; it does not identify a complete macroeconomic production function.

### A physical complement can dominate a digital opportunity

For Aster, a more immediate model is a complementary production system. Let $K_c$ be usable chip capacity, $K_p$ power-supported capacity, $K_h$ cooling-supported capacity, and $K_n$ network-supported capacity, all expressed in equivalent units of the same workload. A limiting approximation is

$$
Q\leq\min(K_c,K_p,K_h,K_n).
$$

If Aster has chips for one megawatt but only half a megawatt of installed cooling, the unused chips do not compensate. Once cooling is expanded, another component may become limiting. This is the lecture's moving-bottleneck argument in a simple form. Real systems allow some substitution and partial operation, but the minimum captures why one missing component can strand expensive assets.

The economic **shadow value** of relaxing a constraint is the improvement in the best achievable objective from a small increase in that constraint's allowance. When cooling is binding and everything else has slack, an extra unit of cooling can be valuable while an extra chip is temporarily worthless. This does not make chips unimportant; it shows that value depends on the state of the whole system.

The operator's integration strategy is therefore understandable: controlling several stages may reduce delays at changing interfaces. It also creates organizational and capital demands. Integration should be evaluated by whether coordination benefits exceed the additional complexity, not assumed superior because it covers more layers.

## 3.2 Energy-first siting and the meaning of a powered shell [09:20](https://www.youtube.com/watch?v=GcCGzfKdCd0&t=560s)

Lochmiller identifies energized data centers—places where chips can actually be installed and operated—as the immediate bottleneck in his account. He contrasts established internet hubs with locating energy-intensive computation near abundant supply. The key move is to transport data to energy rather than always expanding energy transmission to an existing computing hub.

### Cheap energy and usable power are different inputs

**Power** is the rate of energy transfer. One megawatt is one million joules per second. **Energy** accumulates over time; operating at one megawatt for one hour uses one megawatt-hour. Confusing these units can turn a plausible site description into an impossible annual budget.

Let $P_{IT}$ be rated IT power in megawatts, $u\in[0,1]$ average utilization relative to that rating, and $H$ operating hours in the period. Let power usage effectiveness, $\mathrm{PUE}\geq1$, be total facility energy divided by IT energy over the same boundary and period. Then a simplified energy model is

$$
E_{facility}=P_{IT}uH\,\mathrm{PUE}\quad\text{MWh}.
$$

For 100 MW, 80% utilization, 8,760 hours, and PUE 1.2, annual facility energy is 840,960 MWh. At an illustrative average price of fifty dollars per MWh, the energy charge alone is about 42.05 million dollars. This excludes demand charges, contractual terms, onsite generation costs, and other operating expenses. PUE can vary with weather and load; a fixed annual average is an approximation.

An attractive energy price does not establish that the required power is available continuously at the site. Connection capacity, transmission congestion, interconnection schedules, reliability requirements, and the temporal profile of generation all matter. Negative spot prices in some hours do not imply a facility receives free reliable power throughout the year.

### The Abilene example is about constrained geography

The speaker describes West Texas wind and solar resources, transmission constraints, and a large new load willing to consume local electricity. He attributes the site's opportunity partly to renewable development and incentives. His Abilene account includes substations, a gas plant, multiple buildings connected as a large compute cluster, construction employment, and later expansion. The specific capacities and workforce figures remain his source-era operating account.

Crusoe's [own Abilene project description](https://www.crusoe.ai/resources/blog/an-inside-look-at-the-abilene-ai-data-center) independently documents the company's stated energy-first siting and closed-loop cooling approach. It is primary evidence of design intent and company claims, not an external audit of every construction or community-impact figure. The caption alone does not allow us to inspect the aerial image, count installed equipment, or determine what was energized on the day of recording.

The geographic strategy also depends on workload. Batch training can sometimes tolerate distance from end users more easily than an interactive service, although training itself may require excellent internal networking and data access. A latency-sensitive application may need serving capacity closer to customers. “Move data instead of power” is a useful option, not a universal siting rule.

### Across-the-meter operation creates both flexibility and obligations

Later, the speaker describes another Texas site combining local generation, planned storage and other resources, and exchange with the grid. He calls this an across-the-meter approach: export excess energy in some conditions and import when local production is insufficient. The claimed benefit to local ratepayers is a project hypothesis whose realization depends on market rules, cost allocation, and operation.

For a simple hourly balance, let $G_t$ be onsite generation, $I_t$ imports, $X_t$ exports, $B_t$ battery discharge net of charging, and $L_t$ load, all in MW during hour $t$. Ignoring losses for the moment,

$$
G_t+I_t+B_t=L_t+X_t.
$$

Battery state cannot be omitted over time: discharge today requires stored energy from earlier charging, and conversion losses matter. A generation fleet with adequate annual energy can still fail to meet peak or low-renewable periods. The balance must hold each operating interval, subject to network and storage constraints.

For Aster, a useful site comparison therefore includes delivered energy cost, firm power availability, time to energization, carbon and water boundaries, network access, and expansion rights. Buying the cheapest annual-average energy while ignoring delivery timing can strand the rest of the investment.

## 3.3 Electrical conversion, liquid cooling, and water accounting [18:50](https://www.youtube.com/watch?v=GcCGzfKdCd0&t=1130s)

The recording walks through substations, distribution centers, transformers, switchgear, uninterruptible power supplies, chillers, pipes, cooling distribution units, steel, and concrete. These components are the physical explanation for why a data center is more than a warehouse filled with computers. The voltage numbers in the captions are not perfectly consistent; the notes preserve the conversion sequence without reconstructing an unseen electrical schematic.

### Losses compound through a conversion chain

Suppose electrical stages have efficiencies $\eta_1,\ldots,\eta_m$, each between zero and one. If power passes through them in sequence, useful output power is $P_{out}=P_{in}\prod_i\eta_i$. Therefore delivering a specified $P_{out}$ requires

$$
P_{in}=\frac{P_{out}}{\prod_i\eta_i}.
$$

Four stages each at 98% efficiency have combined efficiency about 92.24%. Delivering one MW through that chain requires about 1.084 MW at its input. This is a constructed illustration, not an estimate of the site's actual losses. It explains the speaker's later interest in redesigned power electronics and higher-voltage DC distribution: reducing conversions or improving them can matter at scale.

Reliability, maintainability, fault isolation, and standards constrain such redesigns. Removing a component because it dissipates power is not beneficial if it also removes required protection. Electrical architectures are evaluated as systems under normal and fault conditions, not solely by multiplying nameplate efficiencies.

### Follow heat rather than just water

Nearly all electrical energy consumed by computation ultimately becomes heat that must leave the relevant system. In a simple liquid loop, heat transfer rate is

$$
\dot Q=\dot m c_p\Delta T,
$$

where $\dot Q$ is heat in watts, $\dot m$ coolant mass flow in kilograms per second, $c_p$ specific heat in joules per kilogram-kelvin, and $\Delta T$ the coolant temperature rise in kelvin. With water approximated at $c_p=4{,}180$ and a ten-kelvin rise, removing one MW requires about 23.92 kg/s. This is circulating flow, not water consumed every second.

The speaker describes heat moving from chips to a recirculating water loop and then to outside air through cooling equipment. A closed loop can circulate a large inventory while consuming little replacement water. The inventory, circulation rate, withdrawal, and consumptive use are different quantities. Equating a large filled loop with continuous consumption would misread the design.

Conversely, “closed-loop cooling” does not establish zero total water impact. Makeup water, maintenance, other site uses, electricity generation, and manufacturing have separate boundaries. Ambient temperature also affects the energy needed to reject heat. The [Lawrence Berkeley National Laboratory data-center report](https://energyanalysis.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report) treats electricity and water through explicit system boundaries, which is the useful research connection here. Its national estimates should not be substituted for measurements of one campus.

Aster should report direct site water and upstream effects separately, with period, units, and methodology. An annual total without workload or energy context can be difficult to compare. A ratio alone can also hide growth in the absolute total. Both quantities can be useful when their definitions are stable.

### Cooling capacity and energy efficiency interact

Raising coolant temperature can improve heat rejection opportunities, but chip operating limits, flow, material compatibility, and reliability restrict the choice. More pumping can increase heat transport while consuming additional electricity. A cooling design optimizes the complete operating envelope, not just the largest possible temperature difference in the equation.

For Meridian, this is an indirect but real service concern. A supplier whose advertised compute capacity cannot be cooled in expected weather may throttle or fail its service objectives. The facility's operating envelope and redundancy affect the application's latency and availability. Physical engineering appears in the customer experience through those constraints.

## 3.4 Reliability, checkpoints, and construction economics [22:00](https://www.youtube.com/watch?v=GcCGzfKdCd0&t=1320s)

Lochmiller explains that not every component receives identical backup. In his account, core storage and networking are protected so that checkpoints remain accessible even if the full compute workload stops. This is a reliability design based on consequences, rather than indiscriminately maximizing uptime for every asset.

### A recoverable interruption differs from lost state

A **checkpoint** is saved state sufficient to resume a computation from a known point. Checkpointing can turn a failure from complete loss of progress into bounded rework, provided the checkpoint is valid, durable, and accessible. Backing up storage does not guarantee that a job immediately restarts elsewhere; compatible capacity, network access, software state, and recovery procedures are also needed.

Let checkpoints occur every $\tau$ hours of productive work and take $c$ hours each. Let failures arrive at average rate $\lambda$ per hour, assumed rare and approximately independent of checkpoint timing. If a failure is equally likely within an interval, average lost work is about $\tau/2$. Ignoring restart time and overlapping failures, the fractional overhead is approximately

$$
L(\tau)=\frac{c}{\tau}+\frac{\lambda\tau}{2}.
$$

The first term penalizes frequent checkpoints; the second penalizes long intervals between them. Differentiating gives $L'(\tau)=-c/\tau^2+\lambda/2$. The minimizing interval is

$$
\tau^*=\sqrt{\frac{2c}{\lambda}}.
$$

With a one-minute checkpoint, $c=1/60$ hour, and a failure rate of 0.01 per hour, the interval is about 1.83 hours. This is a teaching approximation, not an operational recommendation for a particular training system. Correlated failures, variable checkpoint cost, repair time, and storage limits require a richer model. Its purpose is to show how an engineering choice follows from competing expected costs.

For an interactive inference request, restarting may be cheap computationally but unacceptable to the customer. For a long training run, losing many hours of state can be expensive even if no external user was waiting. Reliability requirements should follow the workload's consequences. The same nominal uptime percentage does not describe both economic problems adequately.

### Construction labor is a capital cost in this account

The source gives a labor figure around 4.7 million dollars per MW and clarifies that it concerns construction, not recurring annual operating labor. At one GW, that scales to 4.7 billion dollars of capitalized construction labor. If construction spans a different period, annual spending changes even though the project's total does not. The clarification in the dialogue must remain attached to the number.

The discussion includes electricians, welders, plumbers, concrete production, commissioning, insurance, financing during construction, and site work. It emphasizes competition for skilled labor and the need to attract workers to large projects. A data-center build therefore draws on local housing, transport, training, and services as well as industrial equipment.

The speaker also describes rising generation-equipment prices under strong demand. These are source-era observations, not a current price sheet. The underlying mechanism is that supply capacity for specialized equipment can adjust slowly while project demand rises quickly. A component with a small share of total cost may still have a large schedule impact if no substitute arrives in time.

If Aster invests sixty million and earns no service revenue until energization, a delay imposes financing cost and foregone operating cash flow. An inexpensive transformer delivered too late may be economically worse than a more expensive timely alternative. The critical-path question is therefore at least as important as the bill-of-materials question.

### Capital cost needs a defined denominator

“Dollars per megawatt” can refer to utility connection capacity, total facility power, or IT load. Those denominators differ by design and overhead. A quote may include land, generation, shell, fit-out, networking, chips, or only a subset. Comparisons should specify scope before treating price differences as efficiency differences.

The transcript's broad estimate of about twenty million per MW for physical infrastructure and power is useful for understanding the order and composition of investment. It is not a standardized bid transferable to every geography, density, redundancy level, or delivery schedule. Aster's actual budget needs a scope register that prevents omissions and double counting.

## 3.5 Chips, networks, useful life, and the payback trap [30:00](https://www.youtube.com/watch?v=GcCGzfKdCd0&t=1800s)

The next layer is IT equipment. Lochmiller gives an illustrative total near forty million dollars per MW, with the largest share going to GPUs and additional spending on networking, CPUs, storage, fit-out, and deployment. He explicitly notes possible overlap in fit-out costs and that the slides were assembled quickly. We preserve the rough total and the uncertainty rather than forcing the component bars into an audited sum.

### A cluster is more than its processors

The networking discussion distinguishes connections within a rack or tightly coupled domain from the broader network joining racks. Distributed training can require rapid repeated exchange, so a collection of individually capable devices is not automatically a capable training cluster. Topology, bandwidth, latency, congestion, and failures affect useful throughput.

The captions render RoCE imperfectly; the conventional term is **RDMA over Converged Ethernet**. RDMA means remote direct memory access, a communication mechanism that can reduce CPU involvement in data movement under the relevant hardware and software support. Naming the protocol does not establish that a particular network is configured or operated well.

The lecture also notes growing CPU demand for agent orchestration. A GPU-centered cost chart can conceal the conventional computation needed for scheduling, tools, storage, compilation, and sandbox execution. Meridian's complete workflow can bottleneck on those resources even if model inference is fast. The production unit remains the completed service.

### Depreciation, useful life, and market value differ

**Accounting depreciation** allocates an asset's depreciable cost over an accounting life according to a method. **Economic useful life** concerns how long the asset remains worth operating relative to alternatives. **Market value** is what someone will pay at a particular time. These quantities can diverge.

The speaker describes renewed demand and prices for older hardware as a challenge to simple obsolescence assumptions. That is a reason to reassess a forecast, not proof that every chip will remain profitable for a particular number of years. An older device can retain value during scarcity and lose it when power or new capacity becomes abundant. Its resale value also depends on compatibility and location.

Aster's asset portfolio includes buildings and generation equipment that may last much longer than the current compute generation. A single depreciation horizon for the whole project hides this difference. Replacement, residual value, maintenance, and technological compatibility should be modeled by asset class, even if a coarse preliminary model begins with one aggregate number.

### Derive payback and compare it with discounted return

The lecture combines roughly sixty million dollars per MW of initial capital with about fifteen million annual rental revenue and one to two million of selected operating costs. It calls this roughly four-year payback while acknowledging additional engineering and other expenses. Dividing capital by revenue gives four years, but revenue is not free cash flow.

Let $I$ be initial investment and $F>0$ constant annual net cash flow after the included costs. **Simple payback** is $I/F$. With $I=60$ million, revenue fifteen, and included operating expense two, $F=13$ million and simple payback is about 4.62 years. Omitting engineering, financing, taxes, maintenance capital, or replacement can make this optimistic.

At discount rate $r$ and horizon $T$, with no residual value, the constant-cash-flow NPV is

$$
\operatorname{NPV}=-I+F\frac{1-(1+r)^{-T}}{r},\qquad r\ne0.
$$

The annuity factor is the sum of discounted annual payments. At 10% over six years, thirteen million annually has a present value of about 56.62 million, leaving NPV near negative 3.38 million. Thus a project can recover its undiscounted investment within its life and still fail a required-return test. This is precisely why the payback headline cannot settle the economics.

If annual rental revenue scales approximately with productive utilization $u$, write revenue as $R_{max}u$ and annual cost as fixed $F_0$ plus variable $vu$. Annual operating cash flow is then $(R_{max}-v)u-F_0$. A high nameplate price is insufficient if capacity is idle, unavailable, or sold under discounted contracts. The relevant utilization is productive, billable service under contract, not simply equipment powered on.

### Managed services can add value and cost

Lochmiller argues that serving model endpoints can increase revenue beyond renting raw compute. The customer receives model deployment, optimization, scaling, and operations rather than managing individual machines. He illustrates an optimistic revenue case up to roughly thirty million per MW annually. That is a commercial scenario, not a guaranteed margin uplift.

The additional layer also requires engineering, support, evaluation, reliability, and customer acquisition. If Aster doubles revenue but incurs large additional expense or assumes substantial service-level risk, the improvement in cash flow can be much smaller. The right comparison holds the customer outcome and resource use clear while including the full incremental cost of the managed service.

For Meridian, paying Aster a markup may be rational if it avoids greater internal cost or reduces failure. Aster captures value by making the infrastructure more useful, but the amount it can retain depends on alternatives and execution. This returns to the course's central question: technical transformation creates value; competition and contracts determine its division.

## 3.6 Modular facilities and redesigning the electrical stack [40:45](https://www.youtube.com/watch?v=GcCGzfKdCd0&t=2445s)

The speaker describes factory-built modular data centers, including air-cooled and liquid-cooled versions, and reports substantial potential savings relative to parts of the conventional build. The mechanism is to move repeatable work into controlled manufacturing environments and reduce expensive, scarce onsite labor. The modules can also fit power opportunities too small or dispersed for a giant campus.

### Standardization changes where work occurs

A module can package cooling, distribution, and compute interfaces into a repeatable unit. Benefits may include reusable designs, factory testing, purchasing scale, and predictable assembly. Costs include transport constraints, standardized capacity increments, site integration, and the possibility that a design becomes poorly matched to new hardware.

Let conventional cost be $C=C_s+C_o$, where $C_s$ is work potentially standardized in a factory and $C_o$ other cost. If factory production reduces the first part by fraction $a$ and introduces transport and integration cost $T$, new cost is

$$
C'=(1-a)C_s+C_o+T.
$$

Total saving is $aC_s-T$, not $aC$. If standardizable work is 40% of a twenty-million budget, reducing it by half saves four million before transport. Adding one million of transport and integration leaves three million net saving, or 15% of the original total. This illustrates why the lecture's reported savings need a clearly specified denominator.

A modular design may also reduce delivery time. If earlier completion earns operating cash flow sooner, its value can exceed the construction saving alone. Conversely, standardization that delays adaptation to a new cooling requirement can be costly. The relevant comparison combines price, schedule, performance, and adaptability.

### Near-term scarcity and long-term disruption can coexist

Asked for investment views, Lochmiller says incumbent electrical suppliers can be indispensable now while facing longer-term redesign pressure if they do not innovate. He points to solid-state power electronics and changes in voltage architecture. The distinction between horizons is the substantive lesson; the named-company opinions are not transformed into recommendations here.

An incumbent can earn strong returns during a supply shortage and later face substitution. A new entrant can have an elegant design but fail because qualification, reliability, manufacturing scale, and service support take too long. Both outcomes depend on timing. A technically superior architecture is not automatically a commercially ready replacement for infrastructure that must operate reliably for years.

For engineers, the opportunity is concrete: reduce conversion losses, material, installation complexity, and maintenance while meeting fault and safety requirements. For an operator, the challenge is to avoid locking the entire project into an unproven interface solely to obtain a theoretical efficiency gain. Pilot testing and a supported migration path make innovation economically usable.

The same logic explains why physical modularity differs from software virtualization. A virtual machine is a logical abstraction within existing hardware; a physical module still requires land, power, heat rejection, transport, and installation. Standardizing those interfaces is valuable precisely because the physical obligations remain.

Lochmiller also expresses optimism about open models relative to closed models in the later investment discussion. That is a forecast about another layer of the stack, not evidence that physical infrastructure becomes unnecessary. An operator should separate its assumptions about model ownership and distribution from its assumptions about electricity, cooling, and useful compute demand. A change in the winning model supplier can alter customers and bargaining power while leaving substantial infrastructure demand intact.

## 3.7 Space data centers and the limits of abstraction [45:20](https://www.youtube.com/watch?v=GcCGzfKdCd0&t=2720s)

The closing technical question concerns data centers in space. Lochmiller describes interest and a partnership while emphasizing heat rejection, operations, equipment failure, and launch economics. His expectation is that large economic significance is unlikely in the near term. The transcript's statements about future filings and launch-price reductions remain forecasts from that conversation.

### A cold environment does not provide convective cooling

In a vacuum, an external radiator cannot rely on surrounding air to carry heat away. It must radiate energy. For an idealized gray surface of area $A$, emissivity $\epsilon\in(0,1]$, absolute temperature $T$, and effective sink temperature $T_s$, net radiative heat rejection is

$$
\dot Q=\epsilon\sigma A(T^4-T_s^4),
$$

where $\sigma\approx5.6704\times10^{-8}$ watts per square meter-kelvin to the fourth power. This is the Stefan–Boltzmann relation under the assumed geometry and view of the sink. NASA's [space thermal-management material](https://ntrs.nasa.gov/api/citations/19930007716/downloads/19930007716.pdf) treats radiation as a central heat-rejection mechanism.

At 300 K, emissivity 0.9, and a negligible sink temperature, the idealized emission is about 413 watts per square meter. Rejecting one MW requires roughly 2,419 square meters of radiating surface. At 350 K, the requirement falls to about 1,306 square meters. Higher temperature helps because of the fourth power, but component limits and heat transport constrain it. Solar and Earth radiation, orientation, shielding, view factors, and structural mass complicate an actual design.

These calculations do not prove space infrastructure is uneconomic. They show why “space is cold” is not a complete cooling solution. The system still needs to move heat from chips to radiators, deploy enough area, and maintain acceptable temperatures over its operating environment.

### Removing one cost introduces a different asset problem

Space may avoid some terrestrial land or construction requirements, but launch, deployment, communication, radiation tolerance, orbital operations, and repairability enter the cost structure. The speaker's remark about not sending an astronaut to reseat a failed chip captures a major difference: replacing failed equipment is much harder.

If a deployed fleet begins with $N_0$ functioning units and each has an independent constant failure rate $\lambda$, with no repair, expected functioning units after time $t$ are $N_0e^{-\lambda t}$. This model assumes identical independent hazards and ignores common events and degradation. It is useful because it makes declining service capacity explicit rather than assuming every launched unit remains available throughout the financial horizon.

At an illustrative annual failure rate of 5%, expected surviving capacity after five years is about 77.88% of initial capacity. A project might tolerate this through spare capacity, fault-tolerant workloads, or replacement launches, but those strategies cost something. The economic comparison must include the entire service life, not only initial launch price or the absence of concrete foundations.

### A small reproducible engineering calculation

The following functions check the energy, cooling, and radiator models. Inputs use the units named in the function arguments. They return MWh, kg/s, and square meters respectively and reject physically invalid parameters. They are calculations, not design certification or measurements of a real facility.

```python
def annual_energy(it_mw, utilization, pue, hours=8760):
    if it_mw < 0 or not 0 <= utilization <= 1 or pue < 1:
        raise ValueError("invalid power, utilization, or PUE")
    return it_mw * utilization * pue * hours


def water_flow(heat_watts, temperature_rise):
    if heat_watts < 0 or temperature_rise <= 0:
        raise ValueError("invalid thermal load")
    return heat_watts / (4180 * temperature_rise)


def radiator_area(heat_watts, temperature, emissivity=0.9):
    if heat_watts < 0 or temperature <= 0 or not 0 < emissivity <= 1:
        raise ValueError("invalid radiator parameters")
    return heat_watts / (emissivity * 5.670374419e-8 * temperature ** 4)


assert annual_energy(100, 0.8, 1.2) == 840960
assert abs(water_flow(1e6, 10) - 23.92344498) < 1e-7
assert 2419 < radiator_area(1e6, 300) < 2420
```

The final career advice emphasizes learning continuously and using new tools. In the context of this lecture, that advice is more specific than a general exhortation to adapt: the valuable problem can move from chips to power, from power to labor, or from installation to operations. A strong engineer or analyst follows the constraint through the complete system and updates the model when evidence changes.

## Exercises

1. **Audit units and boundaries.** A proposal advertises 50 MW, utilization 70%, PUE 1.25, and electricity at sixty dollars per MWh. Calculate annual facility energy and the energy charge assuming 50 MW is IT power. Explain the change if 50 MW instead denotes total facility power at full load.
2. **Separate flow from consumption.** Derive the water circulation needed to remove two MW with an eight-kelvin temperature rise. Explain why that result cannot establish annual water consumption.
3. **Optimize recovery.** Checkpoints take two minutes and failures occur at rate 0.02 per hour. Derive the optimal interval under the chapter's approximation and its expected fractional overhead. Identify a violation that could make the calculation misleading.
4. **Test the investment.** A one-MW project costs sixty million and generates thirteen million annual net cash flow for six years. At 10%, find the residual value at year six required for zero NPV. Explain why a positive residual estimate requires evidence.
5. **Evaluate modular savings.** Half of a twenty-million construction budget is standardizable. Factory production lowers that part by 30% but adds 1.2 million of transport and site integration. Find net savings and the percentage reduction in total cost. What schedule information would improve the decision?
6. **Stress a space proposal.** Estimate ideal radiator area for five MW at 300 K and emissivity 0.9. Then explain why eliminating terrestrial foundations does not establish a lower lifecycle cost. Include at least three missing terms and one reliability mechanism.

## Solutions and discussion

1. With IT power as the denominator, energy is $50(0.7)(8760)(1.25)=383{,}250$ MWh and the charge is 22.995 million dollars. If fifty MW is total facility rating and the same utilization applies to total draw, energy is $50(0.7)(8760)=306{,}600$ MWh, costing 18.396 million. One must not multiply total facility power by PUE again. Actual contracts and load-dependent overhead can change both simplified results.

2. The flow is $2{,}000{,}000/[4180(8)]\approx59.81$ kg/s. It describes water passing through the heat-transfer loop. The same water can circulate repeatedly. Consumption depends on evaporation, leaks, maintenance, and other losses; upstream water use depends on the energy and manufacturing boundary. A large flow is compatible with low consumptive use, but does not prove it.

3. Here $c=2/60$ hour and $\lambda=0.02$, so $\tau^*=\sqrt{2c/\lambda}\approx1.826$ hours. Each overhead term is about 0.01826, yielding total expected overhead about 3.65%. Correlated failures that also destroy checkpoints, expensive restart, or checkpoint cost varying with state size violate the simple model. The optimal interval must then be recalculated for the actual failure and recovery process.

4. The six-year operating NPV is approximately negative 3.3816 million. A residual $S$ at year six contributes $S/1.1^6$, so $S\approx3.3816(1.1)^6\approx5.99$ million is required. This is a break-even residual, not a forecast. Its plausibility depends on asset condition, replacement needs, land and power rights, compatible demand, and disposal or transfer costs.

5. Standardizable cost is ten million. A 30% reduction saves three million, offset by 1.2 million of added expense, leaving 1.8 million or 9% of the total. Earlier revenue, construction financing saved, installation risk, and the chance of a delayed incompatible module can matter as much as the direct saving. The comparison should use a common completion and service scope.

6. Five MW needs about $5{,}000{,}000/413.37\approx12{,}096$ square meters of ideal radiating area. A practical design also needs heat transport, deployment structure, orientation control, communication, launch, radiation protection, and operations. Equipment failures without repair reduce capacity over time; common failures can be worse than the independent-hazard model. The proposal requires a complete lifecycle and delivered-service comparison, not a comparison of one missing terrestrial cost.

## Primary-source references

- Chase Lochmiller, [original AI-factory lecture](https://www.youtube.com/watch?v=GcCGzfKdCd0), Spring 2026. Source of project accounts, cost estimates, design descriptions, and Q&A.
- Crusoe, [An inside look at the Abilene AI data center](https://www.crusoe.ai/resources/blog/an-inside-look-at-the-abilene-ai-data-center). Primary company description of siting and cooling design.
- Lawrence Berkeley National Laboratory, [2024 United States Data Center Energy Usage Report](https://energyanalysis.lbl.gov/publications/2024-lbnl-data-center-energy-usage-report). Research reference for energy and water system boundaries.
- NASA, [Thermal Management in Space](https://ntrs.nasa.gov/api/citations/19930007716/downloads/19930007716.pdf). Primary technical reference for radiative heat rejection.

**Coverage boundary.** The chapter follows the full caption discussion from production inputs through siting, Abilene, electrical and cooling systems, reliability, labor, the second Texas project, IT capital, depreciation, managed services, modular facilities, electrical innovation, space infrastructure, and career advice. It preserves the speaker's cost-overlap and omitted-expense qualifications. Aerial images, slide bar values not recoverable from speech, and video demonstrations are not reconstructed. Aster, equations, code, and numerical exercises are independent teaching constructions; company claims and forecasts remain attributed.
