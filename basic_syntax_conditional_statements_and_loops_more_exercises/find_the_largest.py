numb = input()
result = ''
max_numb = sorted(numb, reverse=True)
for i in max_numb:
    result += i
print(result)
