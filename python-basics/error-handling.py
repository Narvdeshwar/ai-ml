try:
    x=int(input("Enter the number = "))
    ans=10/x
except ZeroDivisionError:
    print("Can't divide by zero")
except ValueError:
    print("Invalid input value..")
else:
    print(f"Divison Successful {ans}")
finally:
    print("End of file")

