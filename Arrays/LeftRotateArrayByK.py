# https://www.geeksforgeeks.org/problems/rotate-array-by-n-elements-1587115621/0

# Approach:
# Edge case is If k is greater than len(arr)
# Then mod it with len(arr)
# Reverse the Array and Compare with Final Answer

# Input:
# arr[] = [1, 2, 3, 4, 5]
# k = 2
# Output: [3, 4, 5, 1, 2]

# Input:
# arr[] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# k = 3
# Output: [8, 10, 12, 14, 16, 18, 20, 2, 4, 6]

# Input:
# arr[] = [7, 3, 9, 1]
# k = 9
# Output: [3, 9, 1, 7]


def leftRotate(arr, k):

    n = len(arr)
    k = k % n

    arr.reverse()

    i = 0
    j = n - k - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    i = n - k
    j = n - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return arr


# OR
def rotateArr(arr, d):
    p = d % len(arr)
    o = arr[p:]

    for i in range(p):
        o.append(arr[i])

    arr.clear()
    arr.extend(o)

    return arr


# print(rotateArr([1, 2, 3, 4, 5], 7))
# print(rotateArr([1, 2], 1))

print(leftRotate([1, 2, 3, 4], 9))
