# https://www.geeksforgeeks.org/problems/sum-of-numbers-in-string-1587115621/1?page=2&category=Strings&difficulty=Basic,Easy&status=unsolved&sortBy=submissions

# Approach:
# Take a sum var and num var to store complete number
# if digit found then update to num var
# Else concat num to sum & initialize num to 0
# if String ends with digit then return (sum+num)

# Input:
s = "1abc23"
# Output: 24

# Input:
# s = "geeks4geeks"
# Output: 4


def findSum(s):

    sum = 0
    num = 0
    for x in s:

        if ord(x) >= 48 and ord(x) <= 57:
            num = num * 10 + int(x)
        else:
            sum += num
            num = 0

    return sum + num


print(findSum(s))
