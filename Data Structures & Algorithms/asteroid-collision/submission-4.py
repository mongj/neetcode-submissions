class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            # always add the first asteroid, it can never collide
            if not stack:
                stack.append(a)
            # two asteroids facing away will never meet
            elif (a > 0 and stack[-1] < 0):
                stack.append(a)
            # two asteroids moving in the same direction will never meet
            elif (a < 0 and stack[-1] < 0) or (a > 0 and stack[-1] > 0):
                stack.append(a)
            # asteroids facing towards each other will collide
            elif a < 0 and stack[-1] > 0:
                # the current asteroid will destroy all previous asteroids
                # which are smaller than it and going in the opp direction
                while stack and stack[-1] > 0 and abs(a) > stack[-1]:
                    stack.pop()
                # check if current asteroid is the same size, if so destroy both
                if stack and stack[-1] > 0 and abs(a) == stack[-1]:
                    stack.pop() # destroy the last asteroid
                    # implicitly destroy a because we don't append it
                elif not stack or stack[-1] < 0:
                    stack.append(a)
        return stack