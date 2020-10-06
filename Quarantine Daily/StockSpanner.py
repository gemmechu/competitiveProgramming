class StockSpanner(object):

    def __init__(self):
        self.mystack = []

    def next(self, price):
        """
        :type price: int
        :rtype: int
        """
        weight = 1
        while self.mystack and self.mystack[-1][0] <= price:
            weight += self.mystack.pop()[1]
        self.mystack.append((price, weight))
        return weight
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
