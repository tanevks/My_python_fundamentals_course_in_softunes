numb_water = int(input())
capacity = 255
for i in range(numb_water):
    current_liters = int(input())
    if current_liters > capacity:
        print("Insufficient capacity!")
    else:
        capacity -= current_liters
print(255 - capacity)