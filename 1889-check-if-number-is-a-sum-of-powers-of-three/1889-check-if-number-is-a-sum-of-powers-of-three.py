class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        comp = [1]
        i = 1
        candidate = 3**i
        while candidate <= n:
            comp.append(candidate)
            i += 1
            candidate = 3**i
        comp = comp[::-1]
        def check(comp, n, i, cur_sum):
            if cur_sum == n:
                return True
            if i >= len(comp) or cur_sum > n:
                return False
            return check(comp, n, i+1, cur_sum) or check(comp, n, i+1, cur_sum + comp[i])
        return check(comp, n, 0, 0)
        