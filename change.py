"""Make change task"""


def make_change(amount: str) -> dict:
    """General function"""
    my_sum = float(amount[:-4])
    grivna_nominal = [2, 1]
    kop_nominal = [50, 25, 10, 5]
    denom = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}

    if (my_sum * 100) % 5 != 0:
        formated_sum = format(round(my_sum, 1), '.2f')
    else:
        formated_sum = format(my_sum, '.2f')
    grivnas = int(formated_sum.split('.')[0])
    kop = int(formated_sum.split('.')[1])

    for i in grivna_nominal:
        denom[i] = grivnas // i
        grivnas -= (i * denom[i])
        if grivnas <= 0:
            break

    for i in kop_nominal:
        denom[i] = kop // i
        kop -= (i * denom[i])
        if kop <= 0:
            break
    return denom
