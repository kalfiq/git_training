def subtract(arg1, arg2):
    return arg1 - arg2 if arg1 > arg2 else arg2 - arg1

def main():
    a = 2
    b = 5

    print(subtract(a, b))

if __name__ == "__main__":
    main()
