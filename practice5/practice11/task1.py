def print_card():
    print("Anton Romaniuk, IT-32")
    print(f"Name: Anton Romaniuk")
    print(f"Group: IT-32")
    print(f"Birth year: 2008")


def print_card_args(name, surname, year, group="IT-32"):
    print(f"Name: {name} {surname}")
    print(f"Group: {group}")
    print(f"Birth year: {year}")


def main():
    print("--- no parameters, call 1 ---")
    print_card()
    print("--- no parameters, call 2 ---")
    print_card()
    print("--- no parameters, call 3 ---")
    print_card()

    print("--- positional arguments ---")
    print_card_args("Anton", "Romaniuk", 2008, "IT-32")

    print("--- keyword arguments ---")
    print_card_args(year=2008, group="IT-32", surname="Romaniuk", name="Anton")

    print("--- mixed: positional + keyword ---")
    print_card_args("Anton", "Romaniuk", year=2008, group="IT-32")

    print("--- default group (group not passed) ---")
    print_card_args("Anton", "Romaniuk", 2008)


if __name__ == "__main__":
    main()