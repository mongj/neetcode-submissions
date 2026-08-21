class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numFreqMap = {}
        for num in nums1:
            numFreqMap[num] = numFreqMap.get(num, 0) + 1
        
        res = []
        for num in nums2:
            if num in numFreqMap and numFreqMap[num] > 0:
                res.append(num)
                numFreqMap[num] -= 1
        
        return res