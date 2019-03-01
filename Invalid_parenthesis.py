h=input()
c=0
for k in h:
    if k == '(':
        c +=1
    elif k == ')':
        c -=1
        if c<0:
            break
if c==0:
    print('\'True\'')
else:
    print('\'False\'')