class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        start_i = end_i = 0
        max_avg = float('-inf')
        window_sum = nums[0]

        if len(nums) == 1:
            return nums[0]
        
        if k == 1:
            return max(nums)

        for i in range(1, len(nums)):
            end_i += 1
            window_sum += nums[i]
            if (end_i - start_i + 1) >= k:
                window_avg = window_sum / k
                if window_avg > max_avg:
                    max_avg = window_avg
                window_sum -= nums[start_i]
                start_i += 1

        return max_avg