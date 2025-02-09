class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        inOutDeg = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            inOutDeg[start] += 1
            inOutDeg[end] -= 1


        startNode = pairs[0][0] 
        for node in inOutDeg:
            if inOutDeg[node] == 1:
                startNode = node
                break

        path = []
        def a(curr):
            while graph[curr]:
                nextNode = graph[curr].pop()
                a(nextNode)
                path.append((curr, nextNode))

        a(startNode)
        return path[::-1]