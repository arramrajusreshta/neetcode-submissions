class Solution:
    def reverseBits(self, n: int) -> int:
        k=format(n,'032b')
        inverse=k[::-1]
        return int(inverse,2)