class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        groups = defaultdict(int)
        for i, num in enumerate(nums):
            diff = num-i
            groups[diff] += 1
        good_pairs = 0
        for key, val in groups.items():
            good_pairs += val*(val-1)//2
        all_pairs = len(nums)*(len(nums)-1)//2
        return all_pairs-good_pairs

        