class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = []
        i = 0
        while i < len(s):
            cnt = 1
            val = s[i]
            i += 1
            while i < len(s) and s[i] == val:
                cnt += 1
                i += 1
            groups.append(cnt)
        ans = 0
        for i in range(len(groups)-1):
            ans += min(groups[i], groups[i+1])
        return ans

            

        