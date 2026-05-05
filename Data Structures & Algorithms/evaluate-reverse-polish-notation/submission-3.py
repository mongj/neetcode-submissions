class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        available_ops = ["+", "-", "*", "/"]

        def calculate(op: str, left: int, right: int) -> int:
            if op == "+":
                return left + right
            elif op == "-":
                return left - right
            elif op == "*":
                return left * right
            else:
                return int(left / right)

        num_stack = []
        for token in tokens:
            if token in available_ops:
                right = num_stack.pop()
                left = num_stack.pop()
                num_stack.append(calculate(token, left, right))
            else:
                num_stack.append(int(token))

        return num_stack[0]
