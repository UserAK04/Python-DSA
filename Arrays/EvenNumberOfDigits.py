# https://leetcode.com/problems/find-numbers-with-even-number-of-digits/description/?envType=problem-list-v2&envId=array&difficulty=EASY&status=TO_DO

# Approach:
# Check constraints like size maximum size of digits given
# Use and & or operators for checking
# And count even ones


def best(nums):
    cnt = 0
    for num in nums:
        if (num >= 10 and num <= 99) or (num >= 1000 and num <= 9999) or num == 100000:
            cnt += 1

    return cnt


# Approach:
# Convert each number in array to string then find its length
# Check length of each string is it even or odd using Mod operator
# And count even ones


def better(nums):
    cnt = 0
    for num in nums:
        if len(str(num)) % 2 == 0:
            cnt += 1

    return cnt


def brute(nums):

    cnt = 0
    for n in nums:
        if countDigits(n) % 2 == 0:
            cnt += 1

    return cnt


def countDigits(num):
    if num < 10:
        return 1

    cnt = 0
    while num != 0:
        num = num // 10
        cnt += 1

    return cnt


print(best([12, 3453, 2, 6, 7896]))
