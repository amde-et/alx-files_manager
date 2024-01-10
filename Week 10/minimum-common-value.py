class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        while len(nums1)>0 and len(nums2)>0:
            if nums1[0]==nums2[0]:
                return nums1[0]
            elif nums1[0]<nums2[0]:
                nums1.pop(0)
            else:
                nums2.pop(0)
        return -1