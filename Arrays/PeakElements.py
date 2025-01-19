# https://leetcode.com/problems/find-the-peaks/description/

# Approach:
# If nums[i] > num[i - 1] and nums[i] > nums[i + 1] nums[i] is a peak.

# Input:
# mountain = [2, 4, 4]
# Output: []

# Input:
mountain = [1, 4, 3, 8, 5]
# Output: [1,3]


def solve(arr):

    if len(arr) < 3:
        return []

    n = len(arr)
    res = []
    for i in range(1, n - 1):
        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            res.append(arr[i])

    return res


print(solve(mountain))
