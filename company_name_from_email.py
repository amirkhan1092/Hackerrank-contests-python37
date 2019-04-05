
a = input('enter the the emailId ')

b = a[a.find('@')+1:]
b = b[:b.find('.')]
print(b)
