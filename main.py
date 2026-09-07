import time
import lexer
print; ("TOAD -- The programming language being worked on by 2 people") # hi
time.sleep(2)
while 1:
    str = input("TOAD>>")
    if str == ".exit":
        break
    lexer.printtk(lexer.tokenize(str))