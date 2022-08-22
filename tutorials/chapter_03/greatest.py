def greatest(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    elif b > a and b > c and b > d:
        return b
    elif c > a and c > b and c > d:
        return c
    else:
        return d
    
print(greatest(6, 9, 122, 1))
