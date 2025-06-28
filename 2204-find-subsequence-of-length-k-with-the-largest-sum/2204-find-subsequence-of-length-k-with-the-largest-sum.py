class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        arr = []
        for i, num in enumerate(nums):
            arr.append([num, i])
        arr.sort(reverse = True)
        arr = arr[:k]
        arr.sort(key=lambda x: x[1])
        ans = [val[0] for val in arr]
        return ans
        