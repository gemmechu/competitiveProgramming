def brokenBoard(key, sample):
    key=key.split(' ')
    count=0
    for j in sample:
        if(key.__contains__(j)==False):
            sample=sample.replace(j,',')
 
 
    substring=sample.split(',')
    totalcombination=0
    for j in substring:
        n=len(j)
        if(n>0):
            totalcombination+=(n*(n+1))/2
    print(int(totalcombination))
 
size=input()
sample=input()
key=input()
brokenBoard(key,sample)