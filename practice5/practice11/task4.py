def read_grade(prompt):
    while True:
        raw = input(prompt)
        if not raw.lstrip("-").isdigit():
            print("Error: digits only")
            continue
        value = int(raw)
        if value < 0 or value > 100:
            print("Error: the value must be between 0 and 100")
            continue
        return value


def to_letter(grade):
    if grade >= 90:
        return "A"
    if grade >= 80:
        return "B"
    if grade >= 70:
        return "C"
    if grade >= 60:
        return "D"
    if grade >= 50:
        return "E"
    return "F"


def average(grades):
    return sum(grades) / len(grades)


def count_above(grades, limit):
    count = 0
    for g in grades:
        if g > limit:
            count += 1
    return count


def print_report(name, group, grades):
    avg = average(grades)
    letter = to_letter(avg)
    above = count_above(grades, avg)

    print("--- Report ---")
    print(f"Student: {name}, group {group}")
    print("Grades:", " ".join(str(g) for g in grades))
    print(f"Average: {avg:.2f} -> {letter}")
    print(f"Best: {max(grades)}, worst: {min(grades)}")
    print(f"Above average: {above}")


def main():
    name = "Anton Romaniuk"
    group = "IT-32"
    n = 5

    grades = []
    for i in range(1, n + 1):
        grade = read_grade(f"Grade {i} (0-100): ")
        grades.append(grade)

    print_report(name, group, grades)


main()