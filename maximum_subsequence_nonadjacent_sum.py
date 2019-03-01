# User data in the form of set {1,2,3,4,7,8,6,56,0}

setv = eval(input()[1:-1])


inc = 0
exc = 0

for k in setv:
    inc,exc=exc+k,inc if inc>exc else exc

if exc>inc:
    print('Maximum sum is',exc)
else:
    print('Maximum sum is',inc)