from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict, deque
        
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        complete_count = 0
        
        
        def bfs(start):
            queue = deque([start])
            component = set()
            
            while queue:
                node = queue.popleft()
                if node in visited:
                    continue
                visited.add(node)
                component.add(node)
                queue.extend(graph[node] - visited)
            
            return component
        
    
        for i in range(n):
            if i not in visited:
                component = bfs(i)
                
            
                k = len(component)
                expected_edges = k * (k - 1) // 2
                actual_edges = sum(len(graph[node]) for node in component) // 2
                
                if actual_edges == expected_edges:
                    complete_count += 1
        
        return complete_count
