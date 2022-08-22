#kwargs -> keyword arguments

def func(**kwargs):
    for key in kwargs:
        print(f"{key}: {kwargs[key]}")

func(a=1, b=2, name="kaustubh")