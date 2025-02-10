class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        ans = 0
        cur = 0
        for i in range(len(sequence)):
            j = 0
            while i+j<len(sequence) and sequence[i+j]==word[j%len(word)]:
                j+=1
            ans=max(ans,j//len(word))
        return ans
            

        