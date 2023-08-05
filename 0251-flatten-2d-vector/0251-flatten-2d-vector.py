class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.v = []
        for r in vec:
            for c in r:
                self.v.append(c)
        self.length = len(self.v)
        self.curr = 0
        

    def next(self) -> int:
        ret = self.v[self.curr]
        self.curr += 1
        return ret

    def hasNext(self) -> bool:
        return self.curr < self.length


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()