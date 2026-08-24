class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        seen=set()
        for n in nums:
            if n in seen:
                duplicate=n
            seen.add(n)
        for n in range(1, len(nums)+1):
            if n not in seen:
                missing=n
        return[duplicate,missing]