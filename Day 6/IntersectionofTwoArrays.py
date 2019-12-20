from collections import Counter, OrderedDict


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> list[int]:
        arr1_counter = Counter(arr1)
        result = []
        
        for num in arr2:
            result += [num] * arr1_counter.pop(num)
        
        ordered_counter = OrderedDict(sorted(arr1_counter.items()))

        for num in ordered_counter:
            result += [num] * ordered_counter[num]
        
        return result