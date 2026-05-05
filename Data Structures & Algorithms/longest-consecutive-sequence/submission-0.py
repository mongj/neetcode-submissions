class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        acc_longest = 0
        for num in nums_set:
            if not num - 1 in nums_set:
                # num can be the start of a new sequence
                curr_longest = 0
                i = 0
                while num + i in nums_set:
                    curr_longest += 1
                    i += 1
                acc_longest = max(acc_longest, curr_longest)
        return acc_longest
                