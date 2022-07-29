
print("Programa para saber si una persona es mayor de edad:")
edad = input("Ingrese su edad: ")
edad = int(edad)
mensaje="La persona es: "

if(edad!=0):
    if(edad>=18):
        mensaje+= "mayor de edad."
    else:
        mensaje+=  "menor de edad."
else:
    mensaje= "Edad inv'alida"
print(mensaje)
