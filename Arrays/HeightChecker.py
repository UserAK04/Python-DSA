# https://leetcode.com/problems/height-checker/description/?envType=problem-list-v2&envId=array&difficulty=EASY&status=TO_DO

# Input: heights = [1,1,4,2,1,3]
# Output: 3
# Explanation:
heights = [1, 1, 4, 2, 1, 3]
# expected: [1,1,1,2,3,4]
# Indices 2, 4, and 5 do not match.
# Example 2:

# Input: heights = [5,1,2,3,4]
# Output: 5
# Explanation:
# heights = [5, 1, 2, 3, 4]
# expected: [1,2,3,4,5]
# All indices do not match.
# Example 3:

# Input: heights = [1,2,3,4,5]
# Output: 0
# Explanation:
# heights = [1, 2, 3, 4, 5]
# expected: [1,2,3,4,5]


def solve(heights):

    expected = sorted(heights)
    cnt = 0
    for i in range(len(heights)):
        if expected[i] != heights[i]:
            cnt += 1
    return cnt


print(solve(heights))
