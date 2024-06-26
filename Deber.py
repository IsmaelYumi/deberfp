lUserPass = ["jmoran-Jm45e", "mflores-blacK2009", "rrodriguez-1234abc", "eperez-paS$word", "lgonzalez-letmein"]
#Literal B
def Menuprincipal():
  validar =True
  while(validar==True): 
   print("Menú Principal")
   print("C: Cambio de Clave")
   print("R: Registrar Vuelo")
   print("B: Buscar Vuelos")
   print("S: Salir")
   opcion=input("Ingrese la opción deseada: ").strip().upper()
   if(opcion not in ["C", "R", "B", "S"]):
     print("Opcion no valida")
   else:
     validar=False
     return opcion
#Literal C
def Cambio_clave(contra, ListaU):
  validacion=False
  validacion2=False
  validacion3=False
  clave=input("Ingrese su actual clave: ")
  if(clave==contra):
    print("Para su nueva clave debe seguir los siguientes parametros:")
    print("1..Debe tener al menos una letra")
    print("2..Debe tener al menos un numero")
    print("3..Debee tener al menos 5 carcateres")
    nclave=input("Ingrese su nueva clave: ")
    for carcater in nclave:
      if(carcater.isupper()==True):
        validacion=True
        break
    if(validacion==True):
      for carcater in nclave:
        if(carcater.isdigit()==True):
          validacion2=True
          break
    else:
      print("Error en la clave, falta mayuscula")
    if validacion2==True:
      if(len(nclave)>=5):
        validacion3=True
        print("sI ENTRA3")
    if(validacion==True and validacion2==True and validacion3==True):
      print("si entra4")
      for index in range(len(ListaU)):
        usuario,con=ListaU[index].split("-")
        if(con.strip()==contra):
          ListaU[index]= usuario + "-" + nclave
          print( "clave cambiada con exito")
    else:
     print("Clave incorrecta")
#Literal D
def registrar_vuelo(lAerolinea, lOrigen, lDestino, lCodigo, lFecha, lHora, lPrecio, lCantidad):
    ciudades = ["Guayaquil", "Quito", "Cuenca"]
    while True:
        aerolinea = input("Ingrese el nombre de la aerolínea: ").strip()
        lAerolinea.append(aerolinea)
        # Solicitar ciudad origen
        while True:
            origen = input("Ingrese la ciudad de origen ")
            if origen in ciudades:
                lOrigen.append(origen)
                break
            else:
                print("Ciudad de origen inválida. Intente de nuevo.")
        # Solicitar ciudad destino
        while True:
            destino = input(f"Ingrese la ciudad de destino ").strip().title()
            if destino in ciudades and destino != origen:
                lDestino.append(destino)
                break
            else:
                print("Ciudad de destino inválida o igual a la ciudad de origen. Intente de nuevo.")
        # Solicitar código de vuelo
        while True:
            codigo = input("Ingrese el código de vuelo (5 caracteres): ").strip().upper()
            if len(codigo) == 5:
                lCodigo.append(codigo)
                break
            else:
                print("El código de vuelo debe tener exactamente 5 caracteres. Intente de nuevo.")
        # Solicitar fecha de vuelo
        while True:
            fecha = input("Ingrese la fecha de vuelo (formato aaaa/mm/dd): ").strip()
            for caracter in fecha:
               if(caracter=="/"):
                  lFecha.append(fecha)
                  break
        while True:
            hora = input("Ingrese la hora de despegue (formato hh:mm): ").strip()
            for caracter in hora:
               if(caracter==":"):
                  lHora.append(hora)
                  break
        # Solicitar precio
        while True:
            precio_str = input("Ingrese el precio del vuelo: ").strip()
            if precio_str.isdigit() and int(precio_str) > 0:
                precio = int(precio_str)
                lPrecio.append(precio)
                break
            else:
                print("Precio inválido. Debe ser un número entero mayor a cero. Intente de nuevo.")

        # Solicitar cantidad de asientos disponibles
        while True:
            cantidad_str = input("Ingrese la cantidad de asientos disponibles: ").strip()
            if cantidad_str.isdigit() and int(cantidad_str) > 0:
                cantidad = int(cantidad_str)
                lCantidad.append(cantidad)
                break
            else:
                print("Cantidad inválida. Debe ser un número entero mayor a cero. Intente de nuevo.")
def Buscar(lAerolinea, lOrigen, lDestino, lCodigo, lFecha, lHora, lPrecio, lCantidad):
   print("\nMenú Buscar")
   print("O: Ciudad de Origen")
   print("D: Ciudad de Destino")
   print("F: Fecha")
   print("V: Volver")
   opcion = input("Ingrese la opción deseada: ").strip().upper()
   if(opcion=="O"):
      for ciudad in lOrigen:

intentos=0
validar=True
Aerolineas=[]
Origen=[]
Destino=[]
Codigo=[]
Fechas=[]
horas=[]
precios=[]
cantidad=[]
#Literal A
while(intentos<3):
  usuario = input("Ingrese su usuario: ")
  contrasena = input("Ingrese su contraseña: ")
  if usuario + "-" + contrasena in lUserPass:
    continuar=input("Presiona el enter para continuar")
    while(True):
      opcion=Menuprincipal()
      if(opcion=="C"):
        Cambio_clave(contrasena,lUserPass)
      elif(opcion=="R"):
         registrar_vuelo(Aerolineas,Origen,Destino,Codigo,Fechas,horas,precios,cantidad)
  else:
    print("Usuario incorrecto")
    intentos +=1
  if(intentos==3):
    print("Se acabaron los intentos")

  