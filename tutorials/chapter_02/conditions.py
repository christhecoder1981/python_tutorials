age = int(input("Insert your age: "))

if age >= 117 or age < 1:
    print("Its not true!")
elif age < 18:
    print("You are not eligible for voting!")

else:
    print("You are eligible for voting!")