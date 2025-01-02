#https://leetcode.com/problems/two-sum/description/

def better(nums, target):

    mp = {}
    for i in range(len(nums)):
        more = target - nums[i]
        if more in mp:
            return [mp[more], i]

        mp[nums[i]] = i

    return [-1, -1]


def brute(nums, target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:
                return [i, j]


# nums = [2, 7, 11, 15]
nums = [3, 2, 3]
target = 6
print(better(nums, target))
