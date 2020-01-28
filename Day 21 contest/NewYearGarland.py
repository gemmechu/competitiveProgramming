def garland(ab):
    ab=eval(ab[0]),eval(ab[1]),eval(ab[2])
    ab =sorted(ab)
    if(ab[0]==0):
        print('No')
        return
    else:
        ab=(ab[1])-(ab[0]),(ab[2])-(ab[0])
        if(ab[1]-ab[0]<=2):
            print('Yes')
            return
        else:
            print('No')
            return

       
    


size=eval(input())
for i in range(size):
    ab =input()
    ab=ab.split(' ')
    garland(ab)

    
    