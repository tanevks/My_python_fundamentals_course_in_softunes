numb = int(input())
for i in range(numb):
    for j in range(numb):
        for k in range(numb):
            result = chr(97 + i) + chr(97 + j) + chr(97 + k)
            print(result)