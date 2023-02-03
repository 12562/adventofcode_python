import getopt, sys

file = ((getopt.getopt(sys.argv[1:], "i:")[0])[0])[1]

def build(line, rock_structure: set):
    nodes = [ (int(i), int(j)) for l in line.split(" -> ") for (i, j) in [l.split(",")] ]
    for i in range(1, len(nodes)):
        if nodes[i][0] == nodes[i-1][0]:
           for j in range(min(nodes[i-1][1], nodes[i][1]), max(nodes[i-1][1], nodes[i][1]) + 1):
               rock_structure.add((nodes[i][0], j))
        else:
           for j in range(min(nodes[i-1][0], nodes[i][0]), max(nodes[i-1][0], nodes[i][0]) + 1):
               rock_structure.add((j, nodes[i][1]))

def max_ht(rock_structure):
    res = 0
    for _, i in rock_structure:
        res = max(res, i)
    return res

def fall(start, threshold, grid):
    coords = start
    while True:
       if (coords[0], coords[1] + 1) not in grid:
          coords = (coords[0], coords[1] + 1)
       elif (coords[0] - 1, coords[1] + 1) not in grid:
          coords = (coords[0] - 1, coords[1] + 1)
       elif ( coords[0] + 1, coords[1] + 1) not in grid:
          coords = (coords[0] + 1, coords[1] + 1)
       else:
          grid.add(coords)
          return True
       
       if coords[1] >= threshold:
          return False

def fall_floor(start, threshold, grid):
    coords = start
    while True:
       if coords[1] + 1 == threshold + 2:
          grid.add(coords)
          return coords
       
       if (coords[0], coords[1] + 1) not in grid:
          coords = (coords[0], coords[1] + 1)
       elif (coords[0] - 1, coords[1] + 1) not in grid:
          coords = (coords[0] - 1, coords[1] + 1)
       elif ( coords[0] + 1, coords[1] + 1) not in grid:
          coords = (coords[0] + 1, coords[1] + 1)
       else:
          grid.add(coords)
          return True
          
rock_struct = set()
with open(file) as f:
     for line in f: 
         build(line.strip(), rock_struct)

max_level = max_ht(rock_struct)
rock_struct2 = rock_struct.copy()

count = 0
while True:
    if not fall((500, 0), max_level, rock_struct):
       break
    count += 1

print("Part 1:", count)

count = 0
while True:
    count += 1
    if fall_floor((500,0), max_level, rock_struct2) == (500, 0):
       break

print("Part 2:", count) 
