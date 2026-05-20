class Solution:
    def countSeniors(self, details: List[str]) -> int:
        def getAge(detail: str) -> int:
            return int(detail[-4:-2])
        return len(list(filter(lambda d: getAge(d) > 60, details)))