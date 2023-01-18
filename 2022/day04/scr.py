import re
with open("./input4.txt", "r", encoding="utf8") as f:
     res = 0
     res2 = 0
     for line in f:
         rng1_l, rng1_u, rng2_l, rng2_u = map(int, re.split('-|,',line.strip()))
         if (( (rng1_l <= rng2_l ) and (rng2_u <= rng1_u)) or ((rng2_l <= rng1_l) and (rng1_u <= rng2_u))) : 
            res += 1 
         if ((rng1_l >= rng2_l) and (rng1_l <= rng2_u)) or \
            ((rng1_u >= rng2_l) and (rng1_u <= rng2_u)) or \
            ((rng2_l >= rng1_l) and (rng2_l <= rng1_u)) or \
            ((rng2_u >= rng1_l) and (rng2_u <= rng1_u)):
            res2 += 1
                 
print(f"Part 1: {res}")
print(f"Part 2: {res2}")

#with open("./input3.txt", "r", encoding="utf8") as f:
#     res = 0
#     for line1, line2, line3 in zip(f, f, f):
#         line1 = line1.strip()
#         line2 = line2.strip()
#         line3 = line3.strip()
#         for c in line1:
#             if (c in line2) and (c in line3):
#                res += ITEMS.index(c) + 1
#                break
#
#print(f"Part 2: {res}")    
#     
