print("************************** Ejemplo 1 ********************************\n")
#Declaramos una variable
calificacion = int(input("Introduce tu calificación de la AZ-900: "))
#Preguntamos si la calificación es menor a 700
if calificacion < 700:
    print("Ves, por no estudiar.") #Si la calificación es menor que 700, muestro esto
elif calificacion > 1000:
    print("¡MIENTES! No puedes sacar mas de 1000") #Si la calificación es menor que 700, muestro esto
else : #Si no se cumple el if anterior, pasa esta línea.
    print("Felicidades, pasa por tu certificado.") #Se ejecut se ninguno de los if se cumple



print("\n************************** Ejemplo 2 ********************************\n")
#Verificación de mayoría de edad
edad = input("Introduce tu edad: ")
edad = int(edad)

if edad >= 18 and edad <= 100:
    print("¡Bienveni@ al mamitas!")
elif edad > 100:
    print("Si vienes con tus abuelitos si te podemos fiar")
elif edad < 0:
    print("Ni que fueras viajero del tiempo")
else :
    print("No puedes llevarte esos cigarros")
