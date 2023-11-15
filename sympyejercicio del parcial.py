import sympy as sp

codigo = input("Ingresa un código de números: ")
# Inicializa una lista para almacenar los números separados
numeros = []

# Itera a través de los caracteres en el código
for caracter in codigo:
    if caracter.isdigit():  # Verifica si el carácter es un dígito
        numero = int(caracter)  # Convierte el carácter a un entero
        numeros.append(numero)  # Agrega el número a la lista

# Imprime la lista de números separados
print("Números separados:", numeros)

r1=numeros[0]+numeros[1]+numeros[2]
r2=numeros[1]+numeros[2]+numeros[3]
r3=numeros[2]+numeros[3]+numeros[4]
r4=numeros[3]+numeros[4]+numeros[5]
r5=numeros[4]+numeros[5]+numeros[6]


# Definir las variables simbólicas
x, y, z = sp.symbols('x y z')
a=r1+r2
b=r1
c=r2
d=r1
e=r1+r3+r5
f=r5
g=r3
h=r5
i=r2+r5+r4
l=numeros[0]+numeros[1]+numeros[2]+numeros[3]+numeros[4]+numeros[5]+numeros[6]

eq1 = sp.Eq(a*x + -b*y - c*z, l)
eq2 = sp.Eq(-d*x + e*y - f*z, 0)
eq3 = sp.Eq(-g*x -h*y + i*z, 0)

# Resolver el sistema de ecuaciones
sol = sp.solve((eq1,eq2,eq3), (x,y,z))
print(sol)

i=sol[x]

resis=l/i
poten=i**2*resis
print("el valor de la corriente es:",i,"A y el valor de la potencia es de:",poten)


