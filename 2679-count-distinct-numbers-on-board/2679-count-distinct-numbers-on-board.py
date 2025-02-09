class Solution:
    def distinctIntegers(self, n: int) -> int:
        all_numbers = {n}
        added_numbers = all_numbers.copy()
        while added_numbers:
            new_numbers = set()
            for x in added_numbers:
                for i in range(1, min(n, x)):
                    if i not in all_numbers and x%i==1:
                        new_numbers.add(i)
                        all_numbers.add(i)
            added_numbers = new_numbers.copy()
        return len(all_numbers)



        