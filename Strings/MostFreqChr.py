# https://www.geeksforgeeks.org/problems/maximum-occuring-character-1587115620/1?

# Approach:
# Take a alphabets hash array of 27 size ( as 26 alphabets )
# Store freq of each alphabet in the hash array
# Getting each index by [ ASCII(alpha) - 97 ]-> for lowercase
# Finally check the max value in array and store its index in another variable

# Input:
s = "testsample"
# Output: 'e'

# Input:
# s = "output"
# Output: 't'


def solve(s):

    res = [0 for i in range(27)]

    for ele in s:
        res[ord(ele) - 97] += 1

    maxFreq = 0
    maxFreqChr = ""
    for i in range(27):
        if res[i] > maxFreq:
            maxFreq = res[i]
            maxFreqChr = chr(i + 97)

    return maxFreqChr


print(solve(s))
