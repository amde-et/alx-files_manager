class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        space = [['e' for _ in range(n)] for _ in range(m)]
        empty = m*n - len(guards) - len(walls)
        for guard in guards:
            space[guard[0]][guard[1]] = 'o'

        for wall in walls:
            space[wall[0]][wall[1]] = 'o'

        def walk(r, c):
            for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                row, col = r + dy, c + dx

                while row >= 0 and row < m and col >= 0 and col < n:
                    if space[row][col] == 'e':
                        space[row][col] = 'g'
                        nonlocal empty
                        empty -= 1
                    elif space[row][col] == 'o':
                        break
                    row, col = row + dy, col + dx

        for guard in guards:
            walk(guard[0], guard[1])

        return empty