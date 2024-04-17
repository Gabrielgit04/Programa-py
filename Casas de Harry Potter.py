#variables
gry=0
sly=0
huff=0
rave=0

question="¿Que prefieres el amanecer o anochecer?"
question_2='¿Cuando esté muerto quiero que la gente me recuerde como?'
question_3="¿Que tipo de instrumento le agrada más al oido?"
print(question)

print('1.-Amanecer')
print('2.-Anochecer')

opciones=int(input('Escoge una opcion:'))
if opciones==1:
   print('Perteneces a la casa de Gryffindor o Ravenclaw')
   gryf=gry+1
   raven=rave+1
elif opciones==2:    
     print('Peteneces a la casa de Slytherin o Hufflepuff')
     huffl=huff+1
     slyt=sly+1
else:
    print('Ejecucion fallida')
    
slyt=sly+1
gryf=gry+1
raven=rave+1
huffl=huff+1

       
     
print(question_2)

print("1.-El bueno")
print("2.-El grande")
print("3.-El sabio")
print("4.-El audaz")

opciones=int(input())

if opciones==1:
   slyth=slyt+2
   print('Slytherin +',slyth)
elif opciones==2:
     huffle=huffl+2
     print("Hufflepuff +", huffle)
elif opciones==3:
     ravenc=raven+2
     print('Ravenclaw +', ravenc)
elif opciones==4:
     gryff=gryf+2 
     print ('Gryffindor +', gryff)
else:
     print('Entrada invalida')

ravenc=raven+2          
gryff=gryf+2
huffle=huffl+2
slyth=slyt+2

print(question_3)

print('1.-El violin')
print('2.-La trompeta')
print('3.-El piano')
print('4.-El tambor')

opciones=int(input())

if opciones==1:
   slyth=slyth+4
   print("Slytherin +",slyth)
elif opciones==2:
   ravenc=ravenc+4
   print("Ravenclaw +",ravenc)
elif opciones==3:
   huffle=huffle+4
   print("Hufflepuff +",huffle) 
elif opciones==4:
   gryff=gryff+4
   print("Gryffindor +",gryff)   
else:
    print("Entrada invalida") 
    
mas_puntos= max(gryff,slyth,huffle,ravenc)

print("==========")
print("La casa con más puntos es:")
if mas_puntos==gryff:
   print("Gryffindor")
elif mas_puntos==slyth:
     print("Slytherin")   
elif mas_puntos==ravenc:
     print("Ravenclaw") 
elif mas_puntos==huffle:
     print("Hufflepuff") 
else:
    print("Entrada invalida")              

