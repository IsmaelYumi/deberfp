lUserPass = ["jmoran-Jm45e", "mflores-blacK2009", "rrodriguez-1234abc", "eperez-paS$word", "lgonzalez-letmein"]
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

intentos=0
while(intentos<3):
  usuario = input("Ingrese su usuario: ")
  contrasena = input("Ingrese su contraseña: ")
  if usuario + "-" + contrasena in lUserPass:
    continuar=input("Presiona el enter para continuar")
    opcion=Menuprincipal()
    

    break
  else:
    print("Usuario incorrecto")
    intentos +=1
  if(intentos==3):
    print("Se acabaron los intentos")
  