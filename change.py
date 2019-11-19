"""docstring"""

def make_change(amount: str) -> dict:
    """function that returns a way to change a given amount with a minimum number of coins"""
    change_result = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}
    amount = amount.split(' ')[0]
    if amount != '0':
        hryvnia, kopiika = int(amount.split('.')[0]), int(amount.split('.')[1])
        if str(kopiika)[-1] != '5':
            kopiika = int(round(kopiika/100, 1) * 100)
        if hryvnia > 0:
            change_result[2] = hryvnia // 2
            change_result[1] = hryvnia % 2
        if kopiika > 0:
            change_result[50] = kopiika // 50
            change_result[25] = kopiika % 50 // 25
            change_result[10] = kopiika % 50 % 25 // 10
            change_result[5] = kopiika % 50 % 25 % 10 // 5
    return change_result