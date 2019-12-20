import string

def check(password, hashpassword):
    passwordDict = dict.fromkeys(string.ascii_lowercase, 0)
    hashDict = dict.fromkeys(string.ascii_lowercase, 0)

    for j in password:
        passwordDict[j]+=1
    for k in hashpassword:
        hashDict[k]+=1
  
    temp= list(passwordDict.keys())
  
    for i in temp:
        if((passwordDict.get(i) == hashDict.get(i))== True):
            continue
        else:
            return False

    return True
  
def shuffleHash(password, hashpassword):
    passlen=len(password) 
    hashlen=len(hashpassword) 
    result= False
    if(passlen == hashlen):
        result = check(password,hashpassword)
        
    else:
        if(hashlen<passlen):
            result= False
        else:
            for i in range(hashlen-passlen+1):
                
                result = check(password,hashpassword[i:passlen+i])
                if(result):
                    
                    break
    if(result):
        print("YES")
    else:
        print("NO")
 
size=eval(input())
for i in range(size):
    password =input()
    hashpassword=input()
    shuffleHash(password,hashpassword)