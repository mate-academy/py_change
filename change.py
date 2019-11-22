"""docstring"""


def make_change(amount):
    """ docstring"""
    change_to_be_given = {}
    if "." not in amount:
        new_amount = [amount.strip(" UAH"), "00"]
    else:
        new_amount = amount.strip(" UAH").split(".")
    change_to_be_given[2] = int(new_amount[0]) // 2
    change_to_be_given[1] = int(new_amount[0]) - int(new_amount[0]) // 2 * 2
    kopiyky = int(new_amount[1])
    # arithmetic rounding is solved by check if the amount is closer
    # to tens (even multiple of 5) or
    # to tens plus five (odd multiples of 5)
    if kopiyky % 5 == 0 or kopiyky // 5 % 2 == 0:
        change_kopiyky_init = kopiyky // 5 * 5
    else:
        change_kopiyky_init = (kopiyky // 5 + 1) * 5
    kop_nominals = [50, 25, 10, 5]
    for nominal in kop_nominals:
        change_to_be_given[nominal] = change_kopiyky_init // nominal
        change_kopiyky_init = change_kopiyky_init % nominal

    return change_to_be_given
