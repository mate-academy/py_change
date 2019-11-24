"""
Changer by .badian
"""
from typing import Dict, Any, Union


def amounter(amount):
    """amount from str to int value or return int"""
    if isinstance(amount, str):
        flt_amount = int(float(amount.split()[0]) * 100)
        rnd_amount = flt_amount // 5 * 5
        return int(rnd_amount)
    else:
        return amount

def nominator(nominal):
    """uah to coin"""
    if nominal == 1 or nominal == 2:
        return nominal * 100

    else:
        return int(nominal)


def make_change(amount) -> dict:
    """make change in:str out:dict"""
    money_dict: Dict[int, Union[int, Any]] = {
        1: 0,
        2: 0,
        50: 0,
        25: 0,
        10: 0,
        5: 0
    }
    clr_div = amounter(amount) / 200
    flr_div = amounter(amount) // 200
    odd = int(clr_div * 100) - int(flr_div * 100)
    for nominal in [2, 1, 50, 25, 10, 5]:
        flr_div = amounter(amount) // nominator(nominal)
        exit = 0
        while exit != 1:
            if odd == 0:
                money_dict[nominal] = flr_div
                return money_dict
            else:
                if flr_div == 0:
                    exit = 1
                else:
                    money_dict[nominal] = flr_div
                    odd = nominator(nominal) * flr_div
                    amount = int(amounter(amount)) - odd
                    exit = 1
    return money_dict
