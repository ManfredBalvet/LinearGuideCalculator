def config_for_length(length: int):
    mo_lm_014_0585 = 585
    mo_lm_014_0855 = 855
    mo_lm_014_1530 = 1530
    mo_lm_014_2295 = 2295
    mo_lm_014_0585_price = 232.54
    mo_lm_014_0855_price = 292.66
    mo_lm_014_1530_price = 357.68
    mo_lm_014_2295_price = 539.12

    closest_high = length
    closest_low = - length
    config_low = []
    config_high = []
    config_exact = []

    for w in range(length // mo_lm_014_2295 + 2):
        for x in range(length // mo_lm_014_1530 + 2):
            for y in range(length // mo_lm_014_0855 + 2):
                for z in range(length // mo_lm_014_0585 + 2):
                    possible_length = mo_lm_014_2295 * w + mo_lm_014_1530 * x + mo_lm_014_0855 * y + mo_lm_014_0585 * z
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

    print(f"For a length of {length}mm :")
    if len(config_exact) == 0:
        if closest_high > abs(closest_low):
            for [w, x, y, z] in config_low:
                price = w * mo_lm_014_2295_price + x * mo_lm_014_1530_price + y * mo_lm_014_0855_price + z * mo_lm_014_0585_price
                segments = w + x + y + z
                print(f"{w}x MO-LM-014-2295, {x}x MO-LM-014-1530, {y}x MO-LM-014-0855, {z}x MO-LM-014-585 will be too short by {abs(closest_low)} for {segments} segments at {price}$")
        elif abs(closest_low) > closest_high:
            for [w, x, y, z] in config_high:
                price = w * mo_lm_014_2295_price + x * mo_lm_014_1530_price + y * mo_lm_014_0855_price + z * mo_lm_014_0585_price
                segments = w + x + y + z
                print(f"{w}x MO-LM-014-2295, {x}x MO-LM-014-1530, {y}x MO-LM-014-0855, {z}x MO-LM-014-585 will be too long by {abs(closest_high)} for {segments} segments at {price}$")
        else:
            for [w, x, y, z] in config_low:
                price = w * mo_lm_014_2295_price + x * mo_lm_014_1530_price + y * mo_lm_014_0855_price + z * mo_lm_014_0585_price
                segments = w + x + y + z
                print(f"{w}x MO-LM-014-2295, {x}x MO-LM-014-1530, {y}x MO-LM-014-0855, {z}x MO-LM-014-585 will be too short by {abs(closest_low)} for {segments} segments at {price}$")
            for [w, x, y, z] in config_high:
                price = w * mo_lm_014_2295_price + x * mo_lm_014_1530_price + y * mo_lm_014_0855_price + z * mo_lm_014_0585_price
                segments = w + x + y + z
                print(f"{w}x MO-LM-014-2295, {x}x MO-LM-014-1530, {y}x MO-LM-014-0855, {z}x MO-LM-014-585 will be too long by {abs(closest_high)} for {segments} segments at {price}$")
    else:
        for [w, x, y, z] in config_exact:
            price = w * mo_lm_014_2295_price + x * mo_lm_014_1530_price + y * mo_lm_014_0855_price + z * mo_lm_014_0585_price
            segments = w + x + y + z
            print(f"{w}x MO-LM-014-2295, {x}x MO-LM-014-1530, {y}x MO-LM-014-0855, {z}x MO-LM-014-585 will work for {segments} segments at {price}$")

