# for i in range(1, 21):
    # print(i)

# a = 1
# while a <= 20:
#     print(a)
#     a += 2


# a = 0 
# while a < 10:
#     a += 1
#     val = a * a
#     print(val)

# i = 1
# while i <= 10:
#     print(i**2)
#     i += 1


# for i in range(1, 11):
#     print(i**2)

# for i in range(1, 11):
#     print(i*17)

# for i in range(17,171,17):
#     print(i)

# def num(a, b, c):
#     if a >= b and a>= c:
#         print("a")
#     elif b >= a and b>= c:
#         print("b")
#     else:
#         print("c")
    
# num(19,19,19)

# def func(l1):
#     l2 = []
#     for i in l1:
#         l2.append(i.upper())
#     print(l2)

# func(["hi", "everybody"])

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# input1 = input("Insert a word: ") # chris
# for i in input1:
#     ind = alphabet.index(i)
#     print(f"{i}: {ind}") 
"""
c: 2
h: 7
r: 
i: 
s: 

21,34,2,12,alan,mark,bob,emma
"""

l1 = input(" insert 4 nums and 4 words: ").split(",")

numbers = l1[0:4]
l3 = []
for i in numbers:
    i = int(i)
    l3.append(i)

l3.sort()
print(l3)

words = l1[4:]
words.sort()

print(words)