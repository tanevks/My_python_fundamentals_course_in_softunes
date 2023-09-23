numb_of_char = int(input())
counter = 0
for i in range(numb_of_char):
    current_char = input()
    counter += ord(current_char)
print(f"The sum equals: {counter}")