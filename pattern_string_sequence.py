# string="subsequence"
# pattern="sue"

st=input()[8:-1]
pt=input()[9:-1]
num=0
for p in pt:
    num += st.count(p)

print(num)