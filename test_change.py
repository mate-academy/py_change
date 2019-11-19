'''Module'''
import change


def test_0():
    '''Test0'''
    assert change.make_change("0 UAH") == {1: 0, 2: 0,
                                           50: 0, 25: 0, 10: 0, 5: 0}


def test_014():
    '''Test2'''
    assert change.make_change("0.14 UAH") == {1: 0, 2: 0,
                                              50: 0, 25: 0, 10: 1, 5: 0}


def test_123():
    '''Test3'''
    assert change.make_change("1.23 UAH") == {1: 1, 2: 0,
                                              50: 0, 25: 0, 10: 2, 5: 0}


def test_15346():
    '''Test4'''
    assert change.make_change("153.46 UAH") == {1: 1, 2: 76,
                                                50: 1, 25: 0, 10: 0, 5: 0}


def test_385():
    '''Test5'''
    assert change.make_change("3.85 UAH") == {1: 1, 2: 1,
                                              50: 1, 25: 1, 10: 1, 5: 0}


def test_005():
    '''Test6'''
    assert change.make_change("0.05 UAH") == {1: 0, 2: 0,
                                              50: 0, 25: 0, 10: 0, 5: 1}
