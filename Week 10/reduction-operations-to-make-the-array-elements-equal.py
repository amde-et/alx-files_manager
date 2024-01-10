class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        return sum([i*cnt for i, (num, cnt) in enumerate(sorted(Counter(nums).items()))])