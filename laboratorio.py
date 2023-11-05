# Define una variable de cada tipo de primitivo

cadena = 'Esta es una cadena'
numero = 10
decimal = 3.14159
booleano = True

# Concatena a la cadena las otras variables aplicando la conversión correcta para funcionar, guarda el resultado en una variable

# Convertimos el número y el decimal a cadenas
numero_cadena = str(numero)
decimal_cadena = str(decimal)

# Concatenamos las cadenas
cadena = cadena + ', el número es ' + numero_cadena + ', el decimal es ' + decimal_cadena + ' y el booleano es ' + str(booleano)

# Guardamos el resultado en una variable
resultado = cadena

# Investiga sobre el límite de los enteros y los flotantes en python y anotar sus descubrimientos como comentarios en el archivo

# Los enteros en Python son de 64 bits, lo que significa que pueden almacenar números de hasta 2^64 - 1.
# Los flotantes en Python son de doble precisión, lo que significa que pueden almacenar números de hasta 15 decimales.

# Aplica la fórmula de la suma de los primeros n números pares (investigar), tomando como n la variable de tipo entero y almacenar el resultado en una variable

# La fórmula de la suma de los primeros n números pares es:
#
# suma = n * (n + 1)

# Aplicamos la fórmula

suma_pares = numero * (numero + 1)

# Guardamos el resultado en una variable

resultado_suma_pares = suma_pares

# Imprimimos el resultado

print(resultado)
print(resultado_suma_pares)

