# Casos de Uso del Lexer de Python

## Caso 1: Código básico con variables y bucles
### Entrada:
```python
x = 2
while x < 5:
    print(f"x vale {x}")
    x += 1


Salida esperada:
KEYWORDS: while
LITERALS: "x vale {x}"
IDENTIFIERS: x, print
CONSTANTS: 2, 5, 1
OPERATORS: =, <, +=
PUNCTUATION: :, ()

Tokens en total: 16


Caso 2:

import re
def sumar(a, b):
    return a + b


Salida esperada:
KEYWORDS: import, def, return
IDENTIFIERS: re, sumar, a, b
OPERATORS: =
PUNCTUATION: (), :


tokens en total: 14 o 13
