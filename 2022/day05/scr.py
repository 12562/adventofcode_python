import re
import copy
crate_str_arr = []
lst = []
move_arr = []
flag = 0
with open("./input5.txt") as f:
     for line in f:
         if line.strip() == "":
            flag = 2
            continue
         elif line.find("[") == -1 and not flag :
            index_line = line.rstrip()
            flag = 1 
 
         if ( not flag ):
            crate_str_arr.append(line)
         if ( flag == 2): 
            move_arr.append(line.strip()) 

#indices = [int(i) - 1 for i in re.findall('[0-9]+', index_line)]
_iter_ = re.finditer(r"[0-9]+", index_line)
pos = [m.start(0) for m in _iter_]
for i in range(len(crate_str_arr)):
    lst.append([ crate_str_arr[i][pos[j]] for j in range(len(pos)) ])
crate_arr =  [list(filter(lambda a : a != " ", list(reversed(x)))) for x in zip(*lst)]
crate_arr2 = copy.deepcopy(crate_arr)

def move(arr, start, end, amt, rev):
    tmp = arr[start - 1][-amt:]      
    if ( rev ):
       tmp.reverse()
    arr[start - 1] = arr[start - 1][:-amt]
    arr[end - 1] = arr[end - 1] + tmp
         
for move_instr in move_arr:
    amt, start, end =  map(int, re.findall('[0-9]+', move_instr))
    move(crate_arr, start, end, amt, True)
    move(crate_arr2, start, end, amt, False)

res = ""
res2 = ""
for k in range(len(crate_arr)):
    res = res + crate_arr[k][-1]
    res2 = res2 + crate_arr2[k][-1]

print("Part 1: ", res)
print("Part 2: ", res2)
