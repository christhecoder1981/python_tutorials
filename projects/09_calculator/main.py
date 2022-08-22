def add(num1, num2):
    result = num1 + num2
    return result

def sub(num1, num2):
    result = num1 - num2
    return result

def mul(num1, num2):
    result = num1 * num2
    return result

def div(num1, num2):
    result = num1 / num2
    return result
dict = {"+": add, "-": sub, "*": mul, "/": div}

def calc():
        completed = False

        num1 = float(input("Whats the first number? "))
        while not completed:
            op = input("Choose operation +, -, *, /: ")
            num2 = float(input("Whats the next number? "))
            calc_func = dict[op]
            answer = calc_func(num1, num2)
            print(f"{num1} {op} {num2} = {answer} ")

            y_n = input("woud you like to continue with your calculations, press y, or start from beginning, press n")
            if y_n == "y":
                num1 = answer
            else:
                completed = True
                calc()

            
calc()

        





