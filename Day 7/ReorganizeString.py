count = "abbcc"
dictionary={}
size= len(count)
for i in range(0,len(count)):
    if(dictionary.get(count[i])!= None):
        dictionary[count[i]]=dictionary[count[i]]+1
    else:
        dictionary[count[i]]=1
l=dictionary.keys()

result=[]
newDictionary=list(dictionary.keys())
while size >0:

    for j in range(0,len(newDictionary)):
        if(size!=len(count) and result[len(result)-1] == newDictionary[j]):
            continue
        else:
            if(dictionary[newDictionary[j]]!=0):
                result.append(newDictionary[j])
                dictionary[newDictionary[j]]-=1
                size-=1
print(result)