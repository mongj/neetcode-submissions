class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest_seq_len = 0
        for num in nums:
            if num - 1 not in numset:
                # num is the start of a sequence
                seq_len = 1
                while num + 1 in numset:
                    num += 1
                    seq_len += 1
                longest_seq_len = max(longest_seq_len, seq_len)
        return longest_seq_len