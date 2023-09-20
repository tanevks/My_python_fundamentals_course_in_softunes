current_string = ""
while True:
    command = input()
    if command == "End":
        break
    for i in command:
        current_string += i * 2
    if command != "SoftUni":
        print(current_string)
    current_string = ""
