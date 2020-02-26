class Solution:
    def __init__(self):
        self.queue=[]
        pass
    def ping(self,t: int)-> int:
        self.queue.append(t)
        temp=[]
        for item in self.queue:
            if item < t - 3000:
                temp.append(item)
        self.queue=temp
        return len(self.queue)
