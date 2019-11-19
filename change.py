'''Module'''


def make_change(amount: str) -> dict:
    '''
    :param amount:
    :return:
    '''
    answer = {1: 0, 2: 0, 50: 0, 25: 0, 10: 0, 5: 0}
    money = amount.split(' ')[0]
    try:
        uah, kopecks = int(money.split('.')[0]), int(money.split('.')[1])
    except IndexError:
        uah, kopecks = int(money), 0

    if kopecks % 5 != 0:
        if kopecks % 10 > 5:
            kopecks += 10 - (kopecks % 10)
        else:
            kopecks -= kopecks % 10

    answer[2] = uah // 2
    answer[1] = uah % 2
    answer[50] = kopecks // 50
    answer[25] = (kopecks % 50) // 25
    answer[10] = ((kopecks % 50) % 25) // 10
    answer[5] = (((kopecks % 50) % 25) % 10) // 5

    return answer
