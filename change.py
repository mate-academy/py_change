"""
module docstring
"""


def make_change(amount: str) -> dict:
    """
    Returns a way to change a given amount with a minimum number of coins.
    :param amount:
    :return:
    """
    money_change = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}

    money_value = float(amount.strip(" UAH"))
    hryvnia, kopecks = divmod(money_value, 1)
    hryvnia = int(hryvnia)
    kopecks = int(kopecks * 100)

    if kopecks % 5 != 0:
        if kopecks % 10 >= 5:
            kopecks += 10 - kopecks % 10
        else:
            kopecks -= kopecks % 10

    money_change[1] = hryvnia % 2
    money_change[2] = hryvnia // 2
    money_change[50] = kopecks // 50
    money_change[25] = (kopecks % 50) // 25
    money_change[10] = ((kopecks % 50) % 25) // 10
    money_change[5] = (((kopecks % 50) % 25) % 10) // 5

    return money_change
