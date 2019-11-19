"""Containing function make_change"""


def gen_dict(denomination: list, num_coins: list):
    """Generates a dict given two lists as an arguments"""
    res = {}
    for idx, nominal in enumerate(denomination):
        res[nominal] = num_coins[idx]
    return res


def make_change(amount: str) -> dict:
    """
    Returns dict that contains change of
    given amount of money using minimum coins.
    """
    denomin = [200, 100, 50, 25, 10, 5]
    num_coins = [0 for nominal in range(len(denomin))]
    money = float(amount[:amount.index(' ')])

    if str(money)[-1] != '5':
        money = round(money, 1)
    money *= 100

    coin_idx = 0
    for coin in denomin:
        while money / coin >= 1:
            num_coins[coin_idx] += 1
            money = round(money - coin, 2)
        coin_idx += 1

    denomin[0], denomin[1] = 1, 2
    num_coins[0], num_coins[1] = num_coins[1], num_coins[0]

    return gen_dict(denomin, num_coins)
