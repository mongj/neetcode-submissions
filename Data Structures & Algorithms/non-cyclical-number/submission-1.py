class Solution:
    def isHappy(self, n: int) -> bool:
        def getNext(n: int) -> int:
            return sum([int(i)**2 for i in list(str(n))])
        
        fast, slow = n, n
        while fast != 1:
            slow = getNext(slow)
            fast = getNext(getNext(fast))
            if slow == fast:
                return slow == 1
                
        return True
