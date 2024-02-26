'''An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with color.

Return the modified image after performing the flood fill.'''

def pretty_print(matrix):
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            print(matrix[r][c], end='')
        print()

def flood_fill_helper(image, sr, sc, start_color, color):
    # Base case returns if cell is not the same as start color
    if image[sr][sc] != start_color:
        return
    # Assign cell to the new color
    image[sr][sc] = color
    # Recurse over neighbors
    for r, c in [(sr - 1, sc), (sr + 1, sc), (sr, sc - 1), (sr, sc + 1)]:
        if 0 <= r < len(image) and 0 <= c < len(image[0]):
            flood_fill_helper(image, r, c, start_color, color)

def flood_fill(image, sr, sc, color):
    # Determine starting cell's color and return image if it's the same as our color param
    start_color = image[sr][sc]
    if start_color == color:
        return image
    flood_fill_helper(image, sr, sc, start_color, color)
    return image

# TESTS

image1 = [[1,1,1],[1,1,0],[1,0,1]]
image2 = [[0,0,0],[0,0,0]]
pretty_print(image1)
print('\n')
pretty_print(flood_fill(image1, 1, 1, 2))
print('\n')
pretty_print(image2)
print('\n')
pretty_print(flood_fill(image2, 0, 0, 0))
