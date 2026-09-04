name = "Anton"
surname = "Romaniuk"
group = "IT-32"

attempts = 0

while True:
    score = int(input("Enter your score (0-100): "))

    if score < 0:
        print("Score cannot be negative.")
    elif score > 100:
        print("Score is too big, maximum is 100.")
    else:
        break

    attempts += 1

attempts += 1

print("Accepted after", attempts, "attempts")
print("Grade:", end=" ")

if score >= 90:
    print("A")
elif score >= 82:
    print("B")
elif score >= 74:
    print("C")
elif score >= 64:
    print("D")
elif score >= 60:
    print("E")
else:
    print("F")