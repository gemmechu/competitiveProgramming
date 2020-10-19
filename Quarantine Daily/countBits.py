class Solution:
    def countBits(self, num: int) -> List[int]:
        result = []
        for i in range(num+1):
            curr = list(bin(i)[2:])
            result.append(curr.count('1'))
        
        return result
