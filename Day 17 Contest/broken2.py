def brokenBoard(key, sample):
    key=key.split(' ')
    sampleList=[]
    for j in sample:
        sampleList.append(j)
    count=[]
    totalcombination=0
    j=0
    while(j<=len(sampleList)-1):
        if(key.__contains__(sampleList[j])==False):
            n=len(sampleList[:j])
            totalcombination+=(n*(n+1))/2
            sampleList = sampleList[j+1:]
            j=0
        else:
            if(j == len(sampleList)-1):
                n=len(sampleList)
                totalcombination+=(n*(n+1))/2
                
            j+=1
    
    print(int(totalcombination))

# substring=sample.split(',')
 #   totalcombination=0
  #  for j in substring:
   #     n=len(j)
    #    if(n>0):
     #       totalcombination+=(n*(n+1))/2 
    

size=input()
sample=input()
key=input()
brokenBoard(key,sample)



