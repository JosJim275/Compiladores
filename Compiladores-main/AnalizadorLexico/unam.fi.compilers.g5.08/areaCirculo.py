
def calcular_area_rectangulo(base, altura):

    area = base * altura

    return area


MENSAJE_BIENVENIDA = "Bienvenido al calculador de áreas de rectángulos."


print(MENSAJE_BIENVENIDA)
base = 5
altura = 10.2


area_resultado = calcular_area_rectangulo(base, altura)


print(f"El área del rectángulo con base {base} y altura {altura} es: {area_resultado}")