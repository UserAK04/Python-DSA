# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=problem-list-v2&envId=array&difficulty=EASY&status=TO_DO

# Approach
# Better:
# Created hash map & store the count of each ele
# Extract values from hash map & store in array
# Sort the array & compare consecutive eles

# Optimal:
# Create hash array of 0es by storing count of -ve values from 0
# And +ve values from 1000 at their indexes
# Sort the array, compare consecutive eles & ensure omitting 0es

# Input:
# arr = [1, 2, 2, 1, 1, 3]
# Output: true

# Input:
# arr = [1, 2]
# Output: false

# Input:
arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
# Output: true


def better(arr):

    map = {}
    for x in arr:
        if map.get(x, 0) == 0:
            map[x] = 1
        else:
            map[x] += 1

    map = sorted(map.values())

    for i in range(len(map) - 1):
        if map[i] == map[i + 1]:
            return False

    return True


def opti(arr):

    hash = [0 for i in range(2001)]

    for ele in arr:
        hash[ele + 1000] += 1

    hash.sort()

    for i in range(2000):
        if hash[i] != 0 and hash[i] == hash[i + 1]:
            return False

    return True


# print(better(arr))
print(opti(arr))
