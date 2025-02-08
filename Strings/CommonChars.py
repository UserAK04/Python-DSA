# https://leetcode.com/problems/find-common-characters/description/?envType=problem-list-v2&envId=string

# Input:
words = ["bella", "label", "roller"]
# Output: ["e","l","l"]

# Input:
# words = ["cool", "lock", "cook"]
# Output: ["c","o"]


def solve(words):

    resultMap = {}

    for ele in words[0]:
        if resultMap.get(ele, "#") == "#":
            resultMap[ele] = 1
        else:
            resultMap[ele] += 1

    for word in words:

        currentMap = {}
        for ele in word:
            if currentMap.get(ele, "#") == "#":
                currentMap[ele] = 1
            else:
                currentMap[ele] += 1

        for key in resultMap:
            resultMap[key] = min(resultMap.get(key, 0), currentMap.get(key, 0))

    result = []
    for key in resultMap:

        for i in range(resultMap[key]):
            result.append(key)

    return result


print(solve(words))
