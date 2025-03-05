class Solution:
    def coloredCells(self, n: int) -> int:
        average_n_elements = n * (n - 1) / 2
        total = 1 + average_n_elements * 4
        return int(total)
        