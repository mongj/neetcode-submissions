class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]
        
        sub = self.permute(nums[:-1])
        lastNum = nums[-1]
        out = []
        for s in sub:
            for i in range(len(s) + 1):
                sNew = s.copy()
                sNew.insert(i, lastNum)
                out.append(sNew)
        return out