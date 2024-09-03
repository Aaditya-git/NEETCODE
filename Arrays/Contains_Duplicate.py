'''
Problem Link : https://neetcode.io/problems/duplicate-integer

Solution :
'''


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dups = []
        for i in range(0, len(nums)):
            if nums[i] in dups:
                return True
            else:
                dups.append(nums[i])
        return False

