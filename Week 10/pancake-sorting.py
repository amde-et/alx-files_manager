class Solution:
    def pancakeSort(self, arr):
        def dfs(end):
            start = 0

            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

            return arr

        n, stack = len(arr), []

        for i in range(n-1,-1,-1):
            max_ = i

            for j in range(i,-1,-1):
                if arr[j] > arr[max_]: max_ = j

            if max_ != i:
                dfs(max_)
                dfs(i)
                stack.append(max_+1)
                stack.append(i+1)

        return stack







        