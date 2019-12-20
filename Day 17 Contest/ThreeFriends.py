

def findDistance(argument):
    distance=0
    argument=sorted(argument)
    a=argument[0]
    b=argument[1]
    c=argument[2]
    if (a<b and b<c):
        a+=1
        c-=1
        
    elif (a==b and a!=c):
        if(c == b + 1):
            c-=1
        else:
            a+=1
            b+=1
            c-=1
    elif (b == c and a != b):
        if (a == b - 1):
            a+=1
        else:
            a+=1
            b-=1
            c-=1
    distance=abs(a - b) + abs(b - c) + abs(a - c)
    print(distance)
    
        
number = eval(input())

if(number>0):
    for i in range(number):
        argument=[]
        temp=input()
        argument1=temp.split(' ')
        j=0
        for j in range(3):
            argument.append(eval(argument1[j]))
        findDistance(argument)
