class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        i = 1
        while True:
            sqr =float(i*i)
            if(sqr <= x):
                result = i
            else:
                break
            i += 1
        return result
        
