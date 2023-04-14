from collections import deque
import heapq

class GraphAlgo:
    @staticmethod
    def bfs(graph, start):
        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                visited.add(node)
                neighbors = graph[node]
                queue.extend(neighbor for neighbor in neighbors if neighbor not in visited)

        return visited

    @staticmethod
    def dfs(graph, start, visited=None):
        if visited is None:
            visited = set()

        visited.add(start)
        neighbors = graph[start]
        for neighbor in neighbors:
            if neighbor not in visited:
                GraphAlgo.dfs(graph, neighbor, visited)

        return visited

    @staticmethod
    def dijkstra(graph, start, end):
        min_heap = [(0, start)]
        distances = {start: 0}
        visited = set()

        while min_heap:
            cur_dist, cur_node = heapq.heappop(min_heap)

            if cur_node in visited:
                continue
            visited.add(cur_node)

            if cur_node == end:
                return cur_dist

            neighbors = graph[cur_node]
            for neighbor, weight in neighbors.items():
                if neighbor in visited:
                    continue

                new_dist = cur_dist + weight
                if neighbor not in distances or new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    heapq.heappush(min_heap, (new_dist, neighbor))

        return -1
