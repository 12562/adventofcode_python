
input_file: str = "input1.txt"

with open(input_file, 'r') as input_:
     calories: list[tuple] = [(n, sum([int(food) for food in elf.split('\n') if food not in ['']])) for n, elf in enumerate(input_.read().split('\n\n'))]

elfs, calories = zip(*calories)
top: int = max(calories)

print("Part 1: ", top)
print("Part 2: ", sum(sorted(calories, reverse = True)[:3]))
