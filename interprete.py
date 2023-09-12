import ply.lex as lex
import ply.yacc as yacc
from comandos.comando_mkdisk import Mkdisk
from comandos.comando_execute import Execute
from comandos.comando_rep import Rep
from comandos.comando_fdisk import Fdisk
from comandos.comando_rmdisk import Rmdisk
#-------------------------------ANALIZADOR LEXICO---------------------------------------------------------------------
errores_lexicos = []

palabras_reservadas = {
    'execute': 'EXECUTE',
    'mkdisk': 'MKDISK',
    'rmdisk' : 'RMDISK',
    'fdisk' : 'FDISK',
    'rep': 'REP',
    'path': 'PATH',
    'size': 'SIZE',
    'unit' : 'UNIT',
    'name' : 'NAME',
    'fit' : 'FIT',
    'type' : 'TYPE',
    'delete' : 'DELETE',
    'add' : 'ADD'
}

tokens = [
    'ENTERO',
    'ID',
    'CADENA_FILE_PATH',
    'IGUAL',
    'GUION',
    'FILE_PATH'

] + list(palabras_reservadas.values())

def t_COMMENT(t):
    r'\#.*'
    print(t.value)
    # No hacer nada en la acción para ignorar el comentario
    pass

t_IGUAL = r'\='
t_GUION = r'\-'

def t_ENTERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_ID(t): # puede ser una letra o un nombre
    r'[a-zA-Z_][a-zA-z0-9_]*'
    c = t.value
    t.type = palabras_reservadas.get(c.lower(), 'ID')
    return t

def t_CADENA_FILE_PATH(t):
    r'"\.?/([^/]+/)*([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z0-9]+)?"'
    t.value = t.value[1:-1] # remuevo las comillas
    return t

def t_FILE_PATH(t):
    r'\.?/([a-z-A-Z_][a-zA-Z0-9_]*/)*([a-zA-Z_][a-zA-Z0-9_]*\.[a-zA-Z0-9]+)?'
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# caracteres ignorados
t_ignore = ' \t'

def t_error(t):
    errores_lexicos.append(t.value[0])
    print(f'Caracter no reconocido: {t.value[0]} en la linea {t.lexer.lineno}')
    t.lexer.skip(1)

#-------------------------------ANALIZADOR SINTACTICO---------------------------------------------------------------------
def p_comandos(t):
    '''comandos : comando_mkdisk
                | comando_execute
                | comando_rep
                | empty_production
                | comando_fdisk
                | comando_rmdisk'''
    t[0] = t[1]

def p_empty_production(t):
    '''
    empty_production : 
    '''
    t[0] = None

#-------comando mkdisk---------
def p_comando_mkdisk(t):
    'comando_mkdisk : MKDISK lista_mkdisk'
    # t[0] : t[1] t[2] t[3]
    t[0] = Mkdisk(t[2])

def p_lista_mkdisk(t):
    '''lista_mkdisk : lista_mkdisk parametros_mkdisk
                | parametros_mkdisk'''
    if len(t) != 2:
        t[1].update(t[2])
        t[0] = t[1]
    else:
        t[0] = t[1]

def p_parametros_mkdisk(t):
    '''parametros_mkdisk : param_size
                | param_unit
                | param_path
                | param_fit'''
    t[0] = t[1]

#-------comando rmdisk---------
def p_comando_rmdisk(t):
    'comando_rmdisk : RMDISK lista_rmdisk'
    # t[0] : t[1] t[2] t[3]
    t[0] = Rmdisk(t[2])

def p_lista_rmdisk(t):
    '''lista_rmdisk : lista_rmdisk parametros_rmdisk
                | parametros_rmdisk'''
    if len(t) != 2:
        t[1].update(t[2])
        t[0] = t[1]
    else:
        t[0] = t[1]

def p_parametros_rmdisk(t):
    '''parametros_rmdisk : param_path'''
    t[0] = t[1]

#------------comando execute----------
def p_comando_execute(t):
    'comando_execute : EXECUTE lista_execute'
    # se manda el parser para ejecutar todos los comandos del archivo
    lexer2 = lex.lex()
    parser2 = yacc.yacc()
    t[0] = Execute(t[2], lexer2, parser2)

def p_lista_execute(t):
    '''lista_execute : lista_execute parametros_execute
                | parametros_execute'''
    if len(t) != 2:
        t[1].update(t[2])
        t[0] = t[1]
    else:
        t[0] = t[1]

def p_parametros_execute(t):
    '''parametros_execute : param_path'''
    t[0] = t[1]

#-------comando rep---------
def p_comando_rep(t):
    'comando_rep : REP'
    t[0] = Rep()

#------------comando fdisk----------
def p_comando_fdisk(t):
    'comando_fdisk : FDISK lista_fdisk'
    t[0] = Fdisk(t[2])

def p_lista_fdisk(t):
    '''lista_fdisk : lista_fdisk parametros_fdisk
                | parametros_fdisk'''
    if len(t) != 2:
        t[1].update(t[2])
        t[0] = t[1]
    else:
        t[0] = t[1]

def p_parametros_fdisk(t):
    '''parametros_fdisk : param_size
                | param_path
                | param_name
                | param_unit
                | param_type
                | param_fit
                | param_delete
                | param_add'''
    t[0] = t[1]

#------------Parametros------------
def p_param_size(t):
    'param_size : GUION SIZE IGUAL ENTERO'
    t[0] = {'size': t[4]}

def p_param_path(t):
    '''param_path : GUION PATH IGUAL CADENA_FILE_PATH
                |  GUION PATH IGUAL FILE_PATH'''
    t[0] = {'path': t[4]}

def p_param_unit(t):
    '''param_unit : GUION UNIT IGUAL ID'''
    t[0] = {'unit': t[4]}

def p_param_name(t):
    '''param_name : GUION NAME IGUAL ID'''
    t[0] = {'name': t[4]}

def p_param_fit(t):
    '''param_fit : GUION FIT IGUAL ID'''
    t[0] = {'fit': t[4]}

def p_param_type(t):
    '''param_type : GUION TYPE IGUAL ID'''
    t[0] = {'type': t[4]}

def p_param_delete(t):
    '''param_delete : GUION DELETE IGUAL ID'''
    t[0] = {'delete': t[4]}

def p_param_add(t):
    '''param_add : GUION ADD IGUAL ENTERO
                | GUION ADD IGUAL entero_negativo'''
    t[0] = {'add': t[4]}

# gramaticas extra

def p_entero_negativo(t):
    'entero_negativo : GUION ENTERO %prec GUION'
    t[0] = -t[2]

# Definición de precedencia
precedence = (
    ('left', 'GUION'),
)

# Regla de manejo de errores
def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}' en la línea {p.lineno}, posición {p.lexpos}")
    else:
        print("Error de sintaxis en la entrada")

lexer = lex.lex()

# llevarla al main
def parse(input):
    global errors
    global parser
    parser = yacc.yacc()
    lexer.lineno = 1
    return parser.parse(input)