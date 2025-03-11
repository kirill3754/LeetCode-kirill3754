class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def check_contain_letters(i, j):
            for letter in letters:
                if cnt[j][letter]-cnt[i][letter] == 0:
                    return False
            return True
        
        n = len(s)
        letters = 'abc'
        d = {letter: 0 for letter in letters}
        cnt = [d.copy()]
        # print(d)
        for c in s:
            if c in letters:
                d[c] += 1
            else:
                return -1
            # print(d)
            cnt.append(d.copy())
        i, j, ans = 0, 3, 0
        for i in range(n-1):
            while j <= n and not check_contain_letters(i, j):
                j += 1
            if j > n:
                break
            # print(f'i={i}, j={j}')
            ans += n+1-j
        return ans
