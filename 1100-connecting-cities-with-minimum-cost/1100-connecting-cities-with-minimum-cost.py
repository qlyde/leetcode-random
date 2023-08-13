class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        g = collections.defaultdict(list)
        for [x, y, w] in connections:
            g[x].append((y, w))
            g[y].append((x, w))

        ret = 0
        visited = set()
        heap = [(0, 1, -1)]
        heapq.heapify(heap)
        while heap:
            weight, vertex, source = heapq.heappop(heap)
            if vertex not in visited:
                visited.add(vertex)
                if source != -1:
                    ret += weight
                
                for neighbour, edgeWeight in g[vertex]:
                    if neighbour not in visited:
                        heapq.heappush(heap, (edgeWeight, neighbour, vertex))
        
        return ret if len(visited) == n else -1

