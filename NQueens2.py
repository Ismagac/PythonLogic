class Solution:
    def totalNQueens(self, n: int) -> int:
        def backtrack(row: int, cols: set, diagonals: set, anti_diagonals: set) -> int:
            if row == n:
                return 1 

            count = 0
            for col in range(n):
                diag = row - col
                anti_diag = row + col

                if col in cols or diag in diagonals or anti_diag in anti_diagonals:
                    continue 

                cols.add(col)
                diagonals.add(diag)
                anti_diagonals.add(anti_diag)

                count += backtrack(row + 1, cols, diagonals, anti_diagonals)

                cols.remove(col)
                diagonals.remove(diag)
                anti_diagonals.remove(anti_diag)

            return count

        return backtrack(0, set(), set(), set())

solution = Solution()
print(solution.totalNQueens(4))  # 2
print(solution.totalNQueens(1))  # 1
