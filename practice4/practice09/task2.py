name = "Anton"
surname = "Romaniuk"
group = "IT-32"

number = int(input("Enter an integer: "))

if number == 0:
    print("Digits: 1")
    print("Sum of digits: 0")
    print("Max digit: 0, min digit: 0")
    print("Reversed: 0")

elif number < 0:
    print("Please enter a non-negative number.")

else:
    temp = number
    count = 0
    total = 0
    max_digit = 0
    min_digit = 9
    reversed_number = 0

    while temp > 0:
        digit = temp % 10
        temp //= 10

        count += 1
        total += digit

        if digit > max_digit:
            max_digit = digit

        if digit < min_digit:
            min_digit = digit

        reversed_number = reversed_number * 10 + digit

    print("Digits:", count)
    print("Sum of digits:", total)
    print("Max digit:", max_digit, ", min digit:", min_digit)
    print("Reversed:", reversed_number)