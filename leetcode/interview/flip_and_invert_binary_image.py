class Solution:
    @staticmethod
    def flipAndInvertImage(image: [[int]]) -> [[int]]:
        converted = image.copy()
        n = len(image)
        for row in range(n):
            converted[row] = image[row][::-1]  # flip each row
            for column in range(n):
                converted[row][column] = (converted[row][column] + 1) % 2
        return converted


assert Solution.flipAndInvertImage(image=[
    [1, 1, 0],
    [1, 0, 1],
    [0, 0, 0]]) == [[1, 0, 0],
                    [0, 1, 0],
                    [1, 1, 1]]
assert Solution.flipAndInvertImage(image=[[1, 1, 0, 0],
                                          [1, 0, 0, 1],
                                          [0, 1, 1, 1],
                                          [1, 0, 1, 0]]) == [[1, 1, 0, 0],
                                                             [0, 1, 1, 0],
                                                             [0, 0, 0, 1],
                                                             [1, 0, 1, 0]]
