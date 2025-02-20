class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])
        check = [0]*2**n
        for num in nums:
            int_num = int(num, 2)
            check[int_num] = 1
        for i in range(len(check)):
            if check[i] == 0:
                ans = str(bin(i))[2:]
                while len(ans) < n:
                    ans = '0' + ans
                return ans
        return -1
        