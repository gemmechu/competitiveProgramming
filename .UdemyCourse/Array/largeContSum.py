def largeContSum(arr):
    maxSum=currSum=arr[0]

    for i in arr[1:]:
        currSum=max(currSum+i, i)
        maxSum=max(currSum,maxSum)
    return maxSum
a=[1,-1,3,4,10,-1]
print(largeContSum(a))