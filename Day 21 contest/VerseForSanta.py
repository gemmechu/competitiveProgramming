def VerseForSanta(ab,second):
    
    newmax=0
    j=-1
    skip=0
    
    while True:
        i=0
        max=0    
        
        for i in range(len(ab)):
            if(j !=i):
                if(eval(ab[i])<=second):
                    if( max>=second):
                        break
                    else:
                        temp=max
                        max+=eval(ab[i])
                        if(max>second):
                            max=temp
                            break
                if(newmax<max):
                    skip=i+1
                    newmax=max
        j+=1
        
        if(j==len(ab)):
            break
    print(skip)
    
        
    

       
    


size=eval(input())
for i in range(size):
    abc=input()
    ab =input()
    abc=abc.split(' ')
    ab=ab.split(' ')
    VerseForSanta(ab,eval(abc[1]))

    
    