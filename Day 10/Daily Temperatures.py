def dailyTemperatures(T):
    ans = [0]*len(T) 
    stack = []
    
    for i,v in enumerate(T):
        
        while stack and stack[-1][1] < v:
            index,value = stack.pop()
            ans[index] = i - index 
		
        stack.append([i,v])      
    
    return ans
T = [73, 74, 75, 71, 69, 72, 76, 73]

dailyTemperatures(T)