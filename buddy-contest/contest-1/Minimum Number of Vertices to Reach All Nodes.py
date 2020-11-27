from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def child():
            childs = defaultdict(lambda:[])
            
            for edge in edges:
                childs[edge[0]].append(edge[1])
                
            return childs
        
        def dfs(childs,node,curr,visisted):
            found[curr] = node
            
            for i in childs[curr]:
                if i not in visited:
                    visited.add(i)
                    dfs(childs,node,i,visited)
                else:
                    found[i] = node
                
            return count
        
        
        found = [ i for i in range(n)]
        visited = set()
        childs = child()
        
        for i in range(n):
            if i not in visited:
                visited.add(i)
                dfs(childs,i,i,visited)
                
        result = []
        
        for i in range(len(found)):
            if i == found[i]:
                result.append(i)
            
        return sorted(result)
            
