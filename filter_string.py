
a = input('enter the string ')
s = ''
for i in a:
    if i.isalnum() or i == '/':
        s += i
    elif s.endswith('_'):
        continue
    else:
        s += '_'

print(s)


