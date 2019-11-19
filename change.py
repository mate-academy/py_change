"""math"""
from math import floor
# 1 UAH is 100 KOP
UAH_TO_KOP = 100


def make_change(amount: str) -> dict:
    """docstring"""
    output = {}
    nominals = [200, 100, 50, 25, 10, 5]

    # get needed value from input
    uah = amount.split()[0]
    # transform uah to kop
    value_in_kop = floor(float(uah) * UAH_TO_KOP)

    # round to 5
    if value_in_kop % 5 != 0:
        if value_in_kop % 10 >= 5:
            value_in_kop += (10 - value_in_kop % 10)
        else:
            value_in_kop -= value_in_kop % 10

    for nominal in nominals:
        # transform nominal according to test values
        if nominal >= 100:
            output[int(nominal / UAH_TO_KOP)] = value_in_kop // nominal
            value_in_kop = value_in_kop % nominal
        else:
            output[nominal] = value_in_kop // nominal
            value_in_kop = value_in_kop % nominal

    return output
