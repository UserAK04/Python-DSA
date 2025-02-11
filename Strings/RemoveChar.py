# https://www.geeksforgeeks.org/problems/remove-character3815/1?page=2&category=Strings&difficulty=Basic,Easy&status=unsolved&sortBy=submissions

# Approach:
# Hash the string2 which needs to be searched for
# By using .get() method of dict find and skip those letter

# Input:
# string1 = "computer"
# string2 = "cat"
# Output: "ompuer"

# Input:
string1 = "occurrence"
string2 = "car"
# Output: "ouene"


def removeChars(string1, string2):

    hash = {}
    for x in string2:
        hash[x] = 1

    result = ""
    for x in string1:
        if hash.get(x, 0) == 0:
            result += x
        else:
            continue

    return result
