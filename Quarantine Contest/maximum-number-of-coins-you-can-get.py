class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        result = 0
        piles = sorted(piles, reverse = True)
        i = 1
        j = len(piles)-1
        for k in range(len(piles)//3):
            if(i> j):
                break
            result += piles[i]
            i += 2
            j -= 1
        return result
