class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        word = "balloon"
        count = {}

        for ch in word:
            count[ch] = text.count(ch)

        count['l'] //= 2
        count['o'] //= 2

        return min(count.values())