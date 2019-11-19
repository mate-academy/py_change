"""Money change counter"""
def make_change(amount: str) -> dict:
    """Money change counter func"""
    result = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}
    nominals = [200, 100, 50, 25, 10, 5]

    uah = "".join(amount[:-4].split("."))
    if int(uah) < 5:
        return result
    if uah[-1] == "5":
        uah_int = int(uah)
    elif int(uah[-1]) < 5:
        uah_int = (int(uah[:-1]))*10
    else:
        uah_int = (int(uah[:-1]) + 1)*10

    for i in nominals:
        if uah_int // i:
            if i < 100:
                result[i] += uah_int // i
            else:
                result[int(i/100)] += uah_int // i
            uah_int -= (uah_int // i) * i

    return result
