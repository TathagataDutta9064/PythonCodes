try:
    user_input=input("please enter an integer")
    integer_input=int(user_input)
    print("You entered the integer:", integer_input)
except ValueError:
    print("That's not a valid integer. Please try again.")
print("Remaining part")