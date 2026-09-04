print("Romaniuk Anton, IT-32")

score = int(input("Enter your score: "))
missed = int(input("Enter number of missed classes: "))

if score < 0 or score > 100:
    print("Error: score must be between 0 and 100")
else:
    if score >= 90:
        grade = "A"
        ects = "відмінно"
    elif score >= 82:
        grade = "B"
        ects = "добре"
    elif score >= 74:
        grade = "C"
        ects = "добре"
    elif score >= 64:
        grade = "D"
        ects = "задовільно"
    elif score >= 60:
        grade = "E"
        ects = "задовільно"
    else:
        grade = "F"
        ects = "незадовільно"

    if missed > 16 * 0.3:
        print("Warning: more than 30% of classes were missed")

    if grade == "F":
        result = "failed"
    else:
        result = "passed"

    print(f"Score: {score}, Grade: {grade}, Result: {result}")