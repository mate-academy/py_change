from math import floor


def make_change(amount: str) -> dict:

    # get needed value from input
    amount1 = amount.split()
    amount2 = amount1[0]
    # transform gr to kop
    amount3 = float(amount2)
    amount4 = floor(amount3 * 100)
    # round to 5
    if amount4 % 5 != 0:
        if amount4 % 10 >= 5:
            amount4 += (10 - amount4 % 10)
        else:
            amount4 -= amount4 % 10

    # dict to store result
    output = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}

    # calculate number of coins
    output[2] = amount4 // 200
    output[1] = (amount4 % 200) // 100
    output[50] = ((amount4 % 200) % 100) // 50
    output[25] = (((amount4 % 200) % 100) % 50) // 25
    output[10] = ((((amount4 % 200) % 100) % 50) % 25) // 10
    output[5] = (((((amount4 % 200) % 100) % 50) % 25) % 10) // 5

    return output
