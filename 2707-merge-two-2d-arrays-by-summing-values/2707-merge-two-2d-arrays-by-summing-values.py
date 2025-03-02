class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        ans = []
        while i<n1 and j<n2:
            id1 = nums1[i][0]
            id2 = nums2[j][0]
            if id1 == id2:
                ans.append([id1, nums1[i][1] + nums2[j][1]])
                i += 1
                j += 1
            elif id1 < id2:
                ans.append([id1, nums1[i][1]])
                i += 1
            else:
                ans.append([id2, nums2[j][1]])
                j += 1
        while i<n1:
            id1 = nums1[i][0]
            ans.append([id1, nums1[i][1]])
            i += 1
        while j<n2:
            id2 = nums2[j][0]
            ans.append([id2, nums2[j][1]])
            j += 1
        return ans


