class RecentCounter:
    
    def __init__(self):
        self.queue = []
        

    def ping(self, t: int) -> int:
        self.queue.append(t)
        size=len(self.queue)
        while (  size>0 and self.queue[size-1] < t-3000):
            self.queue.pop()
        return len(self.queue)
        


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
inputs = [[],[1],[100],[3001],[3002]]
param_1 = obj.ping(inputs)
print(param_1)