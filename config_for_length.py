import math
from shaft import Shaft
from itertools import product
from collections import namedtuple


ShaftOrder = namedtuple('ShaftOrder', 'quantity, shaft')


def config_for_length(target_length: int, shafts: list[Shaft]) -> list[str]:

    closest_high = target_length
    closest_low = - target_length
    config_low = []
    config_high = []
    config_exact = []

    possible_configs = [range(math.ceil(target_length / shaft.length) + 1) for shaft in shafts]
    for possible_config in product(*possible_configs):
        print(possible_config)
        possible_length = 0
        for i in range(len(shafts)):
            possible_length += possible_config[i] * shafts[i].length

        difference = possible_length - target_length

        if difference == 0:
            config_exact.append(possible_config)
            closest_low = difference
            closest_high = difference

        elif difference < 0:
            if closest_low < difference:
                closest_low = difference
                config_low = [possible_config]
            elif difference == closest_low:
                config_low.append(possible_config)

        elif 0 < difference:
            if difference < closest_high:
                closest_high = difference
                config_high = [possible_config]
            elif difference == closest_high:
                config_high.append(possible_config)

    # if len(config_exact) > 0:
    #     config_price = []
    #     config_segment = []
    #     for config in config_exact:
    #         config_price.append(__get_price(config, price_list))
    #         config_segment.append(sum(config))
    #     price_rank = [0] * len(config_price)
    #     segment_rank = [0] * len(config_segment)
    #     for rank in

    outputs = []
    if len(config_exact) == 0:
        for config in config_low:
            price = __get_price(config, shafts)
            segments = sum(config)
            output = ""
            for i, segment in enumerate(config):
                if segment > 0:
                    output += f"{segment}x {shafts[i].name}, "
            output += f"will make a shaft too short by {abs(closest_low)}mm with {segments} segments for a total of ${price:.2f}USD\n"
            outputs.append(output)

        for config in config_high:
            price = __get_price(config, shafts)
            segments = sum(config)
            output = ""
            for i, segment in enumerate(config):
                if segment > 0:
                    output += f"{segment}x {shafts[i].name}, "
            output += f"will make a shaft long by {abs(closest_high)}mm with {segments} segments for a total of ${price:.2f}USD\n"
            outputs.append(output)

    else:
        for config in config_exact:
            price = __get_price(config, shafts)
            segments = sum(config)
            output = ""
            for i, segment in enumerate(config):
                if segment > 0:
                    output += f"{segment}x {shafts[i].name}, "
            output += f"will work with {segments} segments for a total of ${price:.2f}USD\n"
            outputs.append(output)
    print(outputs)

    return outputs


def __get_price(config: list[int], shafts: list[Shaft]) -> float:
    price = 0
    for i, segments in enumerate(config):
        price += segments * shafts[i].price

    return price
