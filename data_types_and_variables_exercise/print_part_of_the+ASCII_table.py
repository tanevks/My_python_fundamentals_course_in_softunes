start_char = int(input())
end_char = int(input())
result = ''
for i in range(start_char, end_char+1):
    if i == end_char:
        result += chr(i)
    else:
        result += chr(i) + ' '
print(result)