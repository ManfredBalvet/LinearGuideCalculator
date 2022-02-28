import math
from classes import Shaft, ShaftComposite
from itertools import product
from collections import namedtuple

ShaftAndQty = namedtuple('ShaftAndQty', 'shaft, qty')


def config_for_length(target_length: int, shafts: list[Shaft]) -> str:

    closest_high = target_length
    closest_low = - target_length
    config_low = []
    config_high = []
    config_exact = []

    possible_configs = [range(math.ceil(target_length / shaft.length) + 1) for shaft in shafts]
    for quantities in product(*possible_configs):
        possible_length = 0
        for i in range(len(shafts)):
            possible_length += quantities[i] * shafts[i].length

        difference = possible_length - target_length

        if difference == 0:
            config_exact.append(ShaftComposite(shafts, quantities, difference))
            closest_low = difference
            closest_high = difference

        elif difference < 0:
            if closest_low < difference:
                closest_low = difference
                config_low = [ShaftComposite(shafts, quantities, difference)]
            elif difference == closest_low:
                config_low.append(ShaftComposite(shafts, quantities, difference))

        elif 0 < difference:
            if difference < closest_high:
                closest_high = difference
                config_high = [ShaftComposite(shafts, quantities, difference)]
            elif difference == closest_high:
                config_high.append(ShaftComposite(shafts, quantities, difference))

    nb_of_solutions = 5
    if len(config_exact) > 0:
        outputs = f"\nFor a {target_length}mm shaft your {min(len(config_exact), nb_of_solutions)} best configurations with an the exact length are:\n\n"
        for i, shaft_composite in enumerate(__rank(config_exact)):
            if i == nb_of_solutions:
                break
            outputs += __generate_output(shaft_composite) + f"made of {shaft_composite.nb_of_segments} segments " \
                                                            f"for a total of ${shaft_composite.price:.2f}USD\n"

    else:
        outputs = f"\nYour {min(len(config_low), nb_of_solutions)} best configurations for a {target_length + config_low[0].difference}mm shaft " \
                  f"(shorter by {-config_low[0].difference}mm) are:\n\n"
        for i, shaft_composite in enumerate(__rank(config_low)):
            if i == 5:
                break
            outputs += __generate_output(shaft_composite) + f"made of {shaft_composite.nb_of_segments} segments for a total of ${shaft_composite.price:.2f}USD\n"

        outputs += f"\nYour {min(len(config_high), nb_of_solutions)} best configurations for a {target_length + config_high[0].difference}mm shaft " \
                   f"(longer by {config_high[0].difference}mm) are:\n\n"
        for i, shaft_composite in enumerate(__rank(config_high)):
            if i == 5:
                break
            outputs += __generate_output(shaft_composite) + f"made of {shaft_composite.nb_of_segments} segments for a total of ${shaft_composite.price:.2f}USD\n"

    return outputs


def __rank(shaft_composites: list[ShaftComposite]) -> list[ShaftComposite]:
    ranked_shaft_composites = sorted(shaft_composites,
                                     key=lambda shaft_composite: (shaft_composite.nb_of_segments, shaft_composite.price, -shaft_composite.quantities[0]))

    return ranked_shaft_composites


def __generate_output(shaft_composite: ShaftComposite) -> str:
    output = ""
    for i, quantity in enumerate(shaft_composite.quantities):
        if quantity > 0:
            output += f"{quantity}x {shaft_composite.shafts[i].name}, "

    return output
