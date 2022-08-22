# List Comprehension - NO LOGIC ONLY SYNTAX-BASED

print([i for i in range(1,101)])

# -1, -10

list1 = []
for i in range(1,11):
    list1.append(-i)

print(list1)
print([-i for i in range(1, 11)])

list2 =[]
for i in range(1, 11):
    list2.append(i)

list3 = []
for i in range(1, 11):
    if i % 2 ==0:
        square = i * i
        list3.append(square)
    else:
        list3.append(-i)
print(list3)

print([i*i if i%2 == 0 else -i for i in range(1,11)])

print([i**3 for i in range(1,11) if i%2 != 0])


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
