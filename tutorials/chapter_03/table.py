def table(a):
    for i in range(1,11):
        sum = a*i
        print(f"{a} x {i} = {sum} ")

number = int(input("Insert a number: "))
table(number)