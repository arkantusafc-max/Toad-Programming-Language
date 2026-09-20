from enum import Enum, auto
from colorama import Fore
def tokenize(_src): #A função que tokeniza
    tk = [] #a lista de tokens
    pos = 0 # o caractere atual (começa do zero)
    n = len(_src) #tamanho da linha
    while pos < n:
        if str.isspace(_src[pos]): #Pula o caractere se for um espaço
            pos+=1
            continue
        elif str.isdigit(_src[pos]): #verifica se o caractere é um numero (0-9)
            buf = ""
            dot = False
            err = False
            while pos < n and (str.isdigit(_src[pos]) or _src[pos] == '.'):
                if _src[pos] == '.':
                    if dot:
                        err = True
                        break
                    dot = True
                buf+=_src[pos]
                pos+=1
            if err or buf[-1] == ".":
                tk.append(["ERROR", f"LEXICAL ERROR AT COLUMN {pos+1}"]) #Dá erro quando decimal duplo
                break
            else:
                tk.append(["NUMBER", float(buf)])
                continue
        elif str.isalnum(_src[pos]) or _src[pos] == '_': #verifica se é um texto alfanumérico
            buf = ""
            while pos < n and (str.isalnum(_src[pos]) or _src[pos] == '_'):
                buf+=_src[pos]
                pos+=1
            tk.append(["IDENTIFIER", buf])
            continue
        elif _src[pos] == '\"': #Pula o caractere se for um espaço
            buf =""
            pos+=1
            while pos < n and _src[pos] != '\"':
                buf+=_src[pos]
                pos+=1
            tk.append(["STRING", buf])
            pos+=1
            continue
        elif _src[pos] == '=':
            tk.append(["EQUALS", '='])
            pos+=1
        elif _src[pos] == '+':
            tk.append(["SUM", '+'])
            pos+=1
        elif _src[pos] == '-':
            tk.append(["MINUS", '-'])
            pos+=1
        elif _src[pos] == '/':
            tk.append(["DIVISION", '/'])
            pos+=1
        elif _src[pos] == '$':
            tk.append(["VAR", '$'])
            pos+=1
        elif _src[pos] == '(':
            tk.append(["LEFT PARENTHESIS", '('])
            pos+=1
        elif _src[pos] == ')':
            tk.append(["RIGHT PARENTHESIS", ')'])
            pos+=1
        else:
            tk.append(["UNKNOWN", _src[pos]])
            break
    return tk
def printtk(_tk): #Função básica pra printar os tokens
    for i in _tk:
        print(Fore.GREEN+f"[Type: '{i[0]}', Value: '{i[1]}']")
#TODO: Adicionar mais tipos de tokens
#0% feito por ia :fogo::fogo: