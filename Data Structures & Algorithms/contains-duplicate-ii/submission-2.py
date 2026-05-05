class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = dict()
        for i, num in enumerate(nums):
            if num in seen:
                seen_idx = seen[num]
                for j in seen_idx:
                    if nums[i] == nums[j] and abs(i - j) <= k:
                        return True
                seen[num].append(i)
            else:
                seen[num] = [i]
        return False