numb_people = int(input())
capacity_elevator = int(input())
courses = numb_people // capacity_elevator

if numb_people % capacity_elevator != 0:
    courses += 1
print(courses)