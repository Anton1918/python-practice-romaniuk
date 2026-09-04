print("Romaniuk Anton, IT-32")

name = input("Enter your name: ")
age_input = input("Enter your age (integer): ")

if age_input.strip() == "":
    print("Hello, Anonymous!")
else:
    age = int(age_input)

    if age < 0:
        category = "некоректне значення"
    elif age <= 6:
        category = "child"
    elif age <= 17:
        category = "schoolchild"
    elif age <= 64:
        category = "adult"
    else:
        category = "senior"

    print(f"Hello, {name}! You are a {category}.")