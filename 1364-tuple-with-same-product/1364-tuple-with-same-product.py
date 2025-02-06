class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        ans = 0
        freq = defaultdict(int)
        for a, b in combinations(nums, 2):
            prod = a*b
            ans+=freq[prod]*8
            freq[prod]+=1
        return ans
            
        