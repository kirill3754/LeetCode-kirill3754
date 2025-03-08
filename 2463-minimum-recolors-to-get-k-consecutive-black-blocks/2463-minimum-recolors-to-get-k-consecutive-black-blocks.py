class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        w_n = 0
        for i in range(k):
            if blocks[i] == 'W':
                w_n += 1
        n = len(blocks)
        minw = w_n
        for i in range(n-k):
            if blocks[i+k] == 'W':
                w_n += 1
            if blocks[i] == 'W':
                w_n -= 1
            minw = min(minw, w_n)
        return minw

        