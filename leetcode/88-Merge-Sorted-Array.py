class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        insertionIndex = len(nums1) - 1
        i = m - 1
        j = n - 1
        while insertionIndex >= 0:
            if j < 0:
                nums1[insertionIndex] = nums1[i]
                i -= 1
            elif i < 0:
                nums1[insertionIndex] = nums2[j]
                j -= 1
            elif nums1[i] > nums2[j]:
                nums1[insertionIndex] = nums1[i]
                i -= 1
            else:
                nums1[insertionIndex] = nums2[j]
                j -= 1
            insertionIndex -= 1

        