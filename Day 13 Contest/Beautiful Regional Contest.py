
def beutifulReg(params):
    mydict={}
    g=0
    s=0
    b=0
    for i in range(len(params)):
        if(mydict.get(params[i])!=None):
            mydict[params[i]]+=1
        else:
            mydict[params[i]]=1
    nums=list( mydict.values())
    mean=int(len(params)/2)
    summation=0
    for i in range(len(nums)):
        summation+=nums[i]
        if(summation>mean):
            nums=nums[:i]
            break
    for i in range(len(nums)):
        if(g==0):
            g=nums[i]
        else:
            if(s<=g):
                s+=nums[i]

            elif(b<=g):
                b+=nums[i]
    if(g<s and g<b):
        print(g,s,b)
    else:
        print(0,0,0)




num=eval(input())
for i in range(num):
    num2=input()
    args=input()
    args=args.split(' ')
    beutifulReg(args)

