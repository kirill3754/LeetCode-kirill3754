class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        edges_dict = [set() for i in range(n)]
        #print(edges_dict)
        for s, f in edges:
            edges_dict[s].add(f)
            edges_dict[f].add(s)
        #print(edges_dict)
        path = [0]
        ans = 0
        while path:
            #print('___________')
            #print(path)
            #print(edges_dict)
            node = path[-1]
            if not edges_dict[node]:
                #print('if', node, values[node])
                if values[node] % k == 0:
                    path.pop()
                    ans+=1
                else:
                    path.pop()
                    values[path[-1]] += values[node] % k
            else:
                next_node = edges_dict[node].pop()
                edges_dict[next_node].discard(node)
                #print('else', next_node)
                path.append(next_node)
        return ans
                



        