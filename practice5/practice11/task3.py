def get_initials(name: str, surname: str) -> str:
    return f"{name[0].upper()}.{surname[0].upper()}."


def count_letters(text: str, letter: str = "a") -> int:
    letter = letter.lower()
    count = 0
    for ch in text.lower():
        if ch == letter:
            count += 1
    return count


def count_vowels(text: str) -> int:
    vowels = "aeiouy"
    count = 0
    for ch in text.lower():
        if ch in vowels:
            count += 1
    return count


def reverse_text(text: str) -> str:
    result = ""
    for ch in text:
        result = ch + result
    return result


def main():
    name = "Anton"
    surname = "Romaniuk"

    full_name = f"{name} {surname}"
    initials = get_initials(name, surname)
    print(full_name)
    print(f"Initials: {initials}")

    c = len(surname)
    vowels = count_vowels(surname)
    consonants = c - vowels
    print(f"Letters in surname: {c}")
    print(f"Vowels: {vowels}, consonants: {consonants}")

    for v in "aeiou":
        print(f"{v}: {count_letters(surname, letter=v)}")

    print(f"Default letter 'a': {count_letters(surname)}")

    print(f"Reversed surname: {reverse_text(surname)}")

    print(f"Docstring: {count_letters.__doc__}")
    print(f"Annotations: {count_letters.__annotations__}")


if __name__ == "__main__":
    main()