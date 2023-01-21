import getopt, sys

file = ((getopt.getopt(sys.argv[1:], "i:")[0])[0])[1]

def update_coords(dir, dist, current_coords, visited, visited2):
    for num in range(0,dist):
        match dir:
          case "U": (current_coords[0])[1] -= 1
          case "D": (current_coords[0])[1] += 1
          case "L": (current_coords[0])[0] -= 1
          case "R": (current_coords[0])[0] += 1
          case  _ : print("Incorrect dir")   
        for i in range(1,10):
           xdiff, ydiff = tuple(a-b for a,b in zip(current_coords[i-1],current_coords[i]))
           if ((abs(xdiff) > 1) and (abs(ydiff) > 0) or (abs(xdiff) > 0 and abs(ydiff) > 1) ):
              current_coords[i] = list(a+b for a,b in zip(current_coords[i],(xdiff/abs(xdiff), ydiff/abs(ydiff)))) 
           else:
              if (abs(xdiff) > 1 ):
                 (current_coords[i])[0] = (current_coords[i])[0] + (xdiff/abs(xdiff))
              if (abs(ydiff) > 1 ):
                 (current_coords[i])[1] = (current_coords[i])[1] + (ydiff/abs(ydiff))
        visited.add(tuple(current_coords[1]))
        visited2.add(tuple(current_coords[9]))

current_coords = []
visited = set()
visited2 = set()
for i in range(10):
    current_coords.append([0, 0])
with open(file) as f:
     for line in f:
         dir, dist = line.strip().split()
         dist = int(dist)
         update_coords(dir, dist, current_coords, visited, visited2)

print("Part 1:", len(visited))
print("Part 2:", len(visited2))
