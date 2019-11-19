"""Containing function make_change"""
def make_change(amount: str) -> dict:
    """
    Returns dict that contains change of
    given amount of money using minimum coins.
    """
    denominations = [2, 1, 0.5, 0.25, 0.1, 0.05]
    money = float(amount[:amount.index(' ')])
    change = {1: 0, 2: 0, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0}
    change_res = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}

    repl = [(1, 1), (2, 2), (0.5, 50), (0.25, 25), (0.1, 10), (0.05, 5)]

    if str(money)[-1] != '5':
        money = round(money, 1)

    for coin in denominations:
        while money / coin >= 1:
            change[coin] += 1
            money = round(money - coin, 2)

    for begin, end in repl:
        change_res[end] = change[begin]
    return change_res
