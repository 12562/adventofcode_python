import getopt, sys
from collections import deque
file = ((getopt.getopt(sys.argv[1:], "i:")[0])[0])[1]

num_rows = sum(1 for line in open(file))
heightmap = []
source = 0
dest = 0
with open(file) as f:
     for line in f: 
         line = list(line.strip())
         if not heightmap:
            num_cols = len(line)
         heightmap += line
         
def find_shortest_path(part, heightmap):
    source = [heightmap.index("S"), 0] if part == 1 else [heightmap.index("E"), 0]
    dest = [heightmap.index("E")] if part == 1 else [i for i,d in enumerate(heightmap) if d == "a" or d == "S"]
    heightmap = [ord(i) for i in heightmap]

    q = deque()
    q.append(source)
    visited = [] 
    while(q):
      current_index, current_dist = q.popleft()
      if current_index in dest:
         break
      visited.append(current_index)
      match heightmap[current_index]:
            case 83 : current = ord("a")
            case 69 : current = ord("z")
            case _:        current = heightmap[current_index]
      
      possible_neighbors = [current_index - 1, current_index + 1, current_index - num_cols, current_index + num_cols] 
      true_neighbors = []
      for neighbor in possible_neighbors:
         if ( (neighbor <= 0) or (neighbor >= len(heightmap)) or ([neighbor, current_dist+1] in q) or (neighbor in visited) ):
            continue
         else:
            
            
            match heightmap[neighbor]:
                  case 83 : neigh = ord("a")
                  case 69 : neigh = ord("z")
                  case _:    neigh = heightmap[neighbor]       
            true_neighbors.append([neighbor, current_dist + 1]) if (neigh <= current + 1) and (part == 1) else None
            true_neighbors.append([neighbor, current_dist + 1]) if (neigh >= current - 1) and (part == 2) else None
      q.extend(true_neighbors) if true_neighbors != [] else None
    return current_dist 

        
print("Part 1:", find_shortest_path(1, heightmap))
print("Part 2:", find_shortest_path(2, heightmap))
