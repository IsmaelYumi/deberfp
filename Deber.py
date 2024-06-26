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
   opcion = input("Ingrese la opción deseada: ").strip().upper()
   if(opcion!="C" or opcion!="C" or opcion!="C"or opcion!="C" ):
     print("Opcion no valida")
   else:
     validar =False
     return opcion
def Cambio_clave(contra, ListaU):
  validacion=False
  validacion2=False
  validacion3=False
  clave=input("Ingrese su actual clave")
  if(clave==contra):
    print("Para su nueva clave debe seguir los siguientes parametros:")
    print("1..Debe tener al menos una letra")
    print("2..Debe tener al menos un numero")
    print("3..Debee tener al menos 5 carcateres")
    nclave=input("Ingrese su nueva clave: ")
    for carcater in nclave:
      if(carcater.isupper()):
        validacion=True
    if(validacion==True):
      for carcater in nclave:
        if(carcater.isdigit()):
          validacion2=True
    else:
      print("Error en la clave")
    if validacion2==True:
      if(len(nclave)>=5):
        validacion3==True
    if(validacion==True and validacion2==True and validacion3==True):
      for index in range(len(ListaU)):
        usuario,con=ListaU[index].split("-")
        if(con==contra):
          ListaU[index]= usuario + "-" + nclave
          print( "clave cambiada con exito")
          return True
intentos=0
validar=True
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
  else:
    print("Usuario incorrecto")
    intentos +=1
  if(intentos==3):
    print("Se acabaron los intentos")
  