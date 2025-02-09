class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p and not s:
            return True
        if not p:
            return False
        new_p = p[0]
        for i in range(1, len(p)):
            if p[i-1] == '*' and p[i] == '*':
                pass
            else:
                new_p += p[i]
        p = new_p
        sn = len(s)
        pn = len(p)
        #print(s,'\n', p)
        i = j = 0
        star = -1
        while i<sn:
            if j < pn and (s[i] == p[j] or p[j] == '?'):
                i += 1
                j += 1
            elif j < pn and p[j] == '*':
                star = j
                j += 1
                last_match = i
                
            elif star >= 0:
                j = star + 1
                i = last_match + 1
                last_match += 1
            else:
                return False
        while j<pn and p[j] == '*':
            j+=1
        return j == pn


        
        

        