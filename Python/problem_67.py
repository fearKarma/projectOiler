"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

					3
				   7 4
				  2 4 6
				 8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), 
a 15K text file containing a triangle with one-hundred rows.

"""
                                    
# Read the triangle from the text file into a 2D list
triangle = []
with open('triangle.txt', 'r') as file:
    for line in file:
        triangle.append([int(num) for num in line.split()])

# Create a dynamic programming table
table = [row[:] for row in triangle]

# Initialize the table with the values from the first row of the triangle
for j in range(1, len(triangle[0])):
    table[0][j] += table[0][j-1]

# Update the table
for i in range(1, len(triangle)):
    for j in range(len(triangle[i])):
        if j == 0:
            table[i][j] += table[i-1][j]
        elif j == len(triangle[i]) - 1:
            table[i][j] += table[i-1][j-1]
        else:
            table[i][j] += max(table[i-1][j-1], table[i-1][j])

# Find the maximum total from top to bottom
max_total = max(table[-1])

print("Maximum total from top to bottom:", max_total)