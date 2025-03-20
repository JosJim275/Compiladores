from flask import Flask, request, jsonify
from flask_cors import CORS 
import re

app = Flask(__name__)
CORS(app)  # Habilita CORS para permitir solicitudes desde el frontend

TOKEN_SPECIFICATION = [
    ('KEYWORD', r'\b(def|in|import|if|while|return)\b'),
    ('LITERAL', r'f?"[^"]*"'),
    ('CONSTANT', r'\b\d+\.\d+|\b\d+\b'),
    ('IDENTIFIER', r'\b[a-zA-Z_][a-zA-Z_0-9]*\b'),
    ('OPERATOR', r'==|!=|<=|>=|<|>|=|\+|\-|\*|/'),
    ('PUNCTUATION', r'[\(\):\[\]\{\}]'),
    ('WHITESPACE', r'\s+'),
]

token_regex = '|'.join(f'(?P<{name}>{regex})' for name, regex in TOKEN_SPECIFICATION)

def lexer(code):
    tokens = {category: [] for category, _ in TOKEN_SPECIFICATION if category != "WHITESPACE"}
    total_tokens = 0

    for match in re.finditer(token_regex, code):
        kind = match.lastgroup
        value = match.group(kind)
        if kind != 'WHITESPACE':  
            total_tokens += 1
            if value not in tokens[kind]:
                tokens[kind].append(value)
    
    return {"tokens": tokens, "total_tokens": total_tokens}

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    code = data.get("code", "")
    result = lexer(code)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
