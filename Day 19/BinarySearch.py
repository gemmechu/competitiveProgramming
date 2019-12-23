

def search(nums, target: int) -> int:
    end=len(nums)-1
    base=0
    while (base<=end):
        mid = int((base + end)/2)
        if nums[mid] == target:
            return mid
            break
        elif  target < nums[mid]:
            end= mid-1
        else:
            base=mid+1
    return -1

def binarySearch(arr, base,end,val)->int:
    if end>=end:
        mid = int((base + end)/2)
        
        if arr[mid]==val:
            return mid
        
        elif arr[mid]>val:
            
            return binarySearch(arr[:mid],base,mid-1,val)
        else:
            
            return binarySearch(arr[mid:],mid+1,end,val)
    else:
        return -1
arr= [2,4,5,7,10,50]
val = 50
base=0
end=len(arr)-1
print(search(arr,val))
