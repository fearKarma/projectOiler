row0  = [8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8]
row1  = [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0]
row2  = [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65]
row3  = [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91]
row4  = [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80]
row5  = [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50]
row6  = [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70]
row7  = [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21]
row8  = [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72]
row9  = [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95]
row10 = [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92]
row11 = [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57]
row12 = [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58]
row13 = [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40]
row14 = [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66]
row15 = [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69]
row16 = [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36]
row17 = [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16]
row18 = [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54]
row19 = [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]

rows = 20
cols = 20

grid = [[0 for _ in range(cols)] for _ in range(rows)]

grid[0]  = row0 
grid[1]  = row1 
grid[2]  = row2 
grid[3]  = row3 
grid[4]  = row4 
grid[5]  = row5 
grid[6]  = row6 
grid[7]  = row7 
grid[8]  = row8 
grid[9]  = row9 
grid[10] = row10
grid[11] = row11
grid[12] = row12
grid[13] = row13
grid[14] = row14
grid[15] = row15
grid[16] = row16
grid[17] = row17
grid[18] = row18
grid[19] = row19

def find_greatest_product(nums):
    max_product = 1
    for i in range(len(nums) - 3):
        product = nums[i] * nums[i + 1] * nums[i + 2] * nums[i + 3]
        max_product = max(max_product, product)
    return max_product

# Function to find the greatest product in the entire grid
def find_greatest_product_in_grid(grid):
    max_product = 1

    # Check horizontally
    for row in grid:
        max_product = max(max_product, find_greatest_product(row))

    # Check vertically
    for col in range(len(grid[0])):
        column = [grid[row][col] for row in range(len(grid))]
        max_product = max(max_product, find_greatest_product(column))

    # Check diagonally (from top-left to bottom-right)
    for i in range(len(grid) - 3):
        for j in range(len(grid[0]) - 3):
            diagonal = [grid[i + k][j + k] for k in range(4)]
            max_product = max(max_product, find_greatest_product(diagonal))

    # Check diagonally (from top-right to bottom-left)
    for i in range(3, len(grid)):
        for j in range(len(grid[0]) - 3):
            diagonal = [grid[i - k][j + k] for k in range(4)]
            max_product = max(max_product, find_greatest_product(diagonal))

    return max_product

# Find the greatest product in the grid
greatest_product = find_greatest_product_in_grid(grid)

print("The greatest product of four adjacent digits in the grid is:", greatest_product)


