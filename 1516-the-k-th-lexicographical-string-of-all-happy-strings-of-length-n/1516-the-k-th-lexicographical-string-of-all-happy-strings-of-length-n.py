class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        i = 0
        letters = ['a', 'b', 'c']
        word = ['_']*n
        ans = ''
        def add_letter(word, level):
            nonlocal i, ans
            if level == n:
                i += 1
                if i == k:
                    ans = ''.join(word)
                    return True
                return False
            for letter in letters:
                if level and word[level-1] == letter:
                    continue
                word[level] = letter
                result = add_letter(word, level+1)
                if result:
                    return True
            return False
        add_letter(word, 0)
        return ans