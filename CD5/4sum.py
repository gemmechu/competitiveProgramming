class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum1 = {}
        sum2 = {}
        n  = len(nums1)
        for i in range(n):
            a = nums1[i]
            c = nums3[i]
            for j in range(n):
                
                b = nums2[j]
                d = nums4[j]
                key = a+b
                key2= c+d
                if key in sum1:
                    sum1[key] += 1
                else:
                    sum1[key] = 1
                if key2 in sum2:
                    sum2[key2] += 1
                else:
                    sum2[key2] = 1
        result = 0
        for key in sum1:
            if -key in sum2:
                result += sum1[key]* sum2[-key]
        return result
