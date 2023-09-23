n_line = int(input())
open_bracket = 0
close_bracket = 0
counter_bracket = 0
for i in range(n_line):
    current_str = input()
    if current_str == '(':
        open_bracket += 1
        counter_bracket += 1
        if counter_bracket > 1:
            break
    if current_str == ')':
        close_bracket += 1
        counter_bracket -= 1
        if counter_bracket < 0:
            break
if open_bracket == close_bracket and counter_bracket == 0:
    print('BALANCED')
else:
    print('UNBALANCED')
