class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        queue = deque()
        queue.append((0,[0]))
        target = len(graph) - 1
        res = []

        while queue:
            node, path = queue.popleft()

            if node == target:
                res.append(path)
                # print(res)
            for i in graph[node]:
                queue.append((i, path + [i]))
        return res