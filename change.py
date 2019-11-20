"""money change module."""

MONEY_DENOMINATION = [200, 100, 50, 25, 10, 5]


def string_normalizer(string_with_currency: str) -> int:
    """function removes currency name from input string."""

    last_4_characters = -4
    norm_number = float(string_with_currency[:last_4_characters])
    if (norm_number * 100) % 5 != 0:
        norm_number = float(format(round(norm_number, 1), '.2f'))*100
    else:
        norm_number = float(format(norm_number, '.2f'))*100
    return int(norm_number)


def get_number_of_coins(amount: str) -> dict:
    """get the way of change coins"""

    result_template_dict = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}
    normalized_amount = string_normalizer(amount)
    for nominal in MONEY_DENOMINATION:
        result = normalized_amount // nominal
        if nominal % 100 == 0:
            result_template_dict[int(nominal/100)] = result
        else:
            result_template_dict[nominal] = result
        normalized_amount = normalized_amount - result * nominal
    return result_template_dict


def make_change(amount: str) -> dict:
    """make exchange of kopecks"""

    if not amount:
        return {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}
    return get_number_of_coins(amount)
