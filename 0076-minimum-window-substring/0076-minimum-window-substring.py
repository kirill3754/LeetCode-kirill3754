class Solution:
    

    def minWindow(self, s: str, t: str) -> str:
        def not_zero(t_dict):
            return max(v for v in t_dict.values()) > 0

        m = len(s)
        n = len(t)
        t_dict = Counter(t)

        p1 = 0
        t_dict[s[p1]] -= 1
        p2 = 1

        min_len = m + 1
        ans = ''

        while p1 < m and p2 < m:
            if not_zero(t_dict):
                t_dict[s[p2]] -= 1
                p2 += 1
            else:
                cur_len = p2 - p1
                if cur_len < min_len:
                    min_len = cur_len
                    min_p2 = p2
                    min_p1 = p1
                t_dict[s[p1]] += 1
                p1 += 1

        while p1 < m and not not_zero(t_dict):
            cur_len = p2 - p1
            if cur_len < min_len:
                min_len = cur_len
                min_p2 = p2
                min_p1 = p1
            t_dict[s[p1]] += 1
            p1 += 1



        if min_len == m + 1:
            return ''
        return s[min_p1:min_p2]

        