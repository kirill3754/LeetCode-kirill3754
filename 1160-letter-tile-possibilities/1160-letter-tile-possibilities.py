class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        d = dict(Counter(tiles))
        ans = -1
        def append_letter(d):
            nonlocal ans
            ans += 1
            if not d:
                return
            for key, val in d.items():
                new_d = d.copy()
                if val > 1:
                    new_d[key] = val - 1
                else:
                    del new_d[key]
                append_letter(new_d)
        append_letter(d)
        return ans
        