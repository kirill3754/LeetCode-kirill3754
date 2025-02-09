class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        nums.append(0)
        for i in range(n):
            if nums[i] < 1 or nums[i] > n:
                nums[i] = 0
        #print(nums, '\n')
        for i in range(n):
            j = i
            val = 0
            while nums[j] != j and nums[j] > 0:
                #print(nums, nums[j], j, val)
                next_val = nums[j]
                nums[j] = val
                val = next_val
                j = next_val
            if val:
                nums[j] = val
        #print(nums)
        for i in range(1, n + 1):
            if not nums[i]:
                return i

        return n + 1


        