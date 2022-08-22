"""
How many numbers you want to insert in the list: 4
Insert number 1: 4
Insert number 2: 2
Insert number 3: 6
Insert number 4: 1
Here's your list [4,2,6,1]
"""
num_list = []
num = int(input("How many numbers you want to insert in the list:"))
for i in range(1, num + 1):
    ins = int(input(f"Insert the number {i}: "))
    num_list.append(ins)
print(num_list)
