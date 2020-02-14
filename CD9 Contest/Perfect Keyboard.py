


def perfectKeyboard(args):
    result=[]
    for i in range(len(args)-1):
        newElement=[args[i],args[i+1]]
        reversElement = [args[i+1], args[i]]
        if(newElement in result or reversElement in result):
            continue
        else:
            #for a
            result.append(newElement)


    return result

num = eval(input())
for i in range(num):
    args=input()
    print(perfectKeyboard(args))
a=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']