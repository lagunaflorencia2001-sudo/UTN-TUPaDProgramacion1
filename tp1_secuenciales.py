#ACTIVIDAD 1 
print("Hola mundo!")

#ACTIVIDAD 2 
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}!")

#ACTIVIDAD 3
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad en numero: "))
lugar_de_residencia = input("Ingrese su lugar de residencia: ")
print(f"Su nombre es {nombre}, su apellido es {apellido}, tienes {edad} de edad y su lugar de residencia es {lugar_de_residencia}")

#ACTIVIDAD 4 
radio = float(input("Ingrese el radio del circulo: "))
area = 3.14 * radio * radio 
perimetro = 2 *03.14 * radio
print(area)
print(perimetro)

#Actividad 5
segundos = int(input("Ingrese una cantidad de segundos: "))
hora = segundos / 3600

print(hora)

#ACTIVIDAD 6
numero = int(input("Ingrese un numero: "))
for i in range (1, 11):
    print(numero * i )

#ACTIVIDAD 7 
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)

#ACTIVIDAD 8 
peso = float(input("Ingrese su peso en numero en kg: "))
altura = float(input("Ingrese su altura en cm: "))
altura = altura / 100
imc = peso / (altura ** 2)

print(f"Su indice de masa corporal es, {imc}")

#ACTIVIDAD 9 
temperatura = float(input("Ingrese la temperatura actual en grados celcius: "))
fahrenheit = temperatura * 9/5 + 32

print(fahrenheit)

#ACTIVIDAD 10 
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))
promedio = (num1 + num2 + num3) / 3 
print(promedio)