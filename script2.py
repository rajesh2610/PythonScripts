Initial Commit
divisors = []
num = int(input("Enter a number"))

for n in range(1, num):
    if num % n == 0:
        divisors.append(n)

print(" This number is divisible by ", divisors)
\
