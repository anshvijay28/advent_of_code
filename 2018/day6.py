import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from utils import print_number_table
from collections import defaultdict

def solve2(ids):
    lines = ids.split("\n")

    maxX, maxY = 0, 0
    coords = {}

    # lets keep a map for: coordinate --> [distances from each centroid]

    i = 1
    for line in lines:
        x, y = line.split(",")
        x, y = int(x), int(y)

        if (y, x) not in coords:
            coords[(y, x)] = i  # marked coords as row, col 
            i += 1

        maxX = max(maxX, x)
        maxY = max(maxY, y)

    grid = [[0] * (maxX+1) for _ in range(maxY+1)] 
    M, N = len(grid), len(grid[0])

    # at this point we've constructed the graph, and can simply iterate through every point
    # and calculate if its wihtin region through a simple calc 
    # but there may be an issue in the way we've constructed the grid
    # what if points further bottom right of the furthest centroid are within 10000 of every centroid

    # nvm, it worked. 
    ans = 0
    for r in range(M):
        for c in range(N):
            dist = 0

            for row, col in coords:
                dist += abs(row - r) + abs(col - c)
            
            if dist < 10000:
                ans += 1
    
    return ans



def solve(ids):
    lines = ids.split("\n")

    maxX, maxY = 0, 0
    coords = {}

    # lets keep a map for: coordinate --> [distances from each centroid]
    # distances = defaultdict(list)

    i = 1
    for line in lines:
        x, y = line.split(",")
        x, y = int(x), int(y)

        if (y, x) not in coords:
            coords[(y, x)] = i  # marked coords as row, col 
            i += 1

        maxX = max(maxX, x)
        maxY = max(maxY, y)

    grid = [[0] * (maxX+1) for _ in range(maxY+1)] 
    M, N = len(grid), len(grid[0])

    # now we need to mark every cell in this grid accordingly
    for r in range(M):
        for c in range(N):
            if (r, c) in coords:
                grid[r][c] = coords[(r, c)]
                continue
            # otherwise we need to determine the closest coord, for this (r, c)
            closest = 0
            dist = float("inf")
            matches = 1 

            # iterate through all centroids, to find centroid closest to current point
            for row, col in coords:
                man_dist = abs(row - r) + abs(col - c)  # i think this is correct?
                
                # update distances
                # distances[(r, c)].append([man_dist, (row, col)])

                if man_dist < dist:  # found the smallest
                    dist = man_dist
                    closest = coords[(row, col)]
                    matches = 1  # reset the number of matches
                elif man_dist == dist:
                    matches += 1
            
            # then mark this cell in the grid
            if matches == 1:
                grid[r][c] = closest
            else:
                grid[r][c] = 0
    
    # now iterate across the edges to construct set of bad coords
    invalid = set([0])
    
    for c in range(N):
        invalid.add(grid[0][c])
        invalid.add(grid[M-1][c])
    for r in range(M):
        invalid.add(grid[r][0])
        invalid.add(grid[r][N-1])
    
    # then we can just keep a count
    counts = defaultdict(int)
    for r in range(M):
        for c in range(N):
            counts[grid[r][c]] += 1
    
    # then just find the max vaild island
    max_area = -1

    for code in counts:
        if code in invalid:
            continue
        max_area = max(max_area, counts[code])
    
    return max_area
    
    # GROSSLY OVERCOMPLICATED DAY 6 PART 1
    # print(f"grid after construction")
    # print_number_table(grid)
    # print()
    
    # mark infinite islands as ineligible
    # def mark(r, c, code):
    #     if (
    #         r < 0 or r >= M or 
    #         c < 0 or c >= N or 
    #         (r, c) in visited or 
    #         grid[r][c] != code or
    #         grid[r][c] == 0
    #     ):
    #         return
        
    #     # mark
    #     grid[r][c] = 0
    #     visited.add((r, c))

    #     # recurse
    #     mark(r+1, c, code)
    #     mark(r, c-1, code)
    #     mark(r-1, c, code)
    #     mark(r, c+1, code)

    # for c in range(N):
    #     mark(0, c, grid[0][c]) # mark everything in the first row
    #     mark(M-1, c, grid[M-1][c]) # mark everything in the last row
    
    # for r in range(M):
    #     mark(r, 0, grid[r][0])
    #     mark(r, N-1, grid[r][N-1])

    # print(f"grid after marking")
    # print_number_table(grid)
    # print()

    # find largest eligible island
    # area = 0
    # visited = set()
    # def dfs(r, c, code):
    #     if (
    #         r < 0 or r >= M or 
    #         c < 0 or c >= N or 
    #         (r, c) in visited or
    #         grid[r][c] != code
    #     ):
    #         return 0
        
    #     visited.add((r, c))

    #     return dfs(r+1,c,code)+dfs(r-1,c,code)+dfs(r,c+1,code)+dfs(r,c-1,code)+1       

    # for r in range(M):
    #     for c in range(N):
    #         if grid[r][c] > 0:
    #             area = max(area, dfs(r, c, grid[r][c]))
    
    # return area

test = """1, 1
1, 6
8, 3
3, 4
5, 5
8, 9"""

ids = """355, 246
259, 215
166, 247
280, 341
54, 91
314, 209
256, 272
149, 313
217, 274
299, 144
355, 73
70, 101
266, 327
51, 228
274, 123
342, 232
97, 100
58, 157
130, 185
135, 322
306, 165
335, 84
268, 234
173, 255
316, 75
79, 196
152, 71
205, 261
275, 342
164, 95
343, 147
83, 268
74, 175
225, 130
354, 278
123, 206
166, 166
155, 176
282, 238
107, 295
82, 92
325, 299
87, 287
90, 246
159, 174
295, 298
260, 120
203, 160
72, 197
182, 296"""

print(solve2(ids))

# input pretty small for this one