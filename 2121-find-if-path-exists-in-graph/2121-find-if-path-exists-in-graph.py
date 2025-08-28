class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = collections.defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(n, v):
            if n == destination:
                return True
            v.add(n)
            for ne in graph[n]:
                if ne not in v:
                    if dfs(ne,v):
                        return True
            return False
        v = set()
        return dfs(source,v)