numb_snowballs = int(input())
max_weight = 0
max_time = 0
max_quality = 0
max_snowball = 0
value_snowball = 0
for current_snowball in range(numb_snowballs):
    snowball_weight = int(input())
    snowball_time = int(input())
    snowball_quality = int(input())
    value_snowball = (snowball_weight / snowball_time) ** snowball_quality
    if value_snowball > max_snowball:
        max_snowball = value_snowball
        max_weight = snowball_weight
        max_time = snowball_time
        max_quality = snowball_quality

print(f"{max_weight} : {max_time} = {int(max_snowball)} ({max_quality})")