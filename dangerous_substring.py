line = int(input())

string = []

for i in range(line):
    string.append(input())
k = 1
tt = 1
for str in string:
    lst = list(str)
    for i in range(len(lst)):
        if lst[i].isalpha() and lst[i].lower() and k == tt :
            lst[i] = 0
            k = 2
            tt = 2
            continue
        elif lst[i] == ':' or lst[i].isdigit() or lst[i].isalpha() and lst[i].lower() and k == tt:
            lst[i] = 0
            k = 3
            tt = 3
            continue
        elif  lst[i] == '/' and k == tt :
            lst[i] = 0
            k = 4
            tt = 4
            continue

        elif  lst[i].isdigit() or lst[i].isalpha() and lst[i].lower() and k == tt :
            lst[i] = 0
            k = 4
            tt = 4
            continue






