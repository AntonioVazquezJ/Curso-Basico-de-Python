###Tipos de variables que exiten en python.

#String (str) = Cadena de texto.
##Ejemplo 1

print("Esto es un string")
print(type("Esto es un string"))

##Ejemplo 2

nombre = "Juanito"
print(nombre, "- Variable del tipo: ", type(nombre))

#******************************************************************************************
# Enteros (int) = Numeros sin punto decimal.
edad = 54
print(edad, "- Variable del tipo: ", type(21))

#*******************************************************************************************
#Flotantes (float) = Numeros con punto decimal. Este tipo de variable ocupa mas espacio de memoria que uno de tipo entero
pi = 3.1416
print(pi, "- Variable del tipo: ", type(pi))

edad =float(edad) #Cesteo - transformar un tipo de variable a otro
print(edad, "- Variable del tipo: ", type(edad))

edad = float("25")
print(edad, "- Variable del tipo: ", type(edad))

#Nota: no todo se puede transformar como por ejemplo, edad = float(24454kjndkjdnr)

#Ejemplo de diferencia.
print("\n************** Sumatoria de variables **************\n")
edad = 25
edads = "25"
edadf = 25.0

##Solo se pueden sumar variables del mismo tipo.
print(edad + edad)                                  #Esto imprimira 50
print(edads + edads)                                #Esto impimira 2525 (concatenación)
print(edadf + edadf)                                #Esto imprimira 50.0

#Booleanos (bool) = Verdadero o Falso
legusto = False                  #Ni modo carnal
print(legusto, type(legusto))
legusto = True                  #Tienes oportunidad, apurale antes que te la ganen
print(legusto, type(legusto))
