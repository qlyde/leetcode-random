class Solution:
    def simplifyPath(self, path: str) -> str:
        f = path.split("/")
        canonical = []
        for p in f:
            if not p or p == ".":
                continue
            if p == "..":
                if canonical: canonical.pop()
            else:
                canonical.append(p)
        return "/" + "/".join(canonical)
