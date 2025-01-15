# https://leetcode.com/problems/number-of-senior-citizens/description/

# Approach:
# Convert the value at index 11 and 12 to a numerical value.


# Input:
details = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
# Output: 2

# Input:
# details = ["1313579440F2036", "2921522980M5644"]
# Output: 0


def countSeniors(details):

    seniorsCnt = 0
    for detail in details:
        if int(detail[11:13]) > 60:
            cntSeniors += 1

    return cntSeniors


print(countSeniors(details))
