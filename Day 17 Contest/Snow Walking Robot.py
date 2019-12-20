
def snowWalk(sample):
    howmany={'L':0,'R':0,'U':0,'D':0}
    for i in range(0,len(sample)):
        howmany[sample[i]]+=1
    
    if(howmany['L'] or howmany['R'] or howmany['U'] or howmany['D'] !=0 ):
        if(howmany['L'] > howmany['R']):
            howmany['L'] = howmany['R']
        else:
            howmany['R'] = howmany['L']
        if(howmany['U'] > howmany['D']):
            howmany['U'] = howmany['D']
        else:
            howmany['D'] = howmany['U']
        
    if(howmany['L'] and howmany['D'] !=0 ):
        distance = (howmany['D']+howmany['R'])*2
        print(distance)
        res = "L" * howmany['L'] + "U" * howmany['U'] + "R" * howmany['R'] + "D" * howmany['D']
        print(res)  
    elif(howmany['L'] ==0):
        if(howmany['U'] !=0):
            print(2)
            print("UD")
        else:
            print(0)
    elif(howmany['U'] ==0):
        if(howmany['L'] !=0):
            print(2)
            print("LR")
        else:
            print(0)
    
    else:
        print(0)


            
number = eval(input())

if(number>0):
    for i in range(0,number):
        sample=input()
        snowWalk(sample) 