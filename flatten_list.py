##a = [[1,2,[3,4]],[5,6],7]
##h = []
##for i in a:
##    if type(i) is list:
##        for k in i:
##            if type(k) is list:
##                
##                h.extend(k)
##            else:
##                h.append(k)
##    else:
##         h.append(i)
##
##print(h)        


ls = [[1,2,[2,3,[3,5,[2,4,[4,6]]]]],4,[4,5,[5,6]]]
flatten = []
while 1:
    for i in ls:
        if type(i) is list:
            flatten.extend(i)
        else:
            flatten.append(i)
    ls = flatten[:]
    flatten.clear()
    bd = [type(l) is list for l in ls]
    if not any(bd):
        break
            
        
print(ls)
