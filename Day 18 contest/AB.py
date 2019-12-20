import string
def checkAb(a,b):
    count=0
    i=1
    while True:
        if(a==b):
            print(count)
            break
        else:
            dc=b-a
            if(dc>=i):
                a+=i
                count+=1
            else:
                b+=i
                count+=1
            i+=1

        
 
size=eval(input())
for i in range(size):
    ab =input()
    ab=ab.split(' ')
    a = int(ab[0])
    b = int(ab[1])
    if(a==b):
        print(0)
    else:
        if(b<a):
                temp=b
                b=a
                a=temp
        checkAb(a,b)
