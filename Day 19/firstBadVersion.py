

def isBad(n)->bool:
    check={1:True,2:False,3: False,4:True,5:True}
    return check[n]

def checkBadNumber(n):
    arr=list(range(1,n+1))
    base=0
    end=len(arr)-1
    a=binarySearch(arr,base,end)
    print(a)
def binarySearch(arr,base,end):
    if base<end:
        mid = int(base + (end-base)/2)

        if isBad(arr[mid])==True:
            end=mid
            return binarySearch(arr,base,end)
        else:
            base=mid+1
            return binarySearch(arr,base,end)
    else:
        
        return -1
def binarySearch1(n):

    begin =1
    end=n
    while begin<end:
        mid = int(begin + (end-begin)/2)
        if isBad(mid):
            end=mid
        else:
            if isBad(mid+1):
                return mid+1
            begin=mid

    return begin
  
print(binarySearch1(4))