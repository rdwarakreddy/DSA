class Solution(object):
    def validPath(self, edges, source, destination):
        adj = {}
        for i in edges:
            v1, v2 = i
            if v1 not in adj:
                adj[v1] = []
            if v2 not in adj:
                adj[v2] = []
            adj[v1].append(v2)
            adj[v2].append(v1)
        visited = set()
        visited.add(source)
        queue = [source]
        while queue:
            current_vertex = queue.pop(0)
            if current_vertex == destination:
                return True
            for i in adj[current_vertex]:
                if i not in visited:
                    visited.add(i)
                    queue.append(i)
        return False


edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2
sol = Solution()
print(sol.validPath(edges, source, destination))
