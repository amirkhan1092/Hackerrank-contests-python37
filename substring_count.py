st = input('enter the string ')

subst = input('enter the substring ')

k = st.find(subst)
count = 0
while k != -1:
    count += 1
    st =st[k+1:]
    k = st.find(subst)

print(count)