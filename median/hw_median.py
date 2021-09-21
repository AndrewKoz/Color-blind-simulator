def improved_median(a, b, c):
    if a > c:
        a, c = c, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return b


def median(a, b, c):
    if a <= b:
        if b <= c:
            return b
        elif a < c:
            return c
        return a
    else:
        if a <= c:
            return a
        elif b < c:
            return c
        return b

