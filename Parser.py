ESTADO_FINAL = "ESTADO FINAL"
ESTADO_NO_FINAL = "NO ACEPTADO"
ESTADO_TRAMPA = "EN ESTADO TRAMPA"


def automataId(lexema):
    estado = 0
    estadoFinal = [1]
    for caracter in lexema:
        if estado == 0 and (
                caracter == "a" or caracter == "b" or caracter == "c" or caracter == "d" or caracter == "e" or caracter == "f" or caracter == "g" or caracter == "h" or caracter == "i" or caracter == "j" or caracter == "k" or caracter == "l" or caracter == "m" or caracter == "n" or caracter == "o" or caracter == "p" or caracter == "q" or caracter == "r" or caracter == "s" or caracter == "t" or caracter == "u" or caracter == "v" or caracter == "w" or caracter == "x" or caracter == "y" or caracter == "z"
                or caracter == "A" or caracter == "B" or caracter == "C" or caracter == "D" or caracter == "E" or caracter == "F" or caracter == "G" or caracter == "H" or caracter == "I" or caracter == "J" or caracter == "K" or caracter == "L" or caracter == "M" or caracter == "N" or caracter == "O" or caracter == "P" or caracter == "Q" or caracter == "R" or caracter == "S" or caracter == "T" or caracter == "U" or caracter == "V" or caracter == "W" or caracter == "X" or caracter == "Y" or caracter == "Z"):
            estado = 1
        elif estado == 1 and (
                caracter == "a" or caracter == "b" or caracter == "c" or caracter == "d" or caracter == "e" or caracter == "f" or caracter == "g" or caracter == "h" or caracter == "i" or caracter == "j" or caracter == "k" or caracter == "l" or caracter == "m" or caracter == "n" or caracter == "o" or caracter == "p" or caracter == "q" or caracter == "r" or caracter == "s" or caracter == "t" or caracter == "u" or caracter == "v" or caracter == "w" or caracter == "x" or caracter == "y" or caracter == "z"
                or caracter == "A" or caracter == "B" or caracter == "C" or caracter == "D" or caracter == "E" or caracter == "F" or caracter == "G" or caracter == "H" or caracter == "I" or caracter == "J" or caracter == "K" or caracter == "L" or caracter == "M" or caracter == "N" or caracter == "O" or caracter == "P" or caracter == "Q" or caracter == "R" or caracter == "S" or caracter == "T" or caracter == "U" or caracter == "V" or caracter == "W" or caracter == "X" or caracter == "Y" or caracter == "Z"
                or caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9" or caracter == "-" or caracter == "_"):
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataNum(lexema):
    estado = 0
    estadoFinal = [1]
    for caracter in lexema:
        if estado == 0 and (
                caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9"):
            estado = 1
        elif estado == 1 and (
                caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9"):
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataSi(lexema):
    estado = 0
    estadoFinal = [2]
    for caracter in lexema:
        if estado == 0 and caracter == "s":
            estado = 1
        elif estado == 1 and caracter == "i":
            estado = 2
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataEntonces(lexema):
    estado = 0
    estadoFinal = [8]
    for caracter in lexema:
        if estado == 0 and caracter == "e":
            estado = 1
        elif estado == 1 and caracter == "n":
            estado = 2
        elif estado == 2 and caracter == "t":
            estado = 3
        elif estado == 3 and caracter == "o":
            estado = 4
        elif estado == 4 and caracter == "n":
            estado = 5
        elif estado == 5 and caracter == "c":
            estado = 6
        elif estado == 6 and caracter == "e":
            estado = 7
        elif estado == 7 and caracter == "s":
            estado = 8
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataSino(lexema):
    estado = 0
    estadoFinal = [4]
    for caracter in lexema:
        if estado == 0 and caracter == "s":
            estado = 1
        elif estado == 1 and caracter == "i":
            estado = 2
        elif estado == 2 and caracter == "n":
            estado = 3
        elif estado == 3 and caracter == "o":
            estado = 4
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataFinsi(lexema):
    estado = 0
    estadoFinal = [5]
    for caracter in lexema:
        if estado == 0 and caracter == "f":
            estado = 1
        elif estado == 1 and caracter == "i":
            estado = 2
        elif estado == 2 and caracter == "n":
            estado = 3
        elif estado == 3 and caracter == "s":
            estado = 4
        elif estado == 4 and caracter == "i":
            estado = 5
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataRepetir(lexema):
    estado = 0
    estadoFinal = [7]
    for caracter in lexema:
        if estado == 0 and caracter == "r":
            estado = 1
        elif estado == 1 and caracter == "e":
            estado = 2
        elif estado == 2 and caracter == "p":
            estado = 3
        elif estado == 3 and caracter == "e":
            estado = 4
        elif estado == 4 and caracter == "t":
            estado = 5
        elif estado == 5 and caracter == "i":
            estado = 6
        elif estado == 6 and caracter == "r":
            estado = 7
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataHasta(lexema):
    estado = 0
    estadoFinal = [5]
    for caracter in lexema:
        if estado == 0 and caracter == "h":
            estado = 1
        elif estado == 1 and caracter == "a":
            estado = 2
        elif estado == 2 and caracter == "s":
            estado = 3
        elif estado == 3 and caracter == "t":
            estado = 4
        elif estado == 4 and caracter == "a":
            estado = 5
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataEqual(lexema):
    estado = 0
    estadoFinal = [5]
    for caracter in lexema:
        if estado == 0 and caracter == "e":
            estado = 1
        elif estado == 1 and caracter == "q":
            estado = 2
        elif estado == 2 and caracter == "u":
            estado = 3
        elif estado == 3 and caracter == "a":
            estado = 4
        elif estado == 4 and caracter == "l":
            estado = 5
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataLeer(lexema):
    estado = 0
    estadoFinal = [4]
    for caracter in lexema:
        if estado == 0 and caracter == "l":
            estado = 1
        elif estado == 1 and caracter == "e":
            estado = 2
        elif estado == 2 and caracter == "e":
            estado = 3
        elif estado == 3 and caracter == "r":
            estado = 4
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataMostrar(lexema):
    estado = 0
    estadoFinal = [7]
    for caracter in lexema:
        if estado == 0 and caracter == "m":
            estado = 1
        elif estado == 1 and caracter == "o":
            estado = 2
        elif estado == 2 and caracter == "s":
            estado = 3
        elif estado == 3 and caracter == "t":
            estado = 4
        elif estado == 4 and caracter == "r":
            estado = 5
        elif estado == 5 and caracter == "a":
            estado = 6
        elif estado == 6 and caracter == "r":
            estado = 7
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataFunc(lexema):
    estado = 0
    estadoFinal = [4]
    for caracter in lexema:
        if estado == 0 and caracter == "f":
            estado = 1
        elif estado == 1 and caracter == "u":
            estado = 2
        elif estado == 2 and caracter == "n":
            estado = 3
        elif estado == 3 and caracter == "c":
            estado = 4
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataFinFunc(lexema):
    estado = 0
    estadoFinal = [7]
    for caracter in lexema:
        if estado == 0 and caracter == "f":
            estado = 1
        elif estado == 1 and caracter == "i":
            estado = 2
        elif estado == 2 and caracter == "n":
            estado = 3
        elif estado == 3 and caracter == "f":
            estado = 4
        elif estado == 4 and caracter == "u":
            estado = 5
        elif estado == 5 and caracter == "n":
            estado = 6
        elif estado == 6 and caracter == "c":
            estado = 7
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataComa(lexema):
    estado = 0
    estadoFinal = [1]
    for caracter in lexema:
        if estado == 0 and caracter == ",":
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataPuntoyComa(lexema):
    estado = 0
    estadoFinal = [1]
    for caracter in lexema:
        if estado == 0 and caracter == ";":
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def automataParentesisAbre(lexema):
    estado = 0
    estadoFinal = [1]
    for caracter in lexema:
        if estado == 0 and caracter == "(":
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL

def automataParentesisCierra(lexema):
    estado = 0
    estadoFinal = [1]
    for caracter in lexema:
        if estado == 0 and caracter == ")":
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL      

def automataSuma(lexema):
    estado = 0
    estadoFinal = [1]
    for caracter in lexema:
        if estado == 0 and (caracter == "+" or caracter == "-"):
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataMult(lexema):
    estado = 0
    estadoFinal = [1]
    for caracter in lexema:
        if estado == 0 and (caracter == "*" or caracter == "/"):
            estado = 1
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


def automataOprel(lexema):
    estado = 0
    estadoFinal = [1, 3]
    for caracter in lexema:
        if estado == 0 and caracter == ">":
            estado = 1
        elif estado == 0 and caracter == "<":
            estado = 1
        elif estado == 0 and caracter == "=":
            estado = 3
        elif estado == 1 and caracter == "=":
            estado = 3
        elif estado == 0 and caracter == "!":
            estado = 2
        elif estado == 2 and caracter == "=":
            estado = 3
        else:
            estado = -1
            break
    if estado == -1:
        return ESTADO_TRAMPA
    elif estado in estadoFinal:
        return ESTADO_FINAL
    else:
        return ESTADO_NO_FINAL


TOKENS_POSIBLES = [("si", automataSi),
                   ("entonces", automataEntonces),
                   ("sino", automataSino),
                   ("finsi", automataFinsi),
                   ("repetir", automataRepetir),
                   ("hasta", automataHasta),
                   ("equal", automataEqual),
                   ("leer", automataLeer),
                   ("mostrar", automataMostrar),
                   ("func", automataFunc),
                   ("finfunc", automataFinFunc),
                   ("coma", automataComa),
                   (";", automataPuntoyComa),
                   ("(", automataParentesisAbre),
                   (")", automataParentesisCierra),
                   ("opsuma", automataSuma),
                   ("opmult", automataMult),
                   ("oprel", automataOprel),
                   ("num", automataNum),
                   ("id", automataId)]


def lexer(codigo_fuente):
    tokens = []
    posicion_actual = 0
    while posicion_actual < len(codigo_fuente):
        while codigo_fuente[posicion_actual].isspace():
            posicion_actual = posicion_actual + 1

        comienzo_lexema = posicion_actual
        posibles_tokens = []
        posibles_tokens_con_un_caracter_mas = []
        lexema = ""
        var_aux_todos_en_estado_trampa = False

        while not var_aux_todos_en_estado_trampa and posicion_actual < len(codigo_fuente) + 1:

            var_aux_todos_en_estado_trampa = True
            lexema = codigo_fuente[comienzo_lexema:posicion_actual + 1]
            posibles_tokens = posibles_tokens_con_un_caracter_mas
            posibles_tokens_con_un_caracter_mas = []

            for (un_tipo_de_token, afd) in TOKENS_POSIBLES:
                simulacion_afd = afd(lexema)
                if simulacion_afd == ESTADO_FINAL:
                    posibles_tokens_con_un_caracter_mas.append(un_tipo_de_token)
                    var_aux_todos_en_estado_trampa = False
                elif simulacion_afd == ESTADO_NO_FINAL:
                    var_aux_todos_en_estado_trampa = False

            posicion_actual = posicion_actual + 1

        if len(posibles_tokens) == 0:
            print("Error desconocido")

        posicion_actual = posicion_actual - 1
        un_tipo_de_token = posibles_tokens[0]
        token = (un_tipo_de_token, codigo_fuente[comienzo_lexema:posicion_actual])

        tokens.append(token)

    print(tokens)
    return tokens

VN = ['Program','ListaSentencias','A','Sentencia','SentenciaSi','B','SentenciaRepetir','SentenciaAsig','SentenciaLeer',
    'SentenciaMostrar','SentenciaFun','Proc','ListaPar','C','Expresion','D','Expresion2','E','Factor','F','Termino']

VT = ['id','num','si','entonces','sino', 'finsi','repetir','hasta','leer','mostrar','func','finfunc','equal',
    '(', ')',';','oprel','opsuma','opmult','Eof']

SD = {
    'Program': {
        'si': ['ListaSentencias'],
        'repetir': ['ListaSentencias'],
        'leer': ['ListaSentencias'],
        'mostrar': ['ListaSentencias'],
        'func': ['ListaSentencias'],
        'id': ['ListaSentencias']
    },
    'ListaSentencias': {
    'si': ['Sentencia', 'A'],
    'repetir': ['Sentencia', 'A'],
    'leer': ['Sentencia', 'A'],
    'mostrar': ['Sentencia', 'A'],
    'func': ['Sentencia', 'A'],
    'id': ['Sentencia', 'A']  
    },
    'A': {
    ';': [';', 'Sentencia', 'A'],
    'Eof': [],
    'finsi': [],
    'finfunc': [],
    'hasta': [],
    'sino': []
    },
    'Sentencia': {
        'si': ['SentenciaSi'],
        'repetir': ['SentenciaRepetir'],
        'id': ['SentenciaAsig'],
        'leer': ['SentenciaLeer'],
        'mostrar': ['SentenciaMostrar'],
        'func': ['SentenciaFun']
    },
   'SentenciaSi': {
        'si': ['si', 'Expresion', 'entonces', 'ListaSentencias', 'B']
    },
    'B': {
        'sino': ['sino','ListaSentencias','finsi'],
        'finsi': ['finsi']
    },
    'SentenciaRepetir':{
        'repetir':['repetir','ListaSentencias','hasta','Expresion']
    },

    'SentenciaAsig':{
        'id':['id','equal','Expresion']
    },

    'SentenciaLeer':{
        'leer':['leer','id']
    },

    'SentenciaMostrar':{
        'mostrar':['mostrar','Expresion']
    },

    'SentenciaFun':{
        'func':['func','Proc','finfunc']
    },

    'Proc':{
        'id':['id','(','ListaPar',')','ListaSentencias']
    },

    'ListaPar':{
        'id':['id','C']},

    'C':{
        ';':[';','id','C'],
        ')':[]
    },

    'Expresion': {
        '(': ['Expresion2', 'D'],
        'num': ['Expresion2', 'D'],
        'id': ['Expresion2', 'D']
    },
    'D': {
        'oprel': ['oprel', 'Expresion2'],
        ';': [], 
        'entonces': [], 
        ')': [], 
        'hasta': [], 
        'finsi': [], 
        'sino': [], 
        'finfunc': [], 
        'Eof': []
    },

    'Expresion2': {
        '(':['Termino','E'],
        'num':['Termino','E'],
        'id':['Termino','E']
    },
    'E': {
        'opsuma':['opsuma','Termino','E'],
        'oprel':[],
        ';':[],
        'entonces':[],
        ')':[],
        'hasta':[],
        'finsi':[],
        'sino':[],
        'finfunc':[],
        'Eof':[]
    },
    'Termino':{
        '(':['Factor', 'F'],
        'num':['Factor', 'F'],
        'id':['Factor', 'F']
    },
    'F':{
        'opmult':['opmult','Factor','F'], 
        'opsuma':[],
        'oprel':[],
        ';':[],
        'entonces':[],
        ')':[],
        'hasta':[],
        'finsi':[],
        'sino':[],
        'finfunc':[],
        'Eof':[]
    },
    'Factor':{
        '(':['(','Expresion',')'],
        'num':['num'],
        'id':['id']
    }

}

def desc_rec_proc(codigo_fuente):
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
    }   
          
    def pni(no_terminal):
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual in SD[no_terminal].keys():
            ladoderecho=SD[no_terminal][caracter_actual]
            print(f"{no_terminal} --> {ladoderecho}")
            procesar(ladoderecho)  
        else:
            datos_locales['error'] = True


    def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            print(f"{simbolo} -->")
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
            #lexema_actual = datos_locales['lista_tokens'][datos_locales['index']][1]
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:   
                    datos_locales['index'] += 1                        
                else:
                    datos_locales['error'] = True
                    break
            elif simbolo in VN:
                pni(simbolo)
                if datos_locales['error']:
                    break
                
    
    def principal():
        pni('Program')
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual != 'Eof' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        return True
    
    return principal()

#cadena = "si x > 5 entonces mostrar z finsi"
#cadena ="repetir leer x hasta z"
#cadena = "x equal 200"
#cadena = "leer x"
#cadena = "mostrar x"
#cadena = "func x ( q; r; s ; t )  mostrar x finfunc"
#cadena = "func x ( q; r; s ; t ) repetir leer x hasta z finfunc"
#cadena = "id1 equal (1-5)/(z+5)"
#cadena = "si x - 5 entonces leer z finsi ; func a1 (x; y) repetir leer z hasta b finfunc ;  func a1 (x; y) repetir leer x hasta 1 finfunc"
#cadena = "si x!=2 entonces x equal 5 sino x equal 10 finsi"
#tokens = lexer(cadena)
#tokens.append(("Eof", ""))
#desc_rec_proc(tokens)
