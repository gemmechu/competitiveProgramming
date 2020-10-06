def kthGrammar( N: int, K: int) -> int:
    def kthGrammer_rec(N,result):
        temp = []
        if N == 0:
            return result
        
        for i in range(len(result)):
            if(result[i]==0):
                temp.append(0)
                temp.append(1)
            else:
                temp.append(1)
                temp.append(0)
        
        result = kthGrammer_rec(N-1, temp)
        
        return result
    result = kthGrammer_rec(N-1,[0])
    return result[K-1]

a = kthGrammar(2,1)
print(a)