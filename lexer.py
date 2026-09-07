from enum import Enum, auto
class token(Enum): #Classe que guarda os tipos de token, se você quiser adicionar é so por "nomedotoken = auto()"
    ID = auto,
    NUM = auto()
def addTk(_t, _v): #Função que adiciona um tipo de token
    return [_t,_v]
