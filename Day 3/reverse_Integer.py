class Solution:
    def reverse(self, x: int) -> int:
        sign = 0
        if str(x).startswith('-'):
            x *= -1
            sign = 1
        temp = ''
        while x // 10 != 0:

            temp += str(x % 10)
            x = x // 10
            if x // 10 == 0:
                temp += str(x % 10)
        if temp.startswith('0'):
            temp = temp[1:]
        if (sign == 1):
            temp = '-' + temp
        return temp
solution = Solution()
print(solution.reverse(320))