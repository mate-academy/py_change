"""
Changer by .badian
"""
from typing import Dict, Any, Union


def amounter(amount):
    """amount from str to int value or return int"""
    if isinstance(amount, str):
        flt_amount = int(float(amount.split()[0]) * 100)
        rnd_amount = flt_amount // 5 * 5
    else:
        rnd_amount = amount
    return int(rnd_amount)

def nominator(nominal):
    """uah to coin"""
    return nominal * 100 if nominal in (1, 2) else int(nominal)

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
        breaker = 0
        while breaker != 1:
            if odd == 0:
                money_dict[nominal] = flr_div
                return money_dict
            else:
                if flr_div == 0:
                    breaker = 1
                else:
                    money_dict[nominal] = flr_div
                    odd = nominator(nominal) * flr_div
                    amount = int(amounter(amount)) - odd
                    breaker = 1
    return money_dict
