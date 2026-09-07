class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            max_pile= max(gifts)
            i= gifts.index(max_pile)
            gifts[i]= int(max_pile**0.5)
        return sum(gifts)