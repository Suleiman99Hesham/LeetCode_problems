class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        merged_lst = []
        len_nums1 = len(nums1)
        len_nums2 = len(nums2)
        if len_nums1 == 0:
            if len_nums2 % 2 == 0:
                return (nums2[len_nums2//2] + nums2[len_nums2//2 - 1]) / 2
            else:
                return nums2[len_nums2//2]
        elif len_nums2 == 0:
            if len_nums1 % 2 == 0:
                return (nums1[len_nums1//2] + nums1[len_nums1//2 - 1]) / 2
            else:
                return nums1[len_nums1//2]
        i=0
        j= 0
        while i < len_nums1 or j < len_nums2:
            if nums1[i] < nums2[j]:
                merged_lst.append(nums1[i])
                i += 1
            else:
                merged_lst.append(nums2[j])
                j += 1
            
            if i == len_nums1:
                merged_lst.extend(nums2[j:])
                break
            if j == len_nums2:
                merged_lst.extend(nums1[i:])
                break
        if len(merged_lst) % 2 == 0:
            return (merged_lst[len(merged_lst)//2] + merged_lst[len(merged_lst)//2 - 1]) / 2
        else:
            return merged_lst[len(merged_lst)//2]