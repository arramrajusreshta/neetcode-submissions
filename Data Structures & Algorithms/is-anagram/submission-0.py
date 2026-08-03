class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if lengths differ, they can't be anagrams
        if len(s) != len(t):
            return False

        count1 = {}
        count2 = {}

        # count frequency of each character in s
        for i in s:
            count1[i] = count1.get(i, 0) + 1

        # count frequency of each character in t
        for j in t:
            count2[j] = count2.get(j, 0) + 1

        # compare the two dictionaries
        return count1 == count2
