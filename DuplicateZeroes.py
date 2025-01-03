# https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=array&difficulty=EASY&status=TO_DO


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
