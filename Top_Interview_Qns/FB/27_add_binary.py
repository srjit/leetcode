

class Solution:

    def _sum(self, _n1, _n2, _c):

        sum = int(_n1) + int(_n2) + int(_c)
        return {
            0: ('0', '0'),
            1: ('0', '1'),
            2: ('1', '0'),
            3: ('1', '1')
        }[sum]

    def add_binary(self, a: str, b: str) -> str:

        len_a, len_b = len(a), len(b)
        l = a if len_a > len_b else b
        s = b if a == l else a

        diff = len(l) - len(s)
        s = "".join(['0']* diff) + s

        l, s = l[::-1], s[::-1]
        _c = "0"
        op = ""

        for _l, _s in zip(l, s):
            _c, sum = self._sum(_l, _s, _c)
            op += sum

        if _c == "1":
            op += "1"
        
        return op[::-1]

print(Solution().add_binary("1010", "1011"))