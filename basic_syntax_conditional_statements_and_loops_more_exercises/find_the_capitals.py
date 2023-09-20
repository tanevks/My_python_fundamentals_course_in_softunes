current_string = input()
current_list = []
for i in range(len(current_string)):
    x = ord(current_string[i])
    if 65 <= x <= 90:
        current_list.append(i)
print(current_list)
