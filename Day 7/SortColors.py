input = [2,0,2,1,1,0]
def sortColors(nums):
    count=[0,0,0]
    size = len(nums)
    result=[]
    if (size == 0 or size == 1 or size == 2):
        print(nums)
        return
    for i in nums:
        count[i] += 1

    for i in range(0, len(count)):
        for j in range(0,count[i]):
            result.append(i)
    print(result)

sortColors(input)