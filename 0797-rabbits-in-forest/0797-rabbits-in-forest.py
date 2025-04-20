class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        cnt = {}
        for answer in answers:
            if answer in cnt:
                cnt[answer] += 1
            else:
                cnt[answer] = 1
        ans = 0
        for key, val in cnt.items():
            n = key + 1
            n_groups = val // n
            if val % n:
                n_groups += 1
            ans += n_groups * n
        return ans

        