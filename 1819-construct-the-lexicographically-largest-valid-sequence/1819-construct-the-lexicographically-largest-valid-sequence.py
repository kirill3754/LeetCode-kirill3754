class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        def insert_number(left_nums, cur_seq, idx):
            nonlocal ans
            if ans:
                return
            if not left_nums:
                ans = cur_seq
            while idx < tot_len and cur_seq[idx] != 0:
                idx += 1
            if idx == tot_len:
                return
            for num in left_nums[::-1]:
                if num == 1:
                    new_seq = cur_seq.copy()
                else:
                    if idx+num >= tot_len or cur_seq[idx+num] != 0:
                        continue
                    new_seq = cur_seq.copy()
                    new_seq[idx+num] = num
                new_seq[idx] = num
                new_nums = left_nums.copy()
                new_nums.remove(num)
                insert_number(new_nums, new_seq, idx+1)

        ans = []

        left_nums = [i for i in range(1, n+1)]
        left_nums = SortedSet(left_nums)
        tot_len = 2*n - 1
        cur = [0]*tot_len

        insert_number(left_nums.copy(), cur.copy(), 0)

        return ans
