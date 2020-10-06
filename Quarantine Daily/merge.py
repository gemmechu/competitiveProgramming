class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals = sorted(intervals)
        if (len(intervals)< 2):
            return intervals
        def is_overlap(a,b):
            if(a[1]>=b[0]):
                return True
            
            return False
        
        result = [intervals[0]]
        i = 1
        j = 0
        while i < (len(intervals)):
            a = result[j]
            b = intervals[i]
            
            if(is_overlap(a,b)):
                greater = max(b[1],a[1],b[0])
                merged = [a[0], greater]
                result[j] = merged
            else:
                result.append(b)
                j += 1
            i += 1
        return result
        
