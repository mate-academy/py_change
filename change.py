"""docstring"""

def make_change(amount):
    """ docstring"""
    change_to_be_given = {}
    new_amount = round(float(amount.strip(" UAH")), 2)
    change_to_be_given[2] = int(new_amount // 2)
    change_to_be_given[1] = int(new_amount - new_amount // 2 * 2)
    kopiyky = int(new_amount % 1 * 100)
    # arithmetic rounding is solved by check if the amount is closer
    # to tens (even multiple of 5) or
    # to tens plus five (odd multiples of 5)
    if kopiyky % 5 == 0 or kopiyky // 5 % 2 == 0:
        change_kopiyky_init = kopiyky // 5 * 5
    else:
        change_kopiyky_init = (kopiyky // 5 + 1) * 5
    print(change_kopiyky_init)
    change_to_be_given[50] = change_kopiyky_init // 50
    change_to_be_given[25] = (change_kopiyky_init % 50) // 25
    change_to_be_given[10] = ((change_kopiyky_init % 50) % 25) // 10
    change_to_be_given[5] = (((change_kopiyky_init % 50) % 25) % 10) // 5
    print(change_to_be_given)
    return change_to_be_given
