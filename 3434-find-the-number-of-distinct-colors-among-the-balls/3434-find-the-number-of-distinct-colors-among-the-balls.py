class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colored_balls = {}
        colors = defaultdict(int)
        res = []
        for ball, color in queries:
            if ball in colored_balls:
                colors[colored_balls[ball]]-=1
                if colors[colored_balls[ball]] == 0:
                    del colors[colored_balls[ball]]
            colored_balls[ball] = color
            colors[color]+=1
            res.append(len(colors))
        return res


        