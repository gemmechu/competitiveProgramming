def kforthePriceofOne(ab,abc):
    abc=sorted(abc)
    p=int(ab[1])
    k=int(ab[2])
    count=0
    if p< int(abc[0]):
        print(count)
        return
    c=len(abc)
    for i in range(c):
        if(p>=int(abc[i])):
            if(i+k<=c-1):
                if(p>=int(abc[i+k])):
                    p-=int(abc[i])
                    if(i+k==c-1):
                        if(i==0):
                            count+=1
                        else:
                            count+=2
                            break
                        
                    else:
                        count+=1
                elif(p>=int(abc[i+1])):
                    count+=2
                    break
                else:
                    count+=1
                    break
            else:
                count+=1
            
            
    print(count)


size=eval(input())
for i in range(size):
    ab =input()
    ab=ab.split(' ')
    n = int(ab[0])
    abc =input()
    abc= abc.split(' ')
    kforthePriceofOne(ab,abc)

    
    