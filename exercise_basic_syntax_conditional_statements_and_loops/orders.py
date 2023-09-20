n = int(input())
total_price = 0

for i in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if 0.01 > price_per_capsule or price_per_capsule > 100:
        continue
    if 1 > days or days > 31:
        continue
    if 1 > capsules_needed_per_day or days > 2000:
        continue
    price_for_the_coffe = price_per_capsule * capsules_needed_per_day * days
    print(f'The price for the coffee is: ${price_for_the_coffe:.2f}')
    total_price += price_for_the_coffe
print(f'Total: ${total_price:.2f}')
