
try:
    a = int(input('enter the first value '))
    b = int(input('enter the second value '))
except (ValueError,EOFError) as e:
    print('error occur',e)
else:
    c = a+b
    print(c)
'''    
python tutorials (Tutorials point )
Geeksforgeeks (Python built in exceptions )
'''



a = [1,2,3,4]

b = list((lambda x:x*x)(a1) for a1 in a)

print(b)