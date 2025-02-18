class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n = len(pattern)
        digits = [i+1 for i in range(n + 1)]
        digits = SortedSet(digits)
        print(digits)
        def select_digit(digits, position, cur):
            for digit in digits:
                if cur:
                    if pattern[position] == 'I' and digit < cur[-1]:
                        continue
                    if pattern[position] == 'D' and digit > cur[-1]:
                        continue
                if position == n-1:
                    cur.append(digit)
                    return ''.join(map(str, cur))
                new_digits = digits.copy()
                new_digits.remove(digit)
                new_cur = cur.copy()
                new_cur.append(digit)
                result = select_digit(new_digits, position+1, new_cur)
                if result:
                    return result
            return None
        return select_digit(digits, -1, [])
        