n = int(input())
for digit in range(1, n+1):
    digit_str = str(digit)
    sum_digit = 0
    for j in digit_str:
        sum_digit += int(j)
    if sum_digit in [5,7,11]:
        print(f'{digit} -> True')
    else:
        print(f'{digit} -> False')
