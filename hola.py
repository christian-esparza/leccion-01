# Entrada de datos
nombre = input("¿Cuál es tu nombre? ")
anio_nacimiento_texto = input("¿En qué año naciste? ")

# Conversión de tipo y cálculo
anio_nacimiento = int(anio_nacimiento_texto)
anio_actual = 2026
edad = anio_actual - anio_nacimiento

# Saludo general
print(f"¡Hola, {nombre}! En {anio_actual} tienes o cumples aproximadamente {edad} años.")

# Estructura condicional (toma de decisiones)
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.") 