
def config_for_length(length: int) -> str:
    mo_lm_014 = [
        (2295, 539.12),
        (1530, 357.68),
        (855, 292.66),
        (585, 232.54)
    ]

    closest_high = length
    closest_low = - length
    config_low = []
    config_high = []
    config_exact = []

    for w in range(length // mo_lm_014[0][0] + 2):
        for x in range(length // mo_lm_014[1][0] + 2):
            for y in range(length // mo_lm_014[2][0] + 2):
                for z in range(length // mo_lm_014[3][0] + 2):
                    possible_length = mo_lm_014[0][0] * w + mo_lm_014[1][0] * x + mo_lm_014[2][0] * y + mo_lm_014[3][0] * z
                    difference = possible_length - length

                    if difference == 0:
                        config_exact.append([w, x, y, z])
                        closest_low = difference
                        closest_high = difference

                    elif difference < 0:
                        if closest_low < difference:
                            closest_low = difference
                            config_low = [[w, x, y, z]]

                        elif closest_low == difference:
                            config_low.append([w, x, y, z])

                    elif difference > 0:
                        if closest_high > difference:
                            closest_high = difference
                            config_high = [[w, x, y, z]]

                        elif closest_high == difference:
                            config_high.append([w, x, y, z])

    output = ""

    if len(config_exact) == 0:
        for [w, x, y, z] in config_low:
            price = __get_price([w, x, y, z], mo_lm_014)
            segments = w + x + y + z
            for i, segment in enumerate([w, x, y, z]):
                if segment > 0:
                    output += f"{segment}x MO-LM-014-{mo_lm_014[i][0]}, "
            output += f"will be too short by {abs(closest_low)} for {segments} segments at {price}$\n"

        for [w, x, y, z] in config_high:
            price = __get_price([w, x, y, z], mo_lm_014)
            segments = w + x + y + z
            for i, segment in enumerate([w, x, y, z]):
                if segment > 0:
                    output += f"{segment}x MO-LM-014-{mo_lm_014[i][0]}, "
            output += f"will be too long by {abs(closest_high)} for {segments} segments at {price}$\n"

    else:
        for [w, x, y, z] in config_exact:
            price = __get_price([w, x, y, z], mo_lm_014)
            segments = w + x + y + z
            for i, segment in enumerate([w, x, y, z]):
                if segment > 0:
                    output += f"{segment}x MO-LM-014-{mo_lm_014[i][0]}, "
            output += f"will work for {segments} segments at {price}$\n"

    return output


def __get_price(config: list[int], mo_lm_014: list[tuple[int, float]]) -> int:
    price = 0
    for i, segments in enumerate(config):
        price += segments * mo_lm_014[i][1]

    return price
