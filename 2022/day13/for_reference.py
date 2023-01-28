
#def parse ( exp ):
#    print(exp)
#    if exp[0] != '[':
#       return int(exp)
#    brckt_lvl = 0
#    return_exp = []
#    tmp = ''
#    for char in exp[1:-1]:
#        match char:
#          case '[': 
#                    tmp += char
#                    brckt_lvl += 1
#          case ']':
#                    tmp += char
#                    brckt_lvl -= 1
#          case ',' if brckt_lvl == 0:
#                    return_exp.append(parse(tmp))
#                    tmp = ''
#          case _:
#                    tmp += char
#    if tmp != '':
#       return_exp.append(parse(tmp))
#    return return_exp
