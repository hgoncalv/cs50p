import emoji
import sys
import random
from pyfiglet import Figlet



if len(sys.argv) != 3 and len(sys.argv) != 1:
    sys.exit("")

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) == 3:
    if(sys.argv[1]=="--font" or sys.argv[1]=="-f"):
        font_name = sys.argv[2]
    else:
        sys.exit("")
else:
    font_name = font_list[random.randint(0, len(font_list))]

figlet.setFont(font=font_name)
text = input("Input: ")
print("Output: ")
print(figlet.renderText(text))




