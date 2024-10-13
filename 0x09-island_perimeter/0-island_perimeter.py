#!usr/bin/python3
"""island_perimetermodule
"""


def island_perimeter(grid):
    """Island perimeter
    """
    rows = len(grid)
    columns = len(grid[0])

    perimeter = 0

    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == 1:
                if i == 0 or grid[i-1][j] == 0:
                    perimeter += 1
                if i == rows-1 or grid[i+1][j] == 0:
                    perimeter += 1
                if j == 0 or grid[i][j-1] == 0:
                    perimeter += 1
                if j == columns-1 or grid[i][j+1] == 0:
                    perimeter += 1

    return perimeter
