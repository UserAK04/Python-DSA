# https://leetcode.com/problems/minimum-absolute-difference/description/?envType=problem-list-v2&envId=array&difficulty=EASY&status=TO_DO

# Revision - |

# Approach:
# Sort the array
# Traverse & determine the min absolute difference present in the array
# Again Traverse and store the values 
# Whose consecutive's difference is equal to Min absolute diff

# Input:
arr = [4, 2, 1, 3]
# Output: [[1,2],[2,3],[3,4]]

# Input:
# arr = [1, 3, 6, 10, 15]
# Output: [[1,3]]

# Input:
# arr = [3, 8, -10, 23, 19, -4, -14, 27]
# Output: [[-14,-10],[19,23],[23,27]]


def solve(arr):

    arr.sort()
    absMinDiff = 1e9
    for i in range(len(arr) - 1):
        if abs(arr[i + 1] - arr[i]) < absMinDiff:
            absMinDiff = abs(arr[i + 1] - arr[i])

    res = []

    for i in range(len(arr) - 1):
        if abs(arr[i + 1] - arr[i]) == absMinDiff:
            res.append([arr[i], arr[i + 1]])

    print(res)

    return absMinDiff


print(solve(arr))
