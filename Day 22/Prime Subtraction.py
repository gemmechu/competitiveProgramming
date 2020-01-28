def primeSubtraction(ab):
    a=eval(ab[0])
    b =eval(ab[1])

    diff=a-b
    if diff>1:
        print("YES")
        return
    else:
        print("NO")
        return

       
    


size=eval(input())
for i in range(size):
    ab =input()
    ab=ab.split(' ')
    primeSubtraction(ab)

    
    