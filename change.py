"""change money"""


def make_change(amount: str) -> dict:
    """make my money"""
    out = {}
    pen = [2, 1, 50, 25, 10, 5]
    money = int(amount.split()[0].replace(".", ""))

    if money % 5 != 0:
        if money % 10 > 5:
            money = money + (10 - money % 10)
        else:
            money = money - money % 10

    ost = money
    for i in pen:
        grn = i
        if ost >= 0:
            if i < 5:
                grn = i * 100
            out[i] = ost // grn
            ost = ost - grn * out[i]

    return out
