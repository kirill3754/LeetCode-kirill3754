class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        line_i = 1
        cur_fill = 0
        for c in s:
            cur_fill += widths[ord(c)-ord('a')]
            if cur_fill > 100:
                line_i += 1
                cur_fill = widths[ord(c)-ord('a')]
        return [line_i, cur_fill]
        