class Solution:
    def isHappy(self, n: int) -> bool:
        seen = {n}
        while n != 1:
            n = sum([int(i)**2 for i in list(str(n))])
            if n in seen:
                return False
            seen.add(n)
        
        return True