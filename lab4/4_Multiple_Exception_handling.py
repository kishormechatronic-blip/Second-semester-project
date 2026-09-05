try:
    number=int(input("Enter a number :"))
    index=int(input("Enter a index :"))
    numbers=[10,20,30]
    division=100/number
    print("The divided output: ",division)
    print("The index value :",numbers[index])
except ZeroDivisionError:
    print("cannot divide by zero")

except ValueError:
    print("invalid input")

except IndexError:
    print("index out of range")
    