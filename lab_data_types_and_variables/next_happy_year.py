init_year = int(input())
while True:
    init_year += 1
    str_year = str(init_year)
    set_year = set(str_year)
    if len(str_year) == len(set_year):
        print(init_year)
        break
