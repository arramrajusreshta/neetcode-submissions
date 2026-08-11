class Solution:
    def countBits(self, n: int) -> List[int]:
        rs=[]
        for i in range(n+1):
            rs.append(format(i,'b').count('1'))
        return rs