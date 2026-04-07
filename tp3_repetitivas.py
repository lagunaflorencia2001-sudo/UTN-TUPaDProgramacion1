#ACTIVIDAD 1

#pdio el nombre del cl
nombre = input("cliente: ").strip()

#valido que el nombre no este vacion y solo contenga letras
while nombre == "" or not nombre.isalpha():
    print("Error solo se permiten letras")
    nombre = input("cliente: ").strip()

#pedimos la cantidad de productos como str
cant_productos = input("Ingrese la cantidad de porductos por favor: ").strip()

#validar que la cantidad sea un entero positivo
while not cant_productos.isdigit() or int(cant_productos) == 0:
    print("Error: solo se permite numero positivo")
    cant_productos = input("Ingrese la cantidad de porductos nuevamente por favor : ").strip()

#covertimos la cantidad a entero una vez validado
cant_productos = int(cant_productos)

#definir variables total_con_descuento y total_sin_descuento
total_sin_descuento = 0
total_con_descuento = 0.0

#crear un bucle para recorrer todos los productos
for i in range (1, cant_productos + 1 ):
    #pedimos precio como str
    precio = input(f"producto {i} - precio: ").strip()

#validar que el precio fuera un entero positivo
    while not precio.isdigit() or int(precio) == 0: 
        print("Error: solo se permiten numero positivo")
        precio = input(f"producto {i} - precio: ").strip()
    #convertir a int una vez validado
    precio = int(precio)

    #preguntamos si aplico descuento
    desc = input("Descuento (S/N): ").strip().lower()

    #valido que solo ingreso s o n
    while desc != "s" and desc != "n": 
        print("Error: ingrese S para si o N para no")
        desc = input("Descuento (S/N): ").strip().lower()

    #sumatoria de los precio sin descuento
    total_sin_descuento += precio
    
    #si la respuesta es si aplico 10% de descuento
    #sino dejo el precio original
    if desc == "s":
        precio_final = precio * 0.9
    else:
        precio_final = precio
    
    #hago la sumatoria de los precios con descuento
    #sino la sumatoria es sin descuento
    total_con_descuento += precio_final

    #imprimo el producto con precio 
    print(f"Producto {i} - precio ${precio_final} ")

#calculo del ahorro
ahorro = total_sin_descuento - total_con_descuento

#calculo del promedio
promedio = total_con_descuento / cant_productos 

#impresio de los resultados 
print()
print(f"total sin descuento: $ {total_sin_descuento}")
print(f"total con descuento: $ {total_con_descuento:.2f}")
print(f"ahorro total: $ {ahorro:.2f}")
print(f"promedio: $ {promedio:.2f}")

print("/////////////////////////////////////////")

#ACTIVIDAD 2 
usuario_correcto = "alumno"
clave_correcta = "python123"
acceso = False
#Debemos realizar por conteo las 3 veces que el usuario intentara
for i in range (1,4):
#avisamos al usuario cuantas veces se permitiran intentar acceder 
   print("El ingreso de usuario y contraseña se permitira en 3 intentos")
   usuario = input(f"intento {i} : Ingresa el usuario: ").strip().lower()
   clave = input("Ingrese la clave: ").strip().lower()
#comparamos si la contraseñ ingresada es igual o distinta a la correcta
   if usuario == usuario_correcto and clave == clave_correcta:
        print("Acceso concedido") 
        acceso = True
        break
   #comparamos si la contraseña es igual a 3 intentos 
   else:
       if i == 3: 
        print("Cuenta bloqueada")
       else:
           pass

#el acceso se abre si es true   
if acceso:
    print("MENU")
    opcion = ""
    clave_nueva = ""
    #abrimos el while con las opciones
        
    while opcion != "4":
        print("1. VER ESTADO DE SUSCRIPCION")
        print("2. CAMBIAR CLAVE")
        print("3. MENSAJE MOTIVACIONAL")
        print("4. SALIR")
       #pemos que inrese la opcion en el menu
        opcion = input("Ingresa la opcion: ").strip()
        #comparamos para que no se ingrese algo que no sea 1.2.3.4
        while opcion == "" or not opcion.isdigit():
            print("Error: Debe ingresar solo números")
            opcion = input("Ingresa la opcion: ").strip()
    
        #pedimos al usuario que ingrese la opcion que quiera
        opcion = input("Ingresa la opcion: ").strip()
        if not opcion.isdigit():
                print("Error: Debe ingresar digitos")
        #se muestran las opciones 
        if opcion == "1": 
            print("Inscrito")
        elif opcion == "2":
            print("Debes ingresar una clave que sea minimo de 6 caracteres")
            #pedios ingresar clave nueva
            clave_nueva = input("Ingrese su clave nueva: ").strip()
            if len(clave_nueva) < 6:
                    print("Error: contraseña corta")
            else:
                confirmacion = input("Confirma la clave: ")
            #comparamos las contraseñas
            if clave_nueva == confirmacion:
                print("se ha modificado con exito")
            else: 
                print("No coiciden")
        elif opcion == "3":
            print("Tu puedes")
        elif opcion == "4":
            pass
        else:
            print("Opcion invalida")

#ACTIVIDAD 3

operador = ""
lunes1 = ""
lunes2 = ""
martes1 = ""
martes2 = ""
opcion = ""
operador = input("Ingrese el nombre del operador: ").strip()

while not operador.isalpha():
    print("Error solo letras")
    operador = input("Ingrese el nombre del operador nuevamente: ").strip()

