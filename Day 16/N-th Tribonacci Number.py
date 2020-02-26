class Solution:
    def tribonacci(self, n: int) -> int:
        def helper(n:int, cache):
            if(n<=2):
                return cache[n]
            elif(n in cache):
                return cache[n]
            else:
                cache[n] = helper(n-3,cache)+ helper(n-2, cache) + helper(n-1, cache)
            return cache[n]
        cache= {0:0, 1: 1, 2: 1}
        return helper(n, cache)
main = Solution()
print(main.tribonacci(25))