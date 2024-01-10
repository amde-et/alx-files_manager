class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:

        return sum(map(lambda x: x[0]+x[1] < target,
                       combinations(nums, 2)))