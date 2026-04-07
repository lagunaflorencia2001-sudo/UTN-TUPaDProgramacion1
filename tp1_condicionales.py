#ACTIVIDAD 1
edad = int(input("Ingrese su edad: "))
if edad > 18:
    print ("Eres mayor de edad")
else:
    print("Eres menor de edad")

#ACTIVIDAD 2
nota = float(input("Ingrese su nota: "))
if nota >= 6: 
    print ("Aprobado")
else:
    print("Desaprobado")


#ACTIVIDAD 3
num = int(input("Ingrese un el numero: "))
if num % 2 == 0:
    print("Ha ingresado un numero par")
else: 
    print("No ha ingresado un numero par")

#ACTIVIDAD 4
edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#ACTIVIDAD 5
pasword = input("Ingrese su contraseña: ") 
if len (pasword) >= 8 and len (pasword) <= 14:
    print("Ha ongresado la contraseña")
else: 
    print("Por favor, ingrese su contraseña de 8 a 14 digitos")

#ACTIVIDAD 6
consumo = int(input("Ingrese su consumo mensual: "))
if consumo < 150 :
    print("Consumo bajo")
elif consumo >= 150 and consumo <= 300:
    print("Consumo medio")
elif consumo > 300:
    print("Consumo alto ")
if consumo > 500:
    print("Considere medidas de ahorro energético") 

#ACTIVIDAD 7
palabra = input("Ingrese una palabra: ")
if palabra [-1].lower() in "aeiou": 
    print(f"{palabra}!")
else: 
    print (f"{palabra}")


#ACTIVIDAD 8
nombre = input("Ingrese su nombre: ")
opcion = int(input("Ingrese una opción 1 para todas las letras mayusculas, 2 todo minuscula o 3 la primera letra mayuscula: "))
if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())

#ACTIVIDAD 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud <3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte")
elif magnitud >= 7:
    print ("Extremo")

#ACTIVIDAD 10

hemisferio = input("En que HEMISFERIO te encunetras (N/S): ").upper()
mes = int(input("En que mes se encuentra (1 al 12): "))
dia = int(input("En que dia se encuentra (1 al 31): "))

if (mes == 12 and dia >= 21) or (mes == 1) or (mes == 2) or (mes == 3 and dia <= 20):
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")


elif (mes == 3 and dia >= 21) or (mes == 4) or (mes == 5) or (mes == 6 and dia <= 20):
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")


elif (mes == 6 and dia >= 21) or (mes == 7) or (mes == 8) or (mes == 9 and dia <= 20):
    if hemisferio == "N":
        print("Verano")
    else:
        print("Invierno")


elif (mes == 9 and dia >= 21) or (mes == 10) or (mes == 11) or (mes == 12 and dia <= 20):
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera")


