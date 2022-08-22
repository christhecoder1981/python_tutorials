def add(a, b, c):
    d = a +b + c
    return d

#print(add(3, 7, 9, 8, 9))

def add_all(name, *args):
    total = 0
    for i in args:
        total += i
    return name, total

print(add_all("chris", 1,2,3,4,5,6,7,8,9,10))

