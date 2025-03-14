import unittest
from Lexer_Analyzer import lexer  
import os

class TestLexer(unittest.TestCase):
    PRUEBAS_DIR = "Pruebas"

    def test_lexer_on_files(self):
        """Prueba el lexer con archivos dentro de la carpeta Pruebas."""
        for filename in os.listdir(self.PRUEBAS_DIR):
            if filename.endswith(".py"):  # Solo procesamos archivos Python
                with self.subTest(filename=filename):
                    filepath = os.path.join(self.PRUEBAS_DIR, filename)
                    with open(filepath, 'r', encoding='utf-8') as f:
                        code = f.read()
                    
                    tokens, total_count = lexer(code)
                    
                    # Mostrar resultado en consola
                    print(f"\nArchivo: {filename}")
                    print("Tokens reconocidos:")
                    for category, values in tokens.items():
                        print(f"{category} ({len(values)}): {', '.join(values)}")
                    print(f"Total de tokens: {total_count}\n")
                    
                    # Verificamos que haya al menos un token
                    self.assertGreater(total_count, 0, f"El archivo {filename} no generó tokens.")
                    
                    # Verificamos que cada token esté categorizado correctamente
                    for category, values in tokens.items():
                        for token in values:
                            self.assertIsInstance(token, str, f"Token inválido en {category}: {token}")


if __name__ == "__main__":
    unittest.main()
