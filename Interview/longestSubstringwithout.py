def checkDuplicate(s):
    myset = set()
    for i in range(len(s)):
        if (s[i] not in myset):
            myset.add(s[i])

        else:
            return False
    return True


def maxSubstring(s: str) -> int:
    # if str empty
    if (len(s) < 1):
        return 0

    result = 1

    start = 0
    while True:
        # "bacabcbb"
        if (start + result + 1 > len(s) - 1):
            return result
        noduplicate = checkDuplicate(s[start: start + result + 1])
        if (nodublicate):
            result += 1
    else:
        start += 1