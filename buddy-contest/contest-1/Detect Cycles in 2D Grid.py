class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def bound(node):
            return 0 <= node[0] < len(grid) and 0 <= node[1] < len(grid[0])
        
        def dfs(node,x):
            moves = [(0,1),(1,0),(-1,0),(0,-1)]
            
            for i in range(len(moves)):
                move = moves[i]
                new =  node[0] + move[0],node[1] + move[1]
                
                if not bound(new) or new == x:
                    continue

                if new in visited and grid[node[0]][node[1]]  == grid[new[0]][new[1]]:
                    return True
                else:
                    if grid[node[0]][node[1]]  == grid[new[0]][new[1]]:
                        visited.add(new)
                        result = dfs(new, node)
                        if result:
                            return True           
            return False
                        
                
                
            
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in visited:
                    origin = (i,j)
                    visited.add(origin)
                    result = dfs((i,j),9)
                    if result:
                        return True
        return False
