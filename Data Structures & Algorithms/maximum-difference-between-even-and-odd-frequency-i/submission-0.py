class Solution:
    def maxDifference(self, s: str) -> int:
        freq = [s.count(c) for c in set(s)]
        odd = [f for f in freq if f % 2 == 1]
        even = [f for f in freq if f % 2 == 0]
        return max(odd) - min(even)