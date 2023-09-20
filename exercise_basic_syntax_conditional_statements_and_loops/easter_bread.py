budget = float(input())
price_flour = float(input())
price_eggs = price_flour * 0.75
price_milk = price_flour + price_flour * 0.25
price_bread = price_flour + price_eggs + price_milk / 4
numb_bread = int(budget // price_bread)
lost_colored_eggs = 0
for i in range(1,numb_bread+1):
    if i % 3 == 0:
        lost_colored_eggs += i - 2
numb_colored_eggs = int(numb_bread * 3 - lost_colored_eggs)
money_left = budget - (numb_bread * price_bread)
print(f"You made {numb_bread} loaves of Easter bread! Now you have {numb_colored_eggs} "
      f"eggs and {money_left:.2f}BGN left.")
