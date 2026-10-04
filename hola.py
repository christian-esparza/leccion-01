# Pedimos el nombre al usuario
nombre = input("¿Cuál es tu nombre? ")

# Pedimos el año de nacimiento (llega como texto, ej. "2007")
anio_nacimiento_texto = input("¿En qué año naciste? ")

# Convertimos el texto a número entero
anio_nacimiento = int(anio_nacimiento_texto)

# Calculamos la edad aproximada
anio_actual = 2026
edad = anio_actual - anio_nacimiento

# Mostramos el saludo y la edad calculada
print(f"¡Hola, {nombre}! En {anio_actual} tienes o cumples aproximadamente {edad} años.") 
