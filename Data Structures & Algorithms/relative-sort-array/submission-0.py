class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result = []

        for num in arr2:
            result.extend([num] * arr1.count(num))

        remaining = sorted(num for num in arr1 if num not in arr2)

        return result + remaining