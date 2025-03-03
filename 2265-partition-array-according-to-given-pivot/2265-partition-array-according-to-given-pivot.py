class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        nums1 = []
        nums2 = 0
        nums3 = []
        for n in nums:
            if n < pivot:
                nums1.append(n)
            elif n > pivot:
                nums3.append(n)
            else:
                nums2 += 1
        return nums1 + [pivot] * nums2 + nums3
        