numb_int = int(input())
prime_numb = True
for i in range(2, numb_int):
    if numb_int % i == 0:
        prime_numb = False
        break
print(prime_numb)