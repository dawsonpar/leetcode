from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # do binary search on rows in matrix
        # if target is not in rows return False

        # do binary search in row with target
        # if target is not in row return False
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        while top <= bot:
            middleRow = (top + bot) // 2
            if target > matrix[middleRow][-1]:
                top = middleRow + 1
            elif target < matrix[middleRow][0]:
                bot = middleRow - 1
            else:
                break

        if not (top <= bot):
            return False

        middleRow = (top + bot) // 2
        l, r = 0, cols - 1
        while l <= r:
            m = (l + r) // 2
            if target > matrix[middleRow][m]:
                l = m + 1
            elif target < matrix[middleRow][m]:
                r = m - 1
            else:
                return True
        return False
