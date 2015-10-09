# Python switching methods

def f(x):
    return {
        'a': 1,
        'b': 2,
    }[x]


def f(x):
    return {
        'a': 1,
        'b': 2,
    }.get(x, 9)    # 9 is default if x not found