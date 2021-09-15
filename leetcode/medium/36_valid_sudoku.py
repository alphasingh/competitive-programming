"""
https://leetcode.com/problems/valid-sudoku/
"""


class Solution:
    @staticmethod
    def isValidSudoku(board: [[str]]) -> bool:
        def isValidColumn(c):  # c is the start index of the 9 element column
            elements = []
            for r in range(9):
                e = board[r][c]
                if e != '.':
                    elements.append(e)
            # print(elements)
            return len(elements) == len(set(elements))

        def isValidRow(r):  # r is the start index of the 9 element row
            elements = []
            for c in range(9):
                e = board[r][c]
                if e != '.':
                    elements.append(e)
            # print(elements)
            return len(elements) == len(set(elements))

        def isValidBox(r, c):  # r,c is the start position of the 3x3 box
            elements = []
            for ri in range(3):
                for ci in range(3):
                    e = board[r + ri][c + ci]
                    if e != '.':
                        elements.append(e)
            # print(elements)
            return len(elements) == len(set(elements))

        is_valid_sudoku = True
        for column in range(9):
            if not isValidColumn(column):
                is_valid_sudoku = False
                break
        for row in range(9):
            if not isValidRow(row):
                is_valid_sudoku = False
                break
        for row in range(0, 9, 3):
            for column in range(0, 9, 3):
                if not isValidBox(row, column):
                    is_valid_sudoku = False
                    break
        return is_valid_sudoku


assert Solution.isValidSudoku(board=[
    ["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is True
assert Solution.isValidSudoku(board=[
    ["8", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]) is False
"""
Explanation: Same as Example 1, 
except with the 5 in the top left corner being modified to 8. 
Since there are two 8's in the top left 3x3 sub-box, it is invalid.
"""
