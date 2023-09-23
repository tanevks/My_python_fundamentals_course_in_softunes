key_word = int(input())
numb_row = int(input())
word = ''
for i in range(numb_row):
    ch = input()
    ascii_ch = ord(ch) + key_word
    word += chr(ascii_ch)
print(word, end='')
