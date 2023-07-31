class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #           1    2    3    *
        #           4    5    6
        # ---------------------
        #           7    3    8
        #      6    1    5    0
        # 4    9    2    0    0
        # ---------------------
        # 56088
        if len(num1) < len(num2): return self.multiply(num2, num1)

        ps = []
        zeroes = 0
        for a in range(len(num2) - 1, -1, -1):
            product, carry = "", 0
            for b in range(len(num1) - 1, -1, -1):
                p = int(num2[a]) * int(num1[b]) + carry
                product += str(p % 10)
                carry = p // 10
            if carry:
                product += str(carry)

            ps.append(product[::-1] + "0" * zeroes)
            zeroes += 1
        return str(sum([int(p) for p in ps]))
