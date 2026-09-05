try:
    first_number = int(input("Enter the first number: "))
    second_number = int(input("Enter the second number: "))
    division= first_number / second_number
    print("From division the output is =",division)
except ZeroDivisionError:
    print('cannot divide by zero')