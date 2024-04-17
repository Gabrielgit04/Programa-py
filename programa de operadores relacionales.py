#programa de viajes
height=float(input("Cuál es su altura?"))
credit=int(input("Ingrese sus créditos:"))
cumple_requisitos='No cumple con los requisitos requeridos'

if height>=1.37 and credit>=10:
   print('Disfrute de su viaje')
    
elif height<1.37 and credit>=10:
     print("No tiene altura suficiente para ir al viaje")

elif credit<10 and height>= 1.37:
     print('No posee créditos suficientes')  
elif height<1.37 or credit<10:
     print(cumple_requisitos)
