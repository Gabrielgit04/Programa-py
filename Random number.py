import random

question= input("Question: Te gusta el café?")

Magic_8_ball= random.randint(1,8)

if Magic_8_ball == 1:
    resp='si mani'
elif Magic_8_ball == 2:
    resp='si sapohp'  
elif Magic_8_ball == 3:
    resp='idontknow'   
elif Magic_8_ball == 4:
    resp='tengo la mano vacía si hay una alcancía cuidado que la exploto'
elif Magic_8_ball == 5:
    resp='aro pa' 
elif Magic_8_ball == 6:
    resp='si gonorrea'  
elif Magic_8_ball == 7:
    resp='hey Valencia que' 
elif Magic_8_ball == 8:
    resp='aire' 
else:
    resp='error'
print('Respuesta:' + resp)  
                        