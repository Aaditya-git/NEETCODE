'''
https://neetcode.io/problems/two-integer-sum
Solution
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        braces = []
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if ((nums[i] + nums[j] == target) and i != j):
                    braces.append(i)
                    braces.append(j)

        return braces


