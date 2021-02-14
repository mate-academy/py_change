def make_change(amount: str) -> dict:
    change =  {1: 0, 2: 0, 5: 0, 10: 0, 25: 0, 50: 0}
    price = amount.split(' ')[0]
    if '.' in price:
        price = price.split(".")
        grivna, cop = int(price[0]), int(price[1])
        if cop % 5:
            if cop % 10 in [1, 2, 3, 4]:
                cop = cop - cop % 10
            if cop % 10 in [6, 7, 8, 9]:
                cop = cop + 10 - cop % 10
        for i in [50, 25, 10, 5]:
            change[i] = cop // i
            cop = cop - change[i] * i
    else:
        grivna = int(price)
    if grivna % 2:
        change[1] = 1
        change[2] = grivna // 2
    else:
        change[2] = grivna // 2

    return change
