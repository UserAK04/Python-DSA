n = 3


def isPalindrome(num):

    if num < 10:
        return True

    reverse = 0
    oriN = num

    while num != 0:

        reverse = num % 10 + reverse * 10
        num = num // 10

    if oriN == reverse:
        return True

    return False


print(isPalindrome(n))