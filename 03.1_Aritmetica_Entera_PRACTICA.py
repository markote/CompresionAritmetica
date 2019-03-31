# -*- coding: utf-8 -*-
"""
@author: martinez
"""

import math
import random




#%%
"""
Dado un mensaje y su alfabeto con sus frecuencias dar el código 
que representa el mensaje utilizando precisión infinita (reescalado)

El intervalo de trabajo será: [0,R), R=2**k, k menor entero tal que R>4T

T: suma total de frecuencias

"""


def IntegerArithmeticCode(mensaje,alfabeto,frecuencias):
    T=sum(frecuencias)
    df=dict()
    tmp=zip(alfabeto,frecuencias)
    i = 0
    for t in tmp:
        df[t[0]]=(t[1],i)
        i+=1
    
    i = 0
    while not (pow(2,i) > 4*T):
        i+=1
    bits=i
    R=pow(2,i)
    print("R:",R,"bits:",bits)
    print("dict:",df)
    l=0
    u=R-1
    result=""
    scale3 = 0
    print("u:",u," l:",l)
    for c in mensaje:
        freq,it=df[c]
        l=l+int((u-l+1)*(sum(frecuencias[0:it]))/T)
        u=l-1+int((u-l+1)*(sum(frecuencias[0:it+1]))/T)
        ub="{0:b}".format(u)
        lb="{0:b}".format(l)
        cond=True
        print("u:",u," l:",l)
        while(cond):
            cond=False
            if ub[0]==lb[0]:
                print("E1,E2")
                cond=True
                result=result+ub[0]
                ub=ub+"0"
                lb=lb+"1"
                ub=ub[1:]
                lb=lb[1:]
                print("ub:",ub," lb:",lb)
                if result[len(result)-1] == "0" :
                    comp="1"
                else :
                    comp="0"
                while scale3>0 :
                    result=result+comp
                    scale3 = scale3-1
                print("result:",result)
            if ub[1]=="0" and lb[1]=="1" :
                print("E3")
                cond=True
                scale3=scale3+1
                ub[1]="1"
                lb[1]="0"
                ub=ub[1:]+"1"
                lb=lb[1:]+"0"
                print("ub:",ub," lb:",lb)
                 
        u=int(ub,2)
        l=int(lb,2)      
        
    
    lcola="{0:b}".format(l)
    result=result+lcola[0]
    lcola=lcola[1:]

    if result[len(result)-1] == "0":
        comp="1"
    else :
        comp="0"

    for x in range(0,scale3):
        result=result+comp
    
    result=result+lcola
    return result
    
print(IntegerArithmeticCode("1321",["1","2","3"],[2,1,1]))    
#%%
            
            
"""
Dada la representación binaria del número que representa un mensaje, la
longitud del mensaje y el alfabeto con sus frecuencias 
dar el mensaje original
"""
           
#def IntegerArithmeticDecode(codigo,tamanyo_mensaje,alfabeto,frecuencias):

    


             
            
#%%
       




#%%
'''
Definir una función que codifique un mensaje utilizando codificación aritmética con precisión infinita
obtenido a partir de las frecuencias de los caracteres del mensaje.

Definir otra función que decodifique los mensajes codificados con la función 
anterior.
'''

#
#def EncodeArithmetic(mensaje_a_codificar):

#    return mensaje_codificado,alfabeto,frecuencias
    
#def DecodeArithmetic(mensaje_codificado,tamanyo_mensaje,alfabeto,frecuencias):

#    return mensaje_decodificado
        
#%%
'''
Ejemplo (!El mismo mensaje se puede codificar con varios códigos¡)

'''

#lista_C=['010001110110000000001000000111111000000100010000000000001100000010001111001100001000000',
#         '01000111011000000000100000011111100000010001000000000000110000001000111100110000100000000']
#alfabeto=['a','b','c','d']
#frecuencias=[1,10,20,300]
#mensaje='dddcabccacabadac'
#tamanyo_mensaje=len(mensaje)  

#for C in lista_C:
#    mensaje_recuperado=DecodeArithmetic(C,tamanyo_mensaje,alfabeto,frecuencias)
#    print(mensaje==mensaje_recuperado)



#%%

'''
Ejemplo

'''

mensaje='La heroica ciudad dormía la siesta. El viento Sur, caliente y perezoso, empujaba las nubes blanquecinas que se rasgaban al correr hacia el Norte. En las calles no había más ruido que el rumor estridente de los remolinos de polvo, trapos, pajas y papeles que iban de arroyo en arroyo, de acera en acera, de esquina en esquina revolando y persiguiéndose, como mariposas que se buscan y huyen y que el aire envuelve en sus pliegues invisibles. Cual turbas de pilluelos, aquellas migajas de la basura, aquellas sobras de todo se juntaban en un montón, parábanse como dormidas un momento y brincaban de nuevo sobresaltadas, dispersándose, trepando unas por las paredes hasta los cristales temblorosos de los faroles, otras hasta los carteles de papel mal pegado a las esquinas, y había pluma que llegaba a un tercer piso, y arenilla que se incrustaba para días, o para años, en la vidriera de un escaparate, agarrada a un plomo. Vetusta, la muy noble y leal ciudad, corte en lejano siglo, hacía la digestión del cocido y de la olla podrida, y descansaba oyendo entre sueños el monótono y familiar zumbido de la campana de coro, que retumbaba allá en lo alto de la esbeltatorre en la Santa Basílica. La torre de la catedral, poema romántico de piedra,delicado himno, de dulces líneas de belleza muda y perenne, era obra del siglo diez y seis, aunque antes comenzada, de estilo gótico, pero, cabe decir, moderado por uninstinto de prudencia y armonía que modificaba las vulgares exageraciones de estaarquitectura. La vista no se fatigaba contemplando horas y horas aquel índice depiedra que señalaba al cielo; no era una de esas torres cuya aguja se quiebra desutil, más flacas que esbeltas, amaneradas, como señoritas cursis que aprietandemasiado el corsé; era maciza sin perder nada de su espiritual grandeza, y hasta sussegundos corredores, elegante balaustrada, subía como fuerte castillo, lanzándosedesde allí en pirámide de ángulo gracioso, inimitable en sus medidas y proporciones.Como haz de músculos y nervios la piedra enroscándose en la piedra trepaba a la altura, haciendo equilibrios de acróbata en el aire; y como prodigio de juegosmalabares, en una punta de caliza se mantenía, cual imantada, una bola grande debronce dorado, y encima otra más pequenya, y sobre ésta una cruz de hierro que acababaen pararrayos.'
#mensaje_codificado,alfabeto,frecuencias=EncodeArithmetic(mensaje)
#mensaje_recuperado=DecodeArithmetic(mensaje_codificado,len(mensaje),alfabeto,frecuencias)

#ratio_compresion=8*len(mensaje)/len(mensaje_codificado)
#print(ratio_compresion)

#if (mensaje!=mensaje_recuperado):
#        print('!!!!!!!!!!!!!!  ERROR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        
        
