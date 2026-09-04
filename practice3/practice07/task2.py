print("Romaniuk Anton, IT-32")

number = int(input("Enter an integer: "))

if number > 0:
    print("The number is positive")
elif number < 0:
    print("The number is negative")
else:
    print("The number is zero")

if number != 0:
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

if -9 <= number <= 9:
    print("The number is one-digit")
else:
    print("The number is not one-digit")