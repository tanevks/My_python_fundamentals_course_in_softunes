flock_of_sheep = input()
sheep_wolf = ''
list_sheep = []
for i in range(len(flock_of_sheep)):
    if flock_of_sheep[i] != ',' and flock_of_sheep != ' ':
        sheep_wolf += flock_of_sheep[i]
        if flock_of_sheep[i] == ' ':
            sheep_wolf = ''
            continue
    else:
        list_sheep.append(sheep_wolf)
list_sheep.append(sheep_wolf)
index_wolf = list_sheep.index('wolf')
len_list_sheep = len(list_sheep)
if index_wolf == len(list_sheep)-1:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {len_list_sheep - index_wolf -1}! You are about to be eaten by a wolf!" )
