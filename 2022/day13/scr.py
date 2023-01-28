import json
import getopt, sys
import functools

file = ((getopt.getopt(sys.argv[1:], "i:")[0])[0])[1]

def check(l, r):
    if ( type(l) is int ) and ( type(r) is int ):
       if l < r:
          return -1
       elif l > r:
          return 1
       else:
          return 0
    
    if type(l) is int:
       l = [l]
    if type(r) is int:
       r = [r]
    
    if l == [] and r != []:
       return -1
    if l != [] and r == []:
       return 1
    if l == [] and r == []:
       return 0
     
    res = check(l[0], r[0])
    if res:
       return res
    else:
       return check(l[1:], r[1:])

num = 0
res = 0
packets = []
with open(file) as f:
     for line1, line2 in zip(f, f): 
         num += 1
         first = json.loads(line1.strip())
         second = json.loads(line2.strip())
         packets.append(first)
         packets.append(second) 
         if check(first, second) < 1:
            res += num
         f.readline()

packets.append([[2]])
packets.append([[6]])
packets.sort(key=functools.cmp_to_key(check))

print("Part 1:", res)
print("Part 2:", (1 + packets.index([[2]])) * (1 + packets.index([[6]]))) 
