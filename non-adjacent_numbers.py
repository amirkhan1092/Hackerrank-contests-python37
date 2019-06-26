# This problem was asked by Airbnb.
#
# Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.
#
# For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.
#
# Follow-up: Can you do this in O(N) time and constant space?


def non_adjacent_max_sum(A):
    inc = 0
    exc = 0
    for i in A:
        inc, exc = exc + i, inc if inc > exc else exc

    if inc > exc:
        return inc
    else:
        return exc


list = eval(input('enter the list for max non-adjacent sum '))
sum = non_adjacent_max_sum(list)
print(sum)