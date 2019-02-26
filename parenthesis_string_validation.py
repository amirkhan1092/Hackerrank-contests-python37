def findMaxLen(string):
    n = len(string)
    stk = []
    stk.append(0)

    result = 0


    for i in range(n):

        # If opening bracket, push index of it
        if string[i] == '(':
            stk.append(i)

        else:  # If closing bracket, i.e., str[i] = ')'

            stk.pop()

            if len(stk) != 0:
                result = max(result, i - stk[len(stk) - 1])

            else:
                stk.append(i)

    return result
k=input('enter the string ')

print(findMaxLen(k))