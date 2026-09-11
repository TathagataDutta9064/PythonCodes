a=int(input("enter the numerator"))
b=int(input("enter the dinominator"))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("denominator cannot be zero")
except TypeError:
    print("invalid input type")
print("hallow world")
print("other code camn be written here")