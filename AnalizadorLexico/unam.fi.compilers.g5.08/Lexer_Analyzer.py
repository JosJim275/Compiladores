import re  #re library for the regular expressions

#Regular expressions definition

token_specification = [
    ('KEYWORD', r'\bdef\b|\bin\b|\bimport\b|\bif\b|\bwhile\b|\breturn\b'),  #Python keywords
    ('LITERAL', r'f?"[^"]*"'),  #String literals, including f-strings
    ('CONSTANT', r'\b\d+\.\d+|\b\d+\b'),  #Numeric constants
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z_0-9]*'),  #Python valid identifiers
    ('OPERATOR', r'==|!=|<=|>=|<|>|=|\+|\-|\*|/'),  #Common operators
    ('PUNCTUATION', r'[\(\):\[\]\{\}]'),  #Punctuation marks
    ('WHITESPACE', r'\s+'),  #Whitespaces

]


#Part for the regular expressions
token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in token_specification)

#Organizes the tokens by name and counts them
def lexer(code):
    
    """
    Analyzes a code fragment and classifies its tokens
    
    Parameters:
        code (str): Source code to analyze
    
    Returns:
        dict: Set with the classified tokens by category
        int: Total amount of recognized tokens
    """
    
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
    #Code fragment that will read the token types
    code = """x = 0.2
    y={}
    
    while x < 5:
        print(f"x vale {x}")
        x += 1
    """
    
    #Function calls
    tokens, total_count = lexer(code)
    
    #Se concatenan los tokens de la funcion en una sola salida
    #The function tokens are concatenated into a single output
    output = "Tokens reconocidos:\n"
    for category, values in tokens.items():
        count = len(values)
        output += f"{category} ({count}): {', '.join(values)}\n"
    
    output += f"\nTotal de tokens: {total_count}"
    
    print(output)