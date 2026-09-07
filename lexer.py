from enum import Enum, auto
from colorama import Fore
class t(Enum): #Classe que guarda os tipos de token, se você quiser adicionar é so por "nomedotoken = auto()"
    ID = auto(),
    NUM = auto(),
    UNKNOWN = auto(),
    ERROR = auto()
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
            if err:
                tk.append([t.ERROR, "LEXICAL ERROR"]) #Dá erro quando decimal duplo
                break
            else:
                tk.append([t.NUM, buf])
                continue
        elif str.isalnum(_src[pos]): #verifica se é um texto alfanumérico
            buf = ""
            while pos < n and (str.isalnum(_src[pos]) or _src[pos] == '_'):
                buf+=_src[pos]
                pos+=1
            tk.append([t.ID, buf])
            continue
        else:
            tk.append([t.UNKNOWN, _src[pos]])
            break
    return tk
def printtk(_tk): #Função básica pra printar os tokens
    for i in _tk:
        print(Fore.GREEN+f"[Type: '{i[0].name}', Value: '{i[1]}']")
#TODO: Adicionar mais tipos de tokens
#0% feito por ia :fogo::fogo: