import unittest
from Lexer_Analizer import lexer  # Importamos la función lexer del código principal

class TestLexer(unittest.TestCase):
    """
    Pruebas unitarias para verificar el correcto funcionamiento del Lexer.
    Cada prueba evalúa si el lexer clasifica correctamente los tokens en diferentes categorías,
    como palabras clave, identificadores y constantes.
    """
    
    def test_variables_y_bucle(self):
        """
        Prueba la detección de variables y estructuras de control.
        Se evalúa el reconocimiento de palabras clave como 'while', identificadores como 'x',
        y la correcta contabilización de tokens.
        """
        
        code = """x = 2
        while x < 5:
            print(f"x vale {x}")
            x += 1
        """  # Código fuente de prueba con variables, un bucle y una función de impresión
        
        tokens, total_count = lexer(code)  # Analizamos el código con el lexer
        
        # Verificaciones
        self.assertIn("while", tokens["KEYWORDS"])  # Verifica que 'while' esté en palabras clave
        self.assertIn("x", tokens["IDENTIFIERS"])  # Verifica que 'x' esté en identificadores
        self.assertIn("print", tokens["IDENTIFIERS"])  # 'print' debería ser reconocido como identificador
        self.assertIn("2", tokens["CONSTANTS"])  # El número '2' debería estar en constantes
        self.assertEqual(total_count, 16)  # Se espera un total de 16 tokens reconocidos
    
    def test_import_y_funcion(self):
        """
        Prueba la detección de importaciones y funciones.
        Se verifica que el lexer reconozca 'import', 'def', nombres de funciones e instrucciones de retorno.
        """
        
        code = """import re
        def sumar(a, b):
            return a + b
        """  # Código fuente de prueba con una importación, una función y un retorno
        
        tokens, total_count = lexer(code)  # Analizamos el código con el lexer
        
        # Verificaciones
        self.assertIn("import", tokens["KEYWORDS"])  # 'import' debe estar en palabras clave
        self.assertIn("def", tokens["KEYWORDS"])  # 'def' debe estar en palabras clave
        self.assertIn("sumar", tokens["IDENTIFIERS"])  # 'sumar' debe ser un identificador
        self.assertIn("return", tokens["KEYWORDS"])  # 'return' debe ser identificado como palabra clave
        self.assertEqual(total_count, 13)  # Se espera un total de 13 tokens reconocidos


if __name__ == '__main__':
    unittest.main()