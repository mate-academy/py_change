"""
docstring
"""


def make_change(amount: str) -> dict:
    """

    :param amount:
    :return:
    """
    result = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}
    amount = amount.split()[0]
    if len(amount) == 1:
        return result
    hrn, kop = int(amount.split('.')[0]), int(amount.split('.')[1])
    kop = rounder(kop)
    return result_dict(hrn, kop, result)


def result_dict(hrn, kop, result):
    """

    :param hrn:
    :param kop:
    :param result:
    :return:
    """
    for i in result:
        if i in [1, 2]:
            result[2] = hrn // 2
            result[1] = (hrn - result[2] * 2) // 1
        else:
            if kop // i > 0:
                result[i] = kop // i
                kop -= i * (kop // i)
    return result


def rounder(kop):
    """

    :param kop:
    :return:
    """
    if str(kop)[-1] != '5':
        if int(str(kop)[-1]) < 5:
            kop = kop // 10 * 10
        elif int(str(kop)[-1]) > 5:
            kop = kop + 10 - kop % 10
        return kop
    return kop
