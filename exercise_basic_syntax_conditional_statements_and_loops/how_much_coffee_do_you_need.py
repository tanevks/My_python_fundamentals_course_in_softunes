coffe_counter = 0
while True:
    command = input()
    if command == "END":
        break
    if command.lower() == "coding" or command.lower() == "dog" or command.lower() == "cat" or command.lower() == "movie":
        if command.lower() == command:
            coffe_counter += 1
        else:
            coffe_counter += 2
if coffe_counter <= 5:
    print(coffe_counter)
else:
    print("You need extra sleep")

