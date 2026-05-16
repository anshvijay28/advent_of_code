# wtfffff

def get_presents(text):
    presents = []
    curr = []  # current present

    for i in range(len(text)):
        line = text[i].strip()

        if not line:
            continue

        if ":" in line:            
            if curr:
                presents.append(curr)
            curr = []
            continue
        
        # otherwise we add to this present
        row = []
        for j in range(len(line)):            
            row.append(1 if line[j] == "#" else 0)
        curr.append(row)
    
    # add last present
    if len(curr) > 0:
        presents.append(curr)

    return presents
                

def get_requirnments(text):
    # lets make it a list where each element is [size, list of amount of each present]
    reqs = []

    for i in range(len(text)):
        line = text[i].strip()
        if not line:
            continue
            
        size, presents = line.split(":")
        cols, rows = [int(num) for num in size.split("x")]
        
        # process amounts
        presents = presents.split(" ")
        amounts = []

        for amount in presents:
            if not amount:
                continue
            amounts.append(int(amount))
        
        reqs.append([rows, cols, amounts])
    
    return reqs

def split_input(text):
    lines = text.split("\n")
    idx = 0

    while idx < len(lines):
        if "x" in lines[idx]:
            return lines[:idx], lines[idx:]
        
        idx += 1
    
    return []

def placeBlock(block, row, col, area):
    """
    Returns whether or not a present can fit in the given area
    """

    result_area = area

    return False, result_area

def unplaceBlock(block, area):
    # remove the block from the area
    return area


def process_req(req, presents):
    """
    This function will see if a certain area, can house all the presents
    """

    # I don't think its as simple as iteratively placing each present in each area. its most likely a backtracking solution of sorts. For every position in the grid, see if you can place a block there. To see if you can place a block in a position, try all 4 rotations

    # once you've found a orientation that works, move onto the next block
    # if that doesn't work, backtrack

    rows, cols, amounts = req
    space = [[0] * cols for _ in range(rows)]

    def dfs(curr_space, idx):
        if idx == len(amounts):
            return True

        # iterate through amounts
        for i, amount in enumerate(amounts):
            # try to place this block at every row and col in the area
            block = presents[i]

            for row in range(rows):
                for col in range(cols):
                    if space[row][col] == 1: continue

                    # otherwise its free space
                    result, new_space = placeBlock(block, row, col, space)

                    if result:
                        return dfs(new_space, idx+1)
            
            # if we have made it here that means we were unable to place this block anywhere, as such we need to backtrack

            # unplace presents[i]
            new_space = unplaceBlock(block, curr_space)






text = """
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

top, bottom = split_input(text)

presents = get_presents(top)
reqs = get_requirnments(bottom)


