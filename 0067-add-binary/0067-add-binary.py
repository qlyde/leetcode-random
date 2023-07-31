class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) > len(b): return self.addBinary(b, a)
        ret, c = "", 0
        for i in range(max(len(a), len(b))):
            ia = len(a) - 1 - i
            ib = len(b) - 1 - i
            da = int(a[ia]) if ia >= 0 else 0
            db = int(b[ib]) if ib >= 0 else 0
            s = da + db + c
            c = s // 2
            ret = str(s % 2) + ret
        if c: return '1' + ret
        return ret

