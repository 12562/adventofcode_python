# https://github.com/d9d6ka/advent-of-code/blob/master/2022/day-02/part1.py
with open("./input2.txt", "r", encoding="utf8") as f:
     score = score2 = 0
     for line in f:
         draw = line.strip().split()
         match draw:
               case ["A", "X"] | ["B", "Y"] | ["C", "Z"]:
                    score +=  3
               case ["A", "Y"] | ["B", "Z"] | ["C", "X"]:
                    score +=  6
               case _:
                    pass

         match draw[1]:
               case "X":
                    score2 += 1 + 'BCA'.index(draw[0])
               case "Y":
                    score2 += 4 + 'ABC'.index(draw[0])
               case "Z":
                    score2 += 7 + 'CAB'.index(draw[0])

         score += 1 + 'XYZ'.index(draw[1])

print(f"Part 1: {score}")
print(f"Part 2: {score2}")
