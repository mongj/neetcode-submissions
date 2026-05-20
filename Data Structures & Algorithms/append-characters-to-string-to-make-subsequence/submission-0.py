class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        sp = tp = 0
        # finish consuming either s/t -> return len(t) - tp
        while tp < len(t):
            while sp < len(s) and tp < len(t) and s[sp] != t[tp]:
                sp += 1
            if sp == len(s) or tp == len(t):
                break
            tp += 1
            sp += 1
        return len(t) - tp
