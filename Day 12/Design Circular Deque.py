class MyCircularDeque:
    def __init__(self, k):
        self.k = k
        self.q = []
    def insertFront(self, value):
        if len(self.q)< self.k:
            self.q.insert(0,value)
            return True
        return False
    def insertLast(self, value):
        if len(self.q) < self.k:
            self.q.append(value)
            return True
        return False
    def deleteFront(self):
        if(len(self.q)>0):
            self.q.pop(0)
            return True
        return False
    def deleteLast(self):
        if (len(self.q) > 0):
            self.q.pop()
            return True
        return False
    def getFront(self):
        if (len(self.q) > 0):
            return self.q[0]
        return -1
    def getRear(self):
        if (len(self.q) > 0):
            return self.q[-1]
        return -1
    def isFull(self):
        return len(self.q) == self.k