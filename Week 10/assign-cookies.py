class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        it = iter(sorted(s))
        return sum(any(gi <= si for si in it) for gi in sorted(g))