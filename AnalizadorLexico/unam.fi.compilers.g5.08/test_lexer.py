import unittest
from Lexer_Analizer import lexer  #Import lexer function from the main code

class TestLexer(unittest.TestCase):
    """
    Unit tests for verify the correct functionality of the Lexer
    Each test evaluates if lexer classifies the tokens correctly in different categories,
    such as keywords, identifiers and constants
    """
    
    def test_variables_y_bucle(self):
        """
        Tests the variables detection and control structures
        It evaluates the recognizing of keywords like 'while', identifiers like 'x',
        and the right counting of tokens
        """
        
        code = """x = 2
        while x < 5:
            print(f"x vale {x}")
            x += 1
        """  #Source code with variables, a loop and a print function
        
        tokens, total_count = lexer(code)  #Analyze the code with lexer
        
        #Verifications
        self.assertIn("while", tokens["KEYWORDS"])  #Verify that 'while' are in the keywords
        self.assertIn("x", tokens["IDENTIFIERS"])  #Verify that 'x' are in the identifiers
        self.assertIn("print", tokens["IDENTIFIERS"])  #'print' must be recognized as identifier
        self.assertIn("2", tokens["CONSTANTS"])  #The number '2' must be constants
        self.assertEqual(total_count, 16)  #There are 16 tokens expected
    
    def test_import_y_funcion(self):
        """
        Prueba la detección de importaciones y funciones.
        Se verifica que el lexer reconozca 'import', 'def', nombres de funciones e instrucciones de retorno.
        """
        
        code = """import re
        def sumar(a, b):
            return a + b
        """  #Source code, test with a import, function and return
        
        tokens, total_count = lexer(code)  #Analyze the code with lexer
        
        #Verifications
        self.assertIn("import", tokens["KEYWORDS"])  # 'import' must be in keywords
        self.assertIn("def", tokens["KEYWORDS"])  # 'def' must be in keywords
        self.assertIn("sumar", tokens["IDENTIFIERS"])  # 'sumar' must be in identifiers
        self.assertIn("return", tokens["KEYWORDS"])  # 'return' must be identified as a keyword
        self.assertEqual(total_count, 13)  #13 tokens in total to be expected


if __name__ == '__main__':
    unittest.main()