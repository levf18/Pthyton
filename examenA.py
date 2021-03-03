# En una llantera se ha establecido una promoción de las llantas marca
# Ponchadas, dicha promoción consiste en lo siguiente: Si se compran menos
# de cinco llantas el precio es de $300 cada una, de $250 si se compran de
# cinco a 10 y de $200 si se compran más de 10. Obtener la cantidad de dinero
# que una persona tiene que pagar por cada una de las llantas que compra y la
# que tiene que pagar por el total de la compra.
print('Bienvenidos a nuestra llanteria')
print('hoy estamos tirando la casa por la ventana')
print('tenemos los mejores precios y promociones')
print('en las llantas marca Ponchadas')
cantidad = int(input('Ingrese la cantidad de llantas que desea comprar: '))
if cantidad < 5:
    precio = 300
    total = precio * cantidad
elif cantidad >= 5 and cantidad <= 10:
    precio = 250
    total = precio * cantidad
else:
    precio = 200
    total = precio * cantidad
print(f'Usted compro {cantidad} llantas')
print(f'El precio unitario es de ${precio:,}')
print(f'El total a pagar es de ${total:,}')
# Hacer algoritmo que de el valor final por la compra de televisores. El
# descuento lo hace basado en los dos numeros finales a la cédula, si
# termina en 01 el descuento es del 10% y si termina en 25 el descuento es
# del 20%, si termina en 44 el descuento es 35% y si es 57 el 50%.
print('Bienvenido')
print('como nos gusta consentir a nuestros clientes')
print('hoy estamos ofreciendo descuentos en nuestros televisores')
cedula = input('Ingrese los dos ultimos digitos de su cedula: ')
precio = float(input('Ingrese el valor del televisor: '))
descuento = 0
if cedula == '01':
    descuento = precio * 0.1
elif cedula == '25':
    descuento = precio * 0.2
elif cedula == '44':
    descuento = precio * 0.35
elif cedula == '57':
    descuento = precio * 0.5
else:
    print('Su cedula no aplica en la promoción')
total = precio - descuento
print(f'Su descuento fue de ${descuento:,}')
print(f'El total a pagar es de ${total:,}')
# Ejercicio 3
print('Bienvenidos')
cantidad = int(input('Ingrese la cantidad de colchones que desea comprar: '))
precio = float(input('Ingrese el valor del televisor: '))
subtotal = precio * cantidad
descuento = 0
if cantidad < 3:
    descuento = subtotal * 0
elif cantidad >= 3 and cantidad < 6:
    descuento = subtotal * 0.2
elif cantidad >= 6 and cantidad < 8:
    descuento = subtotal * 0.25
else:
    descuento = subtotal * 0.3
total = subtotal - descuento
print(f'Su descuento es ${descuento:,}')
print(f'El total a pagar es de ${total:,}')
# Una universidad desea seleccionar una muestra de estudiantes para
# realizar una encuesta. Si el número de estudiantes es menor que 20 se
# tomará el 50%, si el salón tiene entre 20 y 30 estudiantes se tomará 60%,
# si la cantidad es mayor a 30 tomará 70%. ¿Que cantidad de estudiantes
# serán seleccionados para la encuesta?.
print('Bienvenidos a su universidad en casa')
cantidad = int(input('Ingrese el numero de estudiantes en su salon: '))
if cantidad < 20:
    estudiantes = cantidad * 0.5
elif cantidad >= 20 and cantidad < 30:
    estudiantes = cantidad * 0.6
else:
    estudiantes = cantidad * 0.7
print(f'La cantidad de estudiantes encuestados fue de {estudiantes}%')
