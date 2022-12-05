import subtraction
import multiplication
import division
import addition


def main():
    print("Output of some simple arithmetic operations")

    num1 = int(input("Please input the first number: "))
    num2 = int(input("Please input the second number: "))
    print("Line 1")

    print("")
    print("What operation would you like to perform?")

    operation = int(input("""
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    """
    ))

    print("Added another line")

    result = 0
    if (operation == 1):
        result = addition.add(num1, num2)

    elif (operation == 2):
        result = subtraction.subtract(num1, num2)

    elif (operation == 3):
        result = multiplcation.multiply(num1, num2)

    elif (operation == 4):
        result = division.divide(num1, num2)

    print("The result is: ", result)


if __name__ == "__main__":
    main()
