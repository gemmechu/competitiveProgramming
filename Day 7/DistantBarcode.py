input = [1,2,2,4,4,4]
def rearrangeBarcodes(self, barcodes: list[int]) -> list[int]:
    count=[0,0,0,0,0,0,0,0,0,0]
    result=[]
    size= len(barcodes)
    if(size==0 or size==1 or size==2):
        print(barcodes)
        return
    for i in barcodes:
        count[i]+=1
    while size >0:
        for j in range(0,9):
            if(size!=len(barcodes) and result[len(result)-1]==j):
                check = sorted(count)
                if(check[1]==0):
                    print('un doable')
                    return
                continue
            else:
                if(count[j]!=0):
                    result.append(j)
                    count[j]-=1
                    size-=1
    return result

an = rearrangeBarcodes(input)
print(an)