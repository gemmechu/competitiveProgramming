

def findDistance(argument):
    for i in range(0,3):
        if(argument[i]<0):
            argument[i]= argument[i]*-1
    newarg=sorted(argument)
    distance=0
    if(argument[0]==argument[1]==argument[2]):
        print(distance)
        return
    else:
        if((newarg[0]==newarg[1]) or (newarg[1]==newarg[2])):
            
            distance= (newarg[2]-1)-newarg[0]
            distance2=newarg[2]-newarg[0]-2
            if(abs(distance)>abs(distance2)):
                print(distance2)
            else:
                print(distance)
        else:
            newarg[0]=newarg[0]+1
            newarg[2]=newarg[2]-1
            distance=abs(newarg[0]- newarg[1])+ abs(newarg[0]-newarg[2])+ abs(newarg[1]-newarg[2])
            print(distance)

        
number = eval(input())

if(number>0):
    for i in range(0,number):
        argument=[]
        j=0
        for j in range(0,3):
            argument.append(eval(input()))
        findDistance(argument) 
