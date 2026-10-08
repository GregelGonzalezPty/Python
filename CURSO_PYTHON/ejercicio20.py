edad= int(input("Ingrese su edad: "))
tiene_entrada = bool(input("Ingrese (True o False): "))

if edad>=16 and tiene_entrada==True:
    print("Puede ingresar")
else:
    print("No puede ingresar")