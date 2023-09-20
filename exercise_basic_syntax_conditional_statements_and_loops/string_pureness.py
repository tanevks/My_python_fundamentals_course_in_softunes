n = int(input())
for i in range(n):
    current_string = input()
    string_pureness = ("," in current_string or "." in current_string or "_" in current_string)
    if string_pureness:
        print(f"{current_string} is not pure!")
    else:
        print(f"{current_string} is pure.")
