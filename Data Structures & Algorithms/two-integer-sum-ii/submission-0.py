class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        for i in range(n - 1):
            for j in range(1, n):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]
        return [0, 0] # should never reach here