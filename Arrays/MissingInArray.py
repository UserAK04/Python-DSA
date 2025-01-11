# https://leetcode.com/problems/missing-number/submissions/1504732493/

# Approach:
# Take Sum of first n natural no.s
# Traverse & Take the sum of missingArray
# Difference btw the first sum and second sum is the missing Element

# Revision - |

def missingNumber(arr):
    
    n = len(arr) + 1
    sum = n * (n + 1) // 2
    minSum = 0

    for ele in arr:
        minSum += ele

    return sum - minSum

print(missingNumber([]))
