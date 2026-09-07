import time
import lexer
import pyfiglet
from colorama import Fore
print(Fore.YELLOW+ pyfiglet.figlet_format("T.O.A.D.", font="xsbookb")) # hi
time.sleep(3)
while 1:
    str = input(Fore.LIGHTMAGENTA_EX+"TOAD>>" + Fore.RESET)
    if str == ".exit":
        break
    lexer.printtk(lexer.tokenize(str))