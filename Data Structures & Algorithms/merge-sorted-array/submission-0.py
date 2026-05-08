class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        t = [0] * (m + n)

        # merge
        target = 0
        i = j = 0
        while i < m or j < n:
          if (i < m and j < n and nums1[i] < nums2[j]) or j >= n:
            t[target] = nums1[i]
            i += 1
          else:
            t[target] = nums2[j]
            j += 1
          target += 1 

        # copy over to nums1
        for i, n in enumerate(t):
          nums1[i] = n
    