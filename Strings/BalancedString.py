# https://leetcode.com/problems/check-balanced-string/description/

# Input:
num = "1234"
# Output: false

# Input:
# num = "24123"
# Output: true


def solve(num):

    evenSum = 0
    oddSum = 0

    for i in range(len(num)):
        if i % 2 == 0:
            evenSum += int(num[i])
        else:
            oddSum += int(num[i])

    return evenSum == oddSum


print(solve(num))
