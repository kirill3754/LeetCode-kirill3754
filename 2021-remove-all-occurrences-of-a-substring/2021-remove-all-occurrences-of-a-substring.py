class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        removed = True
        m = len(part)
        while removed:
            removed = False
            i = 0
            n = len(s)
            j = 0
            while i<n and j<m:
                if j==0:
                    st = i
                if s[i] == part[j]:
                    j+=1
                    if j==m:
                        s = s[:i-m+1]+s[i+1:]
                        removed = True
                        i = 0
                        j = 0
                        break
                else:
                    i = st
                    j = 0
                i+=1
        return s

        