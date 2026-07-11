class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        while i >= 0:
            d = digits[i] + 1
            carry = d // 10
            remainder = d % 10

            digits[i] = remainder
            if carry == 0:
                return digits
            elif i == 0:
                return [1] + digits
                
            i -= 1