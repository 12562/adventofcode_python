import getopt, sys, os
sys.path.append(os.getcwd())
from PIL import Image
from pytesseract import pytesseract
from tti import *

file = ((getopt.getopt(sys.argv[1:], "i:")[0])[0])[1]

X = 1
strength = 0
cycle = 0
pos = 0
CRT = ''

def update_crt(mystr, pos):
    if (pos % 40) in range(X-1,X+2):
       mystr += '#'
    else:
       mystr += ' '

    if pos % 40 == 39:
       mystr += '\n'

    return mystr

with open(file) as f:
     for line in f:
         instr = line.strip().split()
         match instr[0]:
            case "noop": 
                         cycle = cycle + 1
                         CRT = update_crt(CRT, pos)
                         pos = (pos + 1) % 40
                         if ( (cycle - 20) % 40 == 0) and (cycle <= 220 ):
                            strength += X * cycle
            case "addx": 
                         for i in range(2):
                             cycle += 1
                             CRT = update_crt(CRT, pos)
                             pos = (pos + 1) % 40
                             if ( (cycle - 20) % 40 == 0) and (cycle <= 220 ):
                                strength += X * cycle
                         X += int(instr[1])
print("Part 1:", strength)
image = txt_to_image(CRT)
image.save('content.png')
img = Image.open('content.png')
pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
txt = pytesseract.image_to_string(img, lang='eng', config='--psm 8').strip()
print("Part 2:", txt)
