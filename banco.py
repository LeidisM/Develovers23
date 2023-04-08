clave = int(2912)
saldo = 0
opcion_usuario_servicios= 0
clave_ingresada = int(input("Ingrese su clave de 4 digitos "))

while clave_ingresada != clave:
  print("clave ingresada no valida")
  
  clave_ingresada = int(input("Ingrese nuevamente la clave de 4 digitos"))
  
if clave_ingresada == clave:
  print("Bienvenido al sistema, su saldo es: ", saldo)  

while opcion_usuario_servicios!=3:
  print(f"Seleccione la opcion de servicio\n\
Presiona 1 para depositar.\n\
Presiona 2 para retirar.\n\
Presiona 3 para salir.")
  opcion_usuario_servicios=int(input())
  if opcion_usuario_servicios == 1:
    valor_usuario_deposito = int(input("ingrese el  valor a depositar"))
    saldo = saldo + valor_usuario_deposito
    print("su saldo actual es: ", saldo)
    
  elif opcion_usuario_servicios == 2:
    print("seleccione el valor a retirar")
    print ("\n\
Presiona 1 para 300000.\n\
Presiona 2 para 50000.\n\
presiona 3 para otro valor\n\
Presiona 4 para cancelar el retiro.")
    opcion_usuario_retiro = int(input())
    if opcion_usuario_retiro == 1 and saldo >= 300000:
        print("Toma tu dinero, tu saldo actual es $: ",(saldo-30000))
    if opcion_usuario_retiro == 1 and saldo < 300000:
      print("no tienes el suficiente dinero $300.000 para retirar el valor: use la opción depositar.") 
      continue
    
    if opcion_usuario_retiro == 2 and saldo >= 50000:  
        print("Toma tu dinero, tu saldo actual es $: ",(saldo-50000))
    if opcion_usuario_retiro == 2 and saldo < 50000:
        print("no tienes el suficiente dinero $50.000 para retirar el valor: use la opción depositar")
        
    if opcion_usuario_retiro==3:
      valor_usuario_retiro=int(input("Ingrese valor a retirar:"))
      if valor_usuario_retiro <= saldo:
        print("tome su dinero",valor_usuario_retiro," su saldo actual es $ ", (saldo - valor_usuario_retiro))
       
      if valor_usuario_retiro > saldo:
        print("no tienes el suficiente dinero para retirar este valor: $", valor_usuario_retiro, " por favor use la opción depositar.")
      
    if opcion_usuario_retiro == 4:
      print("Ha cancelado su retiro, vuelva pronto")
      
      
      
  else:
    print("Usted ha cancelado la opcion de servicios, feliz día")
    