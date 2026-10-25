class Solution:
    def specialArray(self, nums: List[int]) -> int:
        for x in range(len(nums) + 1):
            count = 0

            for num in nums:
                if num >= x:
                    count += 1

            if count == x:
                return x

        return -1