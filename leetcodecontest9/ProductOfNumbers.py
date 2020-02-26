import math
from functools import reduce

import numpy as np


class ProductOfNumbers:

    def __init__(self):
        self.myList=np.empty([0],dtype=int)

    def add(self, num: int) -> None:
        self.myList= np.append(self.myList*num, num)

    def getProduct(self, k: int) -> int:
        return self.myList[-k]




# Your ProductOfNumbers object will be instantiated and called as such:
obj = ProductOfNumbers()
obj.add(3)
obj.add(2)
obj.add(5)
obj.add(4)
obj.add(2)
param_2 = obj.getProduct(2)
print(param_2)

'''
 def getProduct(self, k: int) -> int:
        product = 1
        if(k<1 or self.myList == []):
            return None
        for i in range(len(self.myList)-1, (len(self.myList)-k)-1,-1 ):
            if(i<0):
                break
            if(self.myList[i]==0):
                return 0
            else:
                product*= self.myList[i]
        return product
'''