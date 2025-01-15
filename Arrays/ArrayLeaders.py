# https://www.geeksforgeeks.org/problems/leaders-in-an-array-1587115620/1

# Approach:
# Start Traversing from backwards
# Update latest maximum element and if arr[i] >= Latest Maximum Element, then its the array leader

# Input:
arr = [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

# Input:
# arr = [10, 4, 2, 4, 1]
# Output: [10, 4, 4, 1]
# Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right. side

# Input:
# arr = [5, 10, 20, 40]
# Output: [40]
# Explanation: When an array is sorted in increasing order, only the rightmost element is leader.

# Input:
# arr = [30, 10, 10, 5]
# Output: [30, 10, 10, 5]
# Explanation: When an array is sorted in non-increasing order, all elements are leaders.


def solve(arr):

    n = len(arr)
    res = []
    maxx = 0

    for i in range(n - 1, -1, -1):
        if arr[i] >= maxx:
            res.append(arr[i])
            maxx = arr[i]

    return res[::-1]


print(solve(arr))
