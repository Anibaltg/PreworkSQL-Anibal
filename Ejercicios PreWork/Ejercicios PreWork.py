# Ejercicio 1VO Crea una variable llamada nombre y asígnale tu nombre como valor. Luego, imprime la variable
a = 21
b = 3
print(a % b)

# Ejercicio 2VO Crea dos variables, a y b , y asígnales los valores 5 y 10 respectivamente. Luego, imprime la suma de a y b .
a = 10
b = 3
print(a**b)

# Ejercicio 3VO Calcula el área de un triángulo con base 10 y altura 5
a = 10
b = 3
print(a * b / 2)

# Ejercicio 4VO Calcula el resto de dividir 17 entre 3.

a = 17
b = 3
print(a%b)

# Ejercicio 1Co Dado un número, imprime si es positivo o negativo
x = -10
if x > 0:
    print("Es positivo")
else:
    print("Es negativo")

# Ejercicio 2Co Dado un número, imprime si es par o impar
x = 6
if x % 2 == 0:
    print("par")
else:
    print("impar")

# Ejercicio 3Co Dado tres números, encuentra y muestra el mayor de ellos
a, b, c = 5, 7, 2
mayor = max(a, b, c)
print (mayor)

# Ejercicio 1Bu Imprime los números del 1 al 10 usando un bucle for .

for item in range(11):
    print(item)

# Ejercicio 2Bu Imprime los números pares del 1 al 20 usando un bucle while .
a = 1
while a <= 20:
    if a % 2 == 0:
        print(a)
    a += 1


# Ejercicio 3Bu Usa un bucle para calcular la suma de los números del 1 al 100.
b = range(1, 101)
a = 0
for numeros in b:
    a += numeros
print("La suma es :", a)


# Ejercicio 1Fu Define una función que tome dos números y retorne su suma.
a = 5
b = 3
def cont(suma):
    print(f"La suma es: {a + b}")

cont([a + b])


def suma(a, b):
    return a + b
print(suma(5, 3))

# Ejercicio 2Fu Defineuna función que tome un número y retorne su factorial.
def fac(n):

    if n == 0:
        return 1
    else:
        return n * fac(n - 1)
print(fac(2))

# Ejercicio 3Fu Define una función que tome un número y determine si es primo.
def primo(p):
    if p < 2:
        return False     
    for i in range(2, p):
        if p % i == 0:            
            return False
    return True
print(primo(8))    

# Ejercicio 4Fu Define una función que reciba una lista de números y retorne la suma de ellos.
def sum_lista(lista):
    return sum(lista)
print(sum_lista([1, 2, 3, 4]))

# Ejercicio 5Fu Define una función que reciba una cadena de texto y retorne la cadena en reversa
def cadena(text):
    return text[::-1]
print(cadena("Hola"))

mi_dic = {'Nombre': 'Anibal', 'Edad': 38}

print(mi_dic['Edad'])