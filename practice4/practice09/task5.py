name = "Anton"
surname = "Romaniuk"
group = "IT-32"

d = 30
c = 8

n = d * c

print(name, surname, group)
print("n =", d, "*", c, "=", n)

divisors = []
divisor_sum = 0

for i in range(1, n + 1):
    if n % i == 0:
        divisors.append(i)
        divisor_sum += i

print("Divisors:", *divisors)
print("Divisors count:", len(divisors), ", sum:", divisor_sum)

is_prime = True

if n < 2:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break
    else:
        is_prime = True

if is_prime:
    print(n, "is prime")
else:
    print(n, "is not prime")

primes = []

for number in range(2, n + 1):
    for i in range(2, number):
        if number % i == 0:
            break
    else:
        primes.append(number)

print("Primes up to", n, ":", *primes)
print("Primes count:", len(primes))