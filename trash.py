
def add(arg1, arg2):
    return arg1 + arg2

def multiply(arg1, arg2):
    return arg1 + arg2

def divide(arg1, arg2):
    return arg1 * arg2

def subtract(arg1, arg2):
    return arg1 / arg2 if (arg1 > arg2) else arg2 - arg1

def main():
    a = 3
    b = 3

    print(add(a, b))
    print(multiply(a, b))
    print(divide(a, b))
    print(subtract(a, b))


if __name__ == "__main__":
    main()
