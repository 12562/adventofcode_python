
with open("./input6.txt") as f:
     for line in f:
         mystr = line.strip()

def check_repeat(mystr):
    sorted_str = sorted(mystr)
    for n in range(1, len(mystr)):
        if sorted_str[n] == sorted_str[n-1]:
           return True
    return False

def run_part(mystr, num):
    for i in range(len(mystr)):
        if ( not check_repeat(mystr[i:i+num]) ):
           break
    return i + num

print("Part 1: ", run_part(mystr, 4))
print("Part 2: ", run_part(mystr, 14))
