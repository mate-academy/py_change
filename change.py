"""
module docstring
"""
import math


def make_change(amount: str) -> dict:
    """
    Returns a way to change a given amount with a minimum number of coins.
    :param amount: str
    :return: dict
    """
    money_change = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}
    nominals = [200, 100, 50, 25, 10, 5]

    money_value = float(amount.strip(" UAH"))
    kopecks = math.floor(money_value * 100)
    if kopecks % 5 != 0:
        if kopecks % 10 >= 5:
            kopecks += 10 - kopecks % 10
        else:
            kopecks -= kopecks % 10

    for nominal in nominals:
        if nominal >= 100:
            money_change[int(nominal / 100)] = kopecks // nominal
            kopecks = kopecks % nominal
        else:
            money_change[nominal] = kopecks // nominal
            kopecks = kopecks % nominal

    return money_change
