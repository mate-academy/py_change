""" Money counter """

def make_change(amount: str) -> dict:
    """ Money counter func """
    change = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}

    if amount.split()[0] != '0':
        all_sum = int(amount.split()[0].split('.')[0]
                      + amount.split()[0].split('.')[1])

        change[2] = all_sum // 200
        all_sum -= change[2] * 200

        change[1] = all_sum // 100
        all_sum -= change[1] * 100

        if all_sum % 5 != 0 and all_sum % 10 > 5:
            all_sum += 10 - all_sum % 10

        change[50] = all_sum // 50
        all_sum -= change[50] * 50

        change[25] = all_sum // 25
        all_sum -= change[25] * 25

        change[10] = all_sum // 10
        all_sum -= change[10] * 10

        change[5] = all_sum // 5
        all_sum -= change[5] * 5

    return change
