# Crear una función para convertir grados centigrados a grados Fahrenheit, a grados kelvin
def convertir_temperatura(grad_cent):
    fahrenheit = (9/5)*grad_cent + 32
    kelvin = 273.15 + grad_cent
    return fahrenheit, kelvin

# Ejemplo de uso
grados_celsius = 22

fahrenheit, kelvin = convertir_temperatura(grados_celsius)
print(grados_celsius, "grados Celsius son", fahrenheit, "grados Fahrenheit y", kelvin, "grados Kelvin.")