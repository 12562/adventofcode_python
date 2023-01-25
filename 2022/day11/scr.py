import getopt, sys
import copy
file = ((getopt.getopt(sys.argv[1:], "i:")[0])[0])[1]

monkeys = {}
monkey_lst = []
lcm = 1
with open(file) as f:
     for line in f:
         line = line.strip().split()
         match line[0:2]:
           case ["Monkey", str()]: 
                        curr_monkey = line[1].rstrip(':')
                        monkeys[curr_monkey] = {} 
                        monkey_lst.append(curr_monkey)
                        (monkeys[curr_monkey])['Inspected'] = 0
           case ["Starting", "items:"]: 
                        (monkeys[curr_monkey])['items'] = [int(i.rstrip(",")) for i in line[2:]]
           case ["Operation:", "new"]: 
                        (monkeys[curr_monkey])['operation'] = ''.join(line[3:])
           case ["Test:", "divisible"]: 
                        (monkeys[curr_monkey])['divisible by'] = int(line[3])
                        lcm *= int(line[3])
           case ["If", "true:"]: 
                        (monkeys[curr_monkey])['If true'] = line[5]
           case ["If", "false:"]: 
                        (monkeys[curr_monkey])['If false'] = line[5]
           case _: 
                        continue 

def run_rounds(num_rounds, worry_level_divided, monkeys):
    for i in range(0,num_rounds):
        for monkey in monkey_lst:
            num_items = len((monkeys[monkey])['items'])
            (monkeys[monkey])['Inspected'] += num_items
            (monkeys[monkey])['items'].reverse()
            for j in range(0,num_items):
                old = (monkeys[monkey])['items'].pop()
                if ( worry_level_divided ):
                  worry_level = int(eval((monkeys[monkey])['operation']) / 3 )
                else:
                  worry_level = int(eval((monkeys[monkey])['operation']) % lcm )
                if ( worry_level % (monkeys[monkey])['divisible by'] ):
                   (monkeys[(monkeys[monkey])['If false']])['items'].append(worry_level)
                else:
                   (monkeys[(monkeys[monkey])['If true']])['items'].append(worry_level)
    
    inspected = []
    for j in monkey_lst:
        inspected.append((monkeys[j])['Inspected'])
    inspected.sort()
    return inspected[-1] * inspected[-2]

monkeys2 = copy.deepcopy(monkeys)
print("Part 1:",  run_rounds(20, True, monkeys))
print("Part 2:", run_rounds(10000, False, monkeys2))
