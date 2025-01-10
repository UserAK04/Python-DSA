# https://leetcode.com/problems/find-closest-number-to-zero/description/?envType=problem-list-v2&envId=array&difficulty=EASY&status=TO_DO

# Approach:
# Traverse accross the array
# Take absolute value of each element & store the smallest & it's signed value as well
# that is, store absolute smallest element & it's signed value in 2 variables

# If same val is present in -ve & +ve form in the array then return +ve one

# Revision - |


def solve(nums):
    closest = 1e9
    val = 0

    for ele in nums:
        if abs(ele) < closest:
            closest = abs(ele)
            val = ele
        elif abs(ele) == closest:
            val = max(ele, val)

    return val


# Edge Cases
# nums = [0]
# nums = [-100000, -100000]
nums = [-1, 1]

print(solve(nums))
