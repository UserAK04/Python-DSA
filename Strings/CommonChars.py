# https://leetcode.com/problems/find-common-characters/description/?envType=problem-list-v2&envId=string

# Approach:
# Use first word as the reference word & hash it's chars frequency
# Now do this for each word & compare the first freqmap with each new freqmaps
# Update the first freqmap with the min value of freq from the comparison


# Input:
words = ["bella", "label", "roller"]
# Output: ["e","l","l"]

# Input:
# words = ["cool", "lock", "cook"]
# Output: ["c","o"]


def solve(words):

    resultMap = {}
    refWord = words[0]
    for ele in refWord:
        if resultMap.get(ele, "#") == "#":
            resultMap[ele] = 1
        else:
            resultMap[ele] += 1

    for i in range(1, len(words)):

        currentMap = {}
        for ele in words[i]:
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
