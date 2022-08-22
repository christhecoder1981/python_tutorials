"""
Welcome to Chris's Coffee Shop!
You need to login to get started.

Insert your username: chris
Insert your email: chris@larroum.com
Insert your password: 12345
Hey! You are logged in! And now you can order a coffee!

OR

Invalid Credentials
"""

print("Welcome to Chris's Coffee Shop! \nYou need to login to get started. ")
for attempt in range(3):
    username = input("Insert your username: ")
    mail = input("Insert your email: ")
    password = input("Insert your password: ")
    if username == "chris" and mail == "chris@larroum.com" and password == "12345":
        print("Hey! You are logged in! And now you can order a coffee!")
        break
    else:
        print("Invalid Credentials")
        print("Try again....")
        continue