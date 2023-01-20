import re
with open("input7.txt") as f:
     current_dir = []
     filesystem = {}
     for line in f:
         line = line.strip().split()
         match line[0:3]:
           case ["$", "cd", "/"]:
                   current_dir.append("/")
           case ["$", "cd", ".."]:
                   current_dir.pop()
                   current_dir.pop()
           case ["$", "cd", str()]:
                   current_dir.append("/") if current_dir != ["/"] else None
                   current_dir.append(line[2])
           case ["$", "ls"]:
                   filesystem[''.join(current_dir)] = []
           case ["dir", str()]:
                   filesystem[''.join(current_dir)].append(''.join(current_dir) + ("/" if current_dir != ["/"] else "") + line[1])
           case _:
                   filesystem[''.join(current_dir)].append({line[1] : int(line[0])})

sorted_keys = sorted(filesystem.keys(), key=lambda x: (x.count("/"), len(re.findall("/?([a-z]+)/?", x))), reverse=True)

for key in sorted_keys:
    dir_sum = 0;
    for elem in filesystem[key]:
        match elem:
          case str(): dir_sum += filesystem[elem]
          case dict(): dir_sum += list(elem.values())[0]
          case _: pass
    filesystem[key] = dir_sum

print(f'Part 1: {sum([v for (k,v) in filesystem.items() if v <= 100000])}')
print(f'Part 2: {[v for (k,v) in filesystem.items() if v >= (30000000 - (70000000 - filesystem["/"]))][-1]}')
