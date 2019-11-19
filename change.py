""" Money counter """

def make_change(amount: str) -> dict:
    """ Money counter func """
    change = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}
    nomins = [200, 100, 50, 25, 10, 5]
    all_sum = int(amount[:-4].replace('.', ''))

    if all_sum < 5:
        return change

    if all_sum % 5 != 0:
        str_sum = str(all_sum)
        if int(str_sum[-1]) < 5:
            all_sum = (int(str_sum[:-1])) * 10
        else:
            all_sum = (int(str_sum[:-1]) + 1) * 10

    for nom in nomins:
        if nom >= 100:
            change[int(nom/100)] = all_sum // nom
            all_sum -= change[int(nom/100)] * nom
        else:
            change[nom] = all_sum // nom
            all_sum -= change[nom] * nom

    return change
