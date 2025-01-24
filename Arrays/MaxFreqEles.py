# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=problem-list-v2&envId=array&difficulty=EASY&status=TO_DO

# Approach:
# Better
# Use a FreqArray to store freq of each ele & simul. check max freq
# Count all max freq eles

# Best
# Use hashmap/dict to store freq of each ele & simul. check max freq
# Count all max freq eles

# Input:
# nums = [1, 2, 2, 3, 1, 4, 2]
# Output: 4

# Input:
nums = [1, 2, 3, 4, 5]
# Output: 5


def better(nums):

    maxFreq = 0
    freqMap = [0 for i in range(101)]

    for ele in nums:
        freqMap[ele] += 1
        if freqMap[ele] > maxFreq:
            maxFreq = freqMap[ele]

    cntMaxFreqEles = 0

    for freq in freqMap:
        if freq == maxFreq:
            cntMaxFreqEles += maxFreq

    return cntMaxFreqEles


def best(nums):

    hash = {}
    maxFreq = 0
    for ele in nums:
        if hash.get(ele, 0) == 0:
            hash[ele] = 1
        else:
            hash[ele] += 1
        if hash[ele] > maxFreq:
            maxFreq = hash[ele]

    cntMaxFreqEles = 0
    for key in hash:
        if hash[key] == maxFreq:
            cntMaxFreqEles += maxFreq

    return cntMaxFreqEles


print(better(nums))
