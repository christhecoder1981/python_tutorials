num = int(input("How many numbers do you want? ")) # 5
# 0 1 1 2 3
a = 0
b = 1
if num == 1:
    print(a)
elif num == 2:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for _ in range(num-2):
        c = a + b # 1 2 3
        a = b # 1 1 2
        b = c # 1 2 3
        print(c) # 1 2 3

