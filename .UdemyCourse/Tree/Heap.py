class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
    def build_heap(self):
        pass
    # O(n)
    def insert_item(self, item):
        self.heapList.append(item)
        self.currentSize += 1
        self.perc_up()

    def delete_item(self, item):

        pass
    def print_heap(self):
        print(self.heapList)
    def perc_up(self):
        #if item > parent heapify
        i = self.currentSize
        while i//2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                # swap(i, i//2)
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[i//2]
                self.heapList[i//2] = temp
            i //= 2

heap = BinHeap()
heap.insert_item(5)
heap.insert_item(9)
heap.insert_item(11)
heap.insert_item(14)
heap.insert_item(18)
heap.insert_item(19)
heap.insert_item(21)
heap.insert_item(33)
heap.insert_item(17)
heap.insert_item(27)
heap.insert_item(7)



heap.print_heap()
