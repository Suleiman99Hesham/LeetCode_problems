class Solution:
    def intersect(self, nums1, nums2):
        result=[]
        if len(nums1) <= len(nums2):
            x = len(nums1)
            y = 1
        else:
            x = len(nums2)
            y = 2
        for i in range(x):
            if y == 1:
                if nums1[i] in nums2:
                    nums2.pop(nums2.index(nums1[i]))
                    result.append(nums1[i])
            else:
                if nums2[i] in nums1:
                    nums1.pop(nums1.index(nums2[i]))
                    result.append(nums2[i])
        return result