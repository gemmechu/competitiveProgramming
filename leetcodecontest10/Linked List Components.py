from typing import List


class ListNode:
 def __init__(self, x):
     self.val = x
     self.next = None

class Solution:
	def numComponents(self, head: ListNode, G: List[int]) -> int:
		curr = head
		a = []
		while(curr):
			a.append(curr.val)
			curr = curr.next
		t = []
		result = []
		for i in range(len(a)):
			if a[i] not in G:
				if not t:
					pass
				else:
					result.append(t)
					t = []
			else:
				t.append(a[i])
		if t:
			result.append(t)
		return len(result)


head  = ListNode(0)
a  = ListNode(1)
b  = ListNode(2)
c  = ListNode(3)
head.next = a
a.next = b
b.next = c
G = [0,2]
main= Solution()

print(main.numComponents(head, G))