while opcion != "5":
    print("1. RESERVAR TURNO")
    print("2. CANCELAR TURNO")
    print("3. VER AGENDA DEL DIA")
    print("4. VER RESUMEN GENERAL")
    print("5. CERRAR SISTEMA")

    opcion = input("Ingrese la opcion: ").strip()

    if opcion == "1":
        dia = input(f"Ingrese el dia {lunes1} {martes1}: ")
        nombre = input("Nombre del paciente: ").strip()

        while not nombre.isalpha():
            print("Error: solo se permiten letras")
            nombre = input("Nombre del paciente nuevamente: ").strip()
        
            if dia == lunes1 or nombre == lunes2:
                print("Paciente ya existe")
            elif lunes1 == "":
                lunes1 = nombre
            elif lunes2 == "":
                lunes2 = nombre
            else:
                print("No hay turnos disponibles")

            if opcion == "2":
             nombre: str = input("Ingrese nombre a cancelar: ")

            if nombre == lunes1:
                lunes1 = ""
            elif nombre == lunes2:
                lunes2 = ""
            
            elif opcion == "3":
                dia = input("Dia (1=Lunes, 2=Martes): ")

        if dia == "1":
            print(lunes1, lunes2)
            
        elif opcion == "4":
            print("Lunes:", lunes1, lunes2)
            print("Martes:", martes1, martes2)
        
        elif opcion == "5":
            print("Sistema cerrado")

  
#ACTIVIDAD 4

energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 

agente = input("Nombre del agente: ").strip().lower()

while agente == "" or not agente.isalpha():
        print("Error: solo ingrese letras")
        agente = input("Nombre del agente nuevamente: ").strip().lower()
    
contador = 0
opciones = ""

print("**************menu*************")

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and not alarma:
        print("1. FORZAR CERRADURA")
        print("2. HACKEAR PANEL")
        print("3. DESCANSAR")
        opciones = input("Ingrese el numero del 1 al 3: ").strip()

        while opciones not in ["1", "2", "3"]:
         print("Error: opción inválida")
         opciones = input("Ingrese el numero: ").strip()

        if opciones == "1":
                print("Forzar cerradura")
                contador += 1
                energia -= 20
                tiempo -= 2
                    
                if contador == 3: 
                    alarma = True
                    print("La cerradura trabó")
                    contador = 0
                
                else:
                      if energia <= 40: 
                            num = input("Peligro! Ingrese numero 1 - 3  ").strip()
                            while num not in ["1", "2", "3"]:
                                print("Error")
                                num = input("Ingrese número: ").strip()

                                if num == "3":
                                    alarma = True
                                    print("Se activó la alarma 🚨")

                if not alarma:
                            cerraduras_abiertas += 1


        elif opciones == "2":
              contador += 0
              energia -=10
              tiempo -= 3
              for i in range (4):
                    codigo_parcial += "A"
                    print("Proceso:", codigo_parcial)
              if len(codigo_parcial)>= 8:
                    print("Se abrio cerradura")
                    cerraduras_abiertas += 1
        
        elif opciones == "3":
              contador += 1 
              energia += 15 
              if energia > 100:
                    energia = 100 
              tiempo -=1 

              if alarma: 
                    energia -= 10 

        if cerraduras_abiertas == 3:
              print("Victoria")
        elif energia <= 0 or tiempo <= 0:
              print("Derrota")
        elif alarma == True:
              print("Derrota(bloqueo)")


#ACTIVIDAD 5
vida_gladiador = 100
vida_enemiga = 100
pociones_vida = 3 
daño_ataque_pesado = 15
daño_del_enemigo = 12
turno_gladiador = True

print("+++++++++++BIENVENIDOS AL JUEGO++++++++++++++")

gladiador = input("Nombre del galadiador: ").strip().lower()
while gladiador == "" or not gladiador.isalpha():
    print("Error: solo se permite letras")
    gladiador = input("Nombre del galadiador nuevamente: ").strip().lower()
print("Tienes 100 de vida y pociones tienes 3")


print("****************MENU****************")

curar = 0
rafaga_veloz = 0
opciones = ""
while vida_gladiador > 0 and vida_enemiga > 0:
    print("1. ATAQUE PESADO")
    print("2. RAFAGA VELOZ")
    print("3. CURAR")
    opciones = input("Ingrese un numero de 1 - 3: ").strip()

    while not opciones.isdigit() or int(opciones) < 1 or int(opciones) > 3:
        print("Error: ingrese un número válido (1-3)")
        opciones = input("Ingrese un numero de 1 - 3: ").strip()

    if opciones == "1":
        if vida_enemiga <= 20:
            print("Golpe critico")
            daño = daño_ataque_pesado * 1.5
        else:
            daño = daño_ataque_pesado
        vida_enemiga -= daño
        print("¡Atacaste al enemigo por", daño, "puntos de daño!")

    elif opciones =="2":
            for i in range(1, 4):
                vida_enemiga -= 5
                print("> Golpe", i, "conectado por 5 de daño")
            
    elif opciones == "3":
        if pociones_vida > 0:
           vida_gladiador += 30 
           pociones_vida -= 1
        else: 
           print("No te quedan pociones")
    
    vida_gladiador -= 12
    print("¡El enemigo te atacó por 12 puntos de daño!")



if vida_gladiador > 0: 
    print("victoria", gladiador , "Ha ganado la batalla")
elif vida_gladiador <= 0:
    print("Derrota", gladiador , "Ha perdido la batalla")


