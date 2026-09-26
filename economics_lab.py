"""Executable MS&E435 teaching models; no external services."""
import math


def contribution(price, other_cost, request_cost, requests):
    """Chapter 1: dollars per customer per period, before fixed costs."""
    if min(price, other_cost, request_cost, requests) < 0:
        raise ValueError("inputs must be nonnegative")
    return price - other_cost - request_cost * requests


def roofline(peak, bandwidth, intensity):
    """Chapter 2: operations/s from ops/s, bytes/s and ops/byte."""
    if min(peak, bandwidth, intensity) <= 0:
        raise ValueError("capacities and intensity must be positive")
    return min(peak, bandwidth * intensity)


def facility_energy(it_mw, utilization, pue, hours=8760):
    """Chapter 3: annual MWh under fixed utilization and PUE."""
    if it_mw < 0 or hours <= 0 or pue < 1:
        raise ValueError("invalid power, horizon or PUE")
    if not 0 <= utilization <= 1:
        raise ValueError("utilization must lie in [0, 1]")
    return it_mw * utilization * pue * hours


def posterior_positive(prior, sensitivity, false_positive):
    """Chapters 4, 6 and 9: precision of a binary selection rule."""
    if not all(0 <= p <= 1 for p in
               (prior, sensitivity, false_positive)):
        raise ValueError("probabilities must lie in [0, 1]")
    true_pass = prior * sensitivity
    pass_probability = true_pass + (1 - prior) * false_positive
    if pass_probability == 0:
        raise ValueError("conditioning event has zero probability")
    return true_pass / pass_probability


def delivered_tasks(capacity, availability, utilization, throughput, demand):
    """Chapter 5: bound assuming all feasible work is served."""
    if min(capacity, throughput, demand) < 0:
        raise ValueError("capacity, throughput and demand must be nonnegative")
    if not all(0 <= p <= 1 for p in (availability, utilization)):
        raise ValueError("availability and utilization must lie in [0, 1]")
    return min(capacity * availability * utilization * throughput, demand)


def workflow_success(stage_probability, stages):
    """Chapter 7: independent, identical, required stages without recovery."""
    if not 0 <= stage_probability <= 1:
        raise ValueError("probability must lie in [0, 1]")
    if not isinstance(stages, int) or stages < 0:
        raise ValueError("stage count must be a nonnegative integer")
    return stage_probability ** stages


def specialization_volume(fixed, frontier, specialized):
    if min(fixed, frontier, specialized) < 0:
        raise ValueError("costs must be nonnegative")
    if frontier <= specialized:
        raise ValueError("no positive per-request saving")
    return fixed / (frontier - specialized)


def mean_queue_time(arrivals, service):
    if not 0 <= arrivals < service:
        raise ValueError("require 0 <= arrivals < service")
    return 1 / (service - arrivals)


def annual_capital_charge(purchase, rate, years):
    if purchase < 0 or rate < 0 or years <= 0:
        raise ValueError("require nonnegative cost/rate and positive years")
    if rate == 0:
        return purchase / years
    return purchase * rate / (1 - (1 + rate) ** -years)


def ownership_utilization(fixed, rental, variable, hours=8760):
    if min(fixed, rental, variable) < 0 or hours <= 0:
        raise ValueError("invalid costs or horizon")
    if rental <= variable:
        raise ValueError("ownership has no operating-cost advantage")
    return fixed / (hours * (rental - variable))


def occupancy(free_ligand, dissociation):
    """Chapter 9: equilibrium occupancy; both concentrations share a unit."""
    if free_ligand < 0 or dissociation <= 0:
        raise ValueError("require nonnegative ligand and positive Kd")
    return free_ligand / (dissociation + free_ligand)


def program_value(value, probabilities, costs):
    """Chapter 9: undiscounted net value of a three-stage development path."""
    if len(probabilities) != 3 or len(costs) != 3:
        raise ValueError("this model requires exactly three stages")
    if value < 0 or any(cost < 0 for cost in costs):
        raise ValueError("values and costs must be nonnegative")
    if not all(0 <= prob <= 1 for prob in probabilities):
        raise ValueError("probabilities must lie in [0, 1]")
    p1, p2, p3 = probabilities
    c1, c2, c3 = costs
    return value * p1 * p2 * p3 - c1 - p1 * c2 - p1 * p2 * c3


def self_check():
    assert contribution(30, 3, .02, 250) == 22
    assert contribution(30, 3, .02, 2500) == -23
    assert roofline(100e12, 2e12, 10) == 20e12
    assert facility_energy(100, .8, 1.2) == 840960
    assert math.isclose(posterior_positive(.1, .8, .05), .64)
    assert math.isclose(posterior_positive(.2, .95, .1), 19 / 27)
    assert delivered_tasks(100, .9, .8, 2, 500) == 144
    assert delivered_tasks(100, .9, .8, 2, 50) == 50
    assert math.isclose(workflow_success(.99, 20), .81790694, abs_tol=1e-8)
    assert workflow_success(.5, 0) == 1
    assert math.isclose(occupancy(10, 1), 10 / 11)
    assert math.isclose(program_value(500, (.5, .4, .7), (2, 10, 40)), 55)
    assert math.isclose(program_value(500, (.7, .4, .7), (2, 10, 40)), 77.8)
    assert specialization_volume(120_000, 0.020, 0.005) == 8_000_000
    assert specialization_volume(84_000, 0.004, 0) == 21_000_000
    assert math.isclose(specialization_volume(84_000, .004, .001), 28e6)
    assert math.isclose(mean_queue_time(9.8, 10), 5)
    assert mean_queue_time(15, 20) == .2
    assert math.isclose(
        ownership_utilization(8000, 2.5, .5), .456621, rel_tol=1e-5)
    assert annual_capital_charge(100, 0, 5) == 20
    charge = annual_capital_charge(100, .1, 5)
    assert math.isclose(sum(charge / 1.1**t for t in range(1, 6)), 100)
    for args in [(10, 10), (11, 10), (-1, 10)]:
        try:
            mean_queue_time(*args)
        except ValueError:
            pass
        else:
            raise AssertionError("unstable or invalid queue was accepted")
    for action in [lambda: posterior_positive(.1, 0, 0),
                   lambda: occupancy(10, 0),
                   lambda: facility_energy(100, 1.1, 1.2),
                   lambda: workflow_success(.9, 2.5),
                   lambda: program_value(10, (.5, 1.2, .5), (1, 1, 1))]:
        try:
            action()
        except ValueError:
            pass
        else:
            raise AssertionError("invalid input was accepted")
    print("Economic model checks passed.")


if __name__ == '__main__':
    self_check()
