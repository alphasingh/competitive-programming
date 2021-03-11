"""
https://leetcode.com/problems/battleships-in-a-board/
"""


class Solution:
    @staticmethod
    def isAdjacentToCell(x: int, y: int, cell_row: int, cell_column: int) -> bool:
        is_same = (x == cell_row and y == cell_column)
        is_up = (x == cell_row - 1 and y == cell_column)
        is_down = (x == cell_row + 1 and y == cell_column)
        is_left = (x == cell_row and y == cell_column - 1)
        is_right = (x == cell_row and y == cell_column + 1)
        return is_same or is_up or is_down or is_left or is_right

    @staticmethod
    def isPartOfBattleship(_r: int, _c: int, battleships: dict) -> tuple:
        for k in battleships.keys():
            for cell in battleships[k]:
                if Solution.isAdjacentToCell(_r, _c, cell[0], cell[1]):
                    return k
        return _r, _c

    @staticmethod
    def countBattleships(board: [[str]]) -> int:
        x = 0
        battleships = dict()
        for r, row in enumerate(board):
            for c, cell in enumerate(row):
                if cell == 'X':  # battleship
                    is_part_of_battleship = Solution.isPartOfBattleship(r, c, battleships)
                    if is_part_of_battleship not in battleships:
                        battleships[is_part_of_battleship] = []
                    battleships[is_part_of_battleship].append((r, c))
        return len(battleships)


assert Solution.countBattleships(
    board=[["X", ".", ".", "X"],
           [".", ".", ".", "X"],
           [".", ".", ".", "X"]]) is 2

"""
Input:
X..X
...X
...X
Output:
2
"""
