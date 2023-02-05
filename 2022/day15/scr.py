import getopt, sys
import re

file = ((getopt.getopt(sys.argv[1:], "i:r:")[0])[0])[1]
row  = int(((getopt.getopt(sys.argv[1:], "i:r:")[0])[1])[1])

sensor_beacon_mapping = {}
with open(file) as f:
     for line in f: 
         Sx, Sy, Bx, By = map(int, re.findall('([-0-9]+)', line.strip()))
         sensor_beacon_mapping[(Sx, Sy)] = (Bx, By)

part2_positions_cannot_contain_beacon = set()
positions_cannot_contain_beacon = set()

for coords in sensor_beacon_mapping.items():
    dist = abs(coords[0][1] - coords[1][1]) + abs(coords[0][0] - coords[1][0])
    ydist_from_row = abs(coords[0][1] - row)
    if ( ydist_from_row <= dist):
       xdist_left = dist - ydist_from_row
       for x in range(coords[0][0] - xdist_left, coords[0][0] + xdist_left + 1):
           if ( (x, row) != coords[1] ):
              positions_cannot_contain_beacon.add((x, row))

for coords in sensor_beacon_mapping.items():
    dist = abs(coords[0][1] - coords[1][1]) + abs(coords[0][0] - coords[1][0]) + 1
           
    

print("Part 1:", len(positions_cannot_contain_beacon))
#max_level = max_ht(rock_struct)
#rock_struct2 = rock_struct.copy()
#
#count = 0
#while True:
#    if not fall((500, 0), max_level, rock_struct):
#       break
#    count += 1
#
#print("Part 1:", count)
#
#count = 0
#while True:
#    count += 1
#    if fall_floor((500,0), max_level, rock_struct2) == (500, 0):
#       break
#
#print("Part 2:", count) 
