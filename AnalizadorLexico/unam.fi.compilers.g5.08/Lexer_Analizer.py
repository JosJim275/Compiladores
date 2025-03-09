import re  #Importa la biblioteca re que es para las expresiones regulares

#Parte para definir nuestras reglas de las expresiones regulares
token_specification = [
    ('KEYWORD', r'\bdef\b|\bin\b|\bimport\b|\bif\b|\bwhile\b'),
    ('LITERAL', r'f?"[^"]*"'),
    ('CONSTANT', r'\b\d+\.\d+|\b\d+\b'),               
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z_0-9]*'),           
    ('OPERATOR', r'==|!=|<=|>=|<|>|=|\+|\-|\*|/'), 
    ('PUNCTUATION', r'[\(\):\[\]\{\}]'),   
    ('WHITESPACE', r'\s+'),          
]

#Parte para que la expresion regular 
token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)

#Organiza los tokens en los nombres y cuenta la cantidad de tokens
def lexer(code):
    tokens = {
        "KEYWORDS": [],
        "LITERALS": [],
        "IDENTIFIERS": [],
        "CONSTANTS": [],
        "OPERATORS": [],
        "PUNCTUATION": []
    }
    
    total_tokens = 0  

    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group(kind)
        if kind != 'WHITESPACE':  
            total_tokens += 1
            if kind == "KEYWORD":
                tokens["KEYWORDS"].append(value)
            elif kind == "LITERAL":
                tokens["LITERALS"].append(value)
            elif kind == "IDENTIFIER":
                tokens["IDENTIFIERS"].append(value)
            elif kind == "CONSTANT":
                tokens["CONSTANTS"].append(value)
            elif kind == "OPERATOR":
                tokens["OPERATORS"].append(value)
            elif kind == "PUNCTUATION":
                tokens["PUNCTUATION"].append(value)
    
    return tokens, total_tokens

if __name__ == "__main__":
    #Parte del codigo que va a leer los tipos de tokens
    code = """x = 0.2
    y={}
    
    while x < 5:
        print(f"x vale {x}")
        x += 1
    """
    
    #llamadas de funcion
    tokens, total_count = lexer(code)
    
    #Se concatenan los tokens de la funcion en una sola salida
    output = "Tokens reconocidos:\n"
    for category, values in tokens.items():
        count = len(values)
        output += f"{category} ({count}): {', '.join(values)}\n"
    
    output += f"\nTotal de tokens: {total_count}"
    
    print(output)
