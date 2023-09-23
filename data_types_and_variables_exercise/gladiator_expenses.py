lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
numb_broken_helmet = lost_fights_count // 2
numb_broken_sword = lost_fights_count // 3
numb_broken_shield = lost_fights_count // 6
numb_broken_armor = numb_broken_shield // 2

total_sum = (numb_broken_helmet * helmet_price
             + numb_broken_sword * sword_price
             + numb_broken_shield * shield_price
             + numb_broken_armor * armor_price)
print(f"Gladiator expenses: {total_sum:.2f} aureus")