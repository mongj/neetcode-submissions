class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = path.split("/")
        out = []
        for segment in stack:
            if not segment or segment == ".":
                continue
            if segment == "..":
                if out:
                    out.pop()
            else:
                out.append(segment)
        return "/" + "/".join(out)
