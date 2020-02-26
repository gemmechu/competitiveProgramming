
# Employee info
from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        if len(employees)<1:
            return 0
        q = []
        mydict = {}
        for i in range(len(employees)):
            mydict[employees[i].id] = employees[i]
        result = 0
        visited = []
        q.append(mydict.get(id))

        while len(q) > 0:
            current = q.pop(0)
            if(current not in visited):
                result += current.importance
                visited.append(current)
            for i in range(len(current.subordinates)):
                subordinate_id = current.subordinates[i]
                if mydict.get(subordinate_id) not in q and mydict.get(subordinate_id) not in visited:
                    q.append(mydict.get(subordinate_id))
        return result


[[1,5,[2,3]],[2,3,[]],[3,3,[]]]


d= Employee(2,5,[])
a =Employee(1,5,[2,3])
b =Employee(2,3,[1])
c =Employee(3,7,[])
main = Solution()
print(main.getImportance([a,b,c],1))

