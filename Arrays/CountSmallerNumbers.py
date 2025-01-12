# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/?envType=problem-list-v2&envId=array&difficulty=EASY&status=TO_DO

# Input:
# nums = [8, 1, 2, 2, 3]
# Output: [4, 0, 1, 1, 3]

# Input:
# nums = [6, 5, 4, 8]
# Output: [2,1,0,3]

nums = [1, 1]

# Approach:
# Sort the array & observe its elements relative to its indexes.
# Store this relation in the map & think of the duplicates as well


def better(nums):
    # Space : O(2N)
    # Time : O(2N)

    n = len(nums)

    sortedNums = sorted(nums)
    mapp = {}
    for i in range(n):
        if sortedNums[i] != sortedNums[i - 1]:
            mapp[sortedNums[i]] = i

    for i in range(n):
        nums[i] = mapp.get(nums[i], 0)

    return nums


def brute(nums):

    n = len(nums)
    res = []

    for i in range(n):
        cnt = 0
        for j in range(n):
            if nums[i] > nums[j]:
                cnt += 1
        res.append(cnt)

    return res


print(better(nums))
