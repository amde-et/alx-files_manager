class Solution:
    def smallestNumber(self, num: int) -> int:
        s = sorted(str(abs(num)), reverse = num < 0)
        non_zero = next((i for i, n in enumerate(s) if n != '0'), 0)
        s[0], s[non_zero] = s[non_zero], s[0]
        return int(''.join(s)) * (1 if num >= 0 else -1)