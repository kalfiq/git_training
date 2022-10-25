from addition import add
import subtraction
import multiplication
import division


def main():
    print("Output of some simple arithmetic operations")

    num1 = int(input("Please input the first number: "))
    num2 = int(input("Please input the second number: "))

    print("")
    print("What operation would you like to perform?")

    operation = int(input("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    """
    ))

    result = 0
    if (operation == 1):
        result = add(num1, num2)

    elif (operation == 2):
        result = subtract(num1, num2)

    elif (operation == 3):
        result = multiply(num1, num2)

    elif (operation == 4):
        result = divide(num1, num2)

    print("The result is: ", result)


if __name__ == "__main__":
    main()
