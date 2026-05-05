class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        for i in range(len(temperatures) - 1):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    output[i] = j - i
                    break

        return output

# [2, 1, 1, 3]
# [3, 2, 1, 0]