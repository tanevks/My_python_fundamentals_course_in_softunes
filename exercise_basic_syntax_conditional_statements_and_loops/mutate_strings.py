string_1 = input()
string_2 = input()
string_rez = ""
for i in range(len(string_1)):
    string_rez = string_2[:i+1:] + string_1[i+1:len(string_1):]
    if string_rez != string_1:
        print(string_rez)
        string_1 = string_rez
