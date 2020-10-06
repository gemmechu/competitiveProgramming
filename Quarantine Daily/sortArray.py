class Solution(object):
     def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        def swap(l,r,nums):
            temp = nums[l]
            nums[l]=nums[r]
            nums[r]=temp
            
        def reccur(start,end,nums):
			# out
            if start>=end: return 
            
            # handle
            l,r = start,end-1
            pivot = nums[end]
            while l<=r:
                if nums[l]>pivot:
                    swap(l,r,nums)
                    r-=1
                else:
                    l+=1
            swap(l,end,nums)
			
            reccur(start,l-1,nums)
            reccur(l+1,end,nums)
        
        # main
        reccur(0,len(nums)-1,nums)
        return nums
