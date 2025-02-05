class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        n_diff = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2:
                n_diff += 1
                if n_diff > 2:
                    return False
                elif n_diff == 1:
                    a = c1
                    b = c2
                elif n_diff == 2:
                    if a != c2 or b != c1:
                        return False
        if n_diff == 0 or n_diff == 2:
            return True
        return False

            
        