divisor = int(input())
boundary = int(input())
divisible = 0
for i in range(divisor, boundary + 1):
    if i % divisor == 0:
        divisible = i
print(divisible)
