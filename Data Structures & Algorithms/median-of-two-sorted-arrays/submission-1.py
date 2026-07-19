class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) < len(nums2):
            a, b = nums1, nums2
        else:
            a, b = nums2, nums1
        
        # use binary search to find the number of elements to partition out of array a
        partitionSize = (len(a) + len(b)) // 2
        l, h = 0, len(a)
        while l <= h:
            countFromA = l + (h - l) // 2
            countFromB = partitionSize - countFromA

            aLeft = a[countFromA - 1] if (a and countFromA > 0) else float('-inf')
            aRight = a[countFromA] if (a and countFromA < len(a)) else float('inf')
            bLeft = b[countFromB - 1] if (b and countFromB > 0) else float('-inf')
            bRight = b[countFromB] if (b and countFromB < len(b)) else float('inf')
            if aRight >= bLeft and bRight >= aLeft:
                # find the median
                if (len(a) + len(b)) % 2 == 1:
                    return min(aRight, bRight)
                return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            if aRight < bLeft:
                # take more from A
                l = countFromA + 1
            else:
                # take less from A
                h = countFromA - 1
        
        # this should never be reached
        return -1