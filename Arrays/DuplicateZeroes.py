# https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=array&difficulty=EASY&status=TO_DO

# Approach:
# Take 2 ptrs i & j
# Keep i at last pos of arr & j at (last pos + no. of zeroes in arr)
# While they are not equal, duplicate ith ele to jth pos and then decrement both i , j
# If ith ele is 0 then duplicate ith ele to jth pos and then decrement j

def duplicateZeros(arr):

    z = arr.count(0)

    i = len(arr) - 1
    j = len(arr) + z - 1

    while i != j:

        insert(arr, i, j)
        j -= 1

        if arr[i] == 0:
            insert(arr, i, j)
            j -= 1

        i -= 1

    return arr


def insert(arr, i, j):
    if j < len(arr):
        arr[j] = arr[i]


# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]

print(duplicateZeros([1, 0, 2, 3, 0, 4, 5, 0]))
