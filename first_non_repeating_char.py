
st =  input()

for i in st:
    if st.count(i) == 1:
        print(i)
        break
else:
    print(None)