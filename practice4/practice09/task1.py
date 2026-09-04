name = "Anton"
surname = "Romaniuk"
group = "IT-32"

d = 30
c = 8

print(name, surname, group)

count = 0
total = 0
product = 1
even = 0
odd = 0

print("Numbers from", d, "to 31:", end=" ")

for i in range(d, 32):
    print(i, end=" ")
    count += 1
    total += i
    product *= i

    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print()

average = total / count

print("Count:", count)
print("Sum:", total)
print("Product:", product)
print(f"Average: {average:.2f}")
print("Even:", even, ", odd:", odd)

print("Countdown:", end=" ")
for i in range(c, 0, -1):
    print(i, end=" ")