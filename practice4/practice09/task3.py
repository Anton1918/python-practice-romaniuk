name = "Anton"
surname = "Romaniuk"
group = "IT-32"

text = name + surname

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1
    elif char.isalpha():
        consonant_count += 1

print(name, surname, group)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print("Total letters:", vowel_count + consonant_count)