a = open('tabledata.dat')
print(a.readlines())
a.seek(0)
line = a.readline()
line = a.readline()
India = []
France = []
print(line)

# print(line.split())

while len(line):

    fst = line.split()
    print(fst)
    India.append(int(fst[0]))
    France.append(int(fst[1]))
    line = a.readline()

print(sum(India)//len(India))
print(sum(France)//len(France))
print(France)

