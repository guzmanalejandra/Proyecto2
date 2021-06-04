# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 22:09:26 2021

Questionario



@author: EMenendez

"""
from py2neo import NodeMatcher

def PreguntarUsuario(matcher: NodeMatcher):
    print("¿Cual es el nombre de usuario que quiere utilizar? \n Recuerde que una vez lo elija, este no puede ser cambiado.\n")
    tf= True
    while(tf):
        user= input()
        user_list=[]
        try:
            user_list= list(matcher.match("NUser").where(user))
        except: 
            pass
        if not user_list:
            print("Nombre aceptado.")
            tf=False
        
    return user
def PreguntarContraseña():
    tf= True
    while(tf):
        print("Contraseña:\n")
        pass1= input()
        print("Escriba su contraseña nuevamente: \n")
        pass2 = input()
        if pass1==pass2:
            tf=False
        else:
            print("Contraseñas no coinciden, ingrese us contraseña nuevamente.")
        
    return pass1

def PreguntaSexo():
    print("A continuación se hará una serie de preguntas para saber más de ti,\n contesta con sinceridad  para obtener el mejor resultado posible.")
    tf= True
    while(tf):
        print("¿Cuál es su sexo? Eliga el número de respuesta que mejor lo representa.")
        print("1) Hombre\n 2) Mujer \n 3) Prefiero no decirlo\n")
        sexo= int(input())
        if sexo==1:
            respuesta= "Hombre"
            tf=False
        elif sexo==2:
            respuesta= "Mujer"
            tf=False
        elif sexo==3:
            respuesta== "Prefiero no especificarlo"
            tf=False
        else:
            print("Por favor escribir una opción correcta.\n ")
        
    return respuesta

def PreguntaOrientación():
    
    tf= True
    while(tf):
        print("¿Cuál es su orientación sexual? Eliga el número de respuesta que mejor lo representa.")
        print("1) Heterosexual \n 2) Homosexual \n 3) Demisexual \n 4) Asexual \n 5) Bisexual \n")
        sexo= int(input())
        if sexo==1:
            respuesta= "Heterosexual"
            tf=False
        elif sexo==2:
            respuesta= "Homosexual"
            tf=False
        elif sexo==3:
            respuesta== "demisexual"
            tf=False
        elif sexo==4:
            respuesta= "Asexual"
            tf=False
        elif sexo==5:
            respuesta== "Bisexual"
            tf=False
        else:
            print("Por favor escribir una opción correcta.")
        
    return respuesta

def PreguntaPareja():
    tf= True
    while(tf):
        print("¿Actualmente tiene pareja? Eliga el número de respuesta que mejor lo representa.")
        print("1) Si \n 2) No \n ")
        sexo= int(input())
        if sexo==1:
            respuesta= "Si"
            tf=False
        elif sexo==2:
            respuesta= "No"
            tf=False
        else:
            print("Por favor escribir una opción correcta.")
        
    return respuesta

def PreguntarApps():
    print("¿Consideras que apps como Tinder, Bumble, Happn, etc son buenas para conseguir una relación formal?")
    print("1. Si\n2. Tal vez\n3. No")
    while True:
        try:
            respuesta = int(input("Digite su respuesta: "))
            if respuesta < 1 or respuesta > 3:
                print("Digite en el rango indicado")
            else:
                break
        except ValueError:
            print("Digite un número entero")


    if respuesta == 1:
        return "Si"
    elif respuesta == 2:
        return "Tal vez"
    else:
        return "No"

def PreguntarCitas():
    print("¿Qué tan difícil es para ti encontrar una cita?\nContestar en un rango del 1 al 5")
    while True:
        try:
            respuesta = int(input("Digite su respuesta: "))
            if respuesta < 1 or respuesta > 5:
                print("Digite en el rango indicado")
            else:
                break
        except ValueError:
            print("Digite un número entero")

    return str(respuesta)

def PreguntarHobbies():
    print("¿Es importante que tengan hobbies similares con tu posible pareja?")
    print("1. Si, es importante\n2. No, no es importante")
    while True:
        try:
            respuesta = int(input("Digite su respuesta: "))
            if respuesta < 1 or respuesta > 2:
                print("Digite en el rango indicado")
            else:
                break
        except ValueError:
            print("Digite un número entero")

    if respuesta == 1:
        return "Si"
    else:
        return "No"

def PreguntarTrabajo():
    print("¿Le parece importante que trabajen/estudien en lugares similares?")
    print("1. Si\n2. No")
    while True:
        try:
            respuesta = int(input("Digite su respuesta: "))
            if respuesta < 1 or respuesta > 2:
                print("Digite en el rango indicado")
            else:
                break
        except ValueError:
            print("Digite un número entero")

    if respuesta == 1:
        return "Si"
    else:
        return "No"

def PreguntarMusica():
    print("¿Le da importancia al gusto musical de una posible pareja?")
    print("1. Si\n2. No")
    while True:
        try:
            respuesta = int(input("Digite su respuesta: "))
            if respuesta < 1 or respuesta > 2:
                print("Digite en el rango indicado")
            else:
                break
        except ValueError:
            print("Digite un número entero")

    if respuesta == 1:
        return "Si"
    else:
        return "No"

def PreguntarRegion():
    print("¿Le da importancia a que su posible pareja sea de su misma región?")
    print("1. Si\n2. No")
    while True:
        try:
            respuesta = int(input("Digite su respuesta: "))
            if respuesta < 1 or respuesta > 2:
                print("Digite en el rango indicado")
            else:
                break
        except ValueError:
            print("Digite un número entero")

    if respuesta == 1:
        return "Si"
    else:
        return "No"
    
def preguntaUsuarioHabitos():
    print("¿Crees que es importante que su pareja tenga buenos hábitos? 1. Si o 2.No")

    while True:
        try:
            ans = int(input("Ingrese su respuesta (1 o 2): "))
            if ans < 1 or ans > 2:
                print("Digite en el rango indicado")
            else:
                break
        except ValueError:
            print("Valor Ingresado Erroneo, intente de nuevo.")
    if ans == 1:
        return "Si"
    else:
        return "No"
def preguntarUsuarioMetas():
    print("¿Cree que es bueno tener metas similares en la vida con su posible pareja? 1. Si o 2.No")
    while True:
        try:
            ans = int(input("Ingrese su respuesta (1 o 2): "))
            if ans < 1 or ans > 2:
                print("Digite en el rango indicado")
            else:
                break
        except ValueError:
            print("Valor Ingresado Erroneo, intente de nuevo.")
    if ans == 1:
        return "Si"
    else:
        return "No"

def preguntarUsuarioProfesional():
    print("¿Considera importante que sus carreras profesionales sean similares? 1.Si o 2.No")
    while True:
        try:
            ans = int(input("Ingrese su respuesta (1 o 2): "))
            if ans < 1 or ans > 2:
                print("Digite en el rango indicado")
            else:
                break
        except ValueError:
            print("Valor Ingresado Erroneo, intente de nuevo.")
    if ans == 1:
        return "Si"
    else:
        return "No"

def preguntarUsuarioGustos():
    print("¿Ha tenido problemas con alguna pareja actual o del pasado por diferencia de gustos, aficiones, hobbies, etc? 1.Si o 2.No")
    while True:
        try:
            ans = int(input("Ingrese su respuesta (1 o 2): "))
            if ans < 1 or ans > 2:
                print("Digite en el rango indicado")
            else:
                break
        except ValueError:
            print("Valor Ingresado Erroneo, intente de nuevo.")
    if ans == 1:
        return "Si"
    else:
        return "No"
        


def preguntarUsuarioDiferente():
    print("¿Cree que tener gustos diferentes en una relación en ocasiones es bueno? 1. Si o 2. No")
    while True:
        try:
            ans = int(input("Ingrese su respuesta (1 o 2): "))
            if ans < 1 or ans > 2:
                print("Digite en el rango indicado")
            else:
                break
        except ValueError:
            print("Valor Ingresado Erroneo, intente de nuevo.")
    if ans == 1:
        return "Si"
    else:
        return "No"

def questionario(matcher: NodeMatcher):
    Usuario = PreguntarUsuario(matcher)
    Contrasena = PreguntarContraseña()
    Sexo = PreguntaSexo()
    OS = PreguntaOrientación()
    Pareja = PreguntaPareja()
    apps = PreguntarApps()
    citas = PreguntarCitas()
    hobbies = PreguntarHobbies()
    trabajo = PreguntarTrabajo()
    musica = PreguntarMusica()
    region = PreguntarRegion()
    habitos = preguntaUsuarioHabitos()
    metas = preguntarUsuarioMetas()
    profesional = preguntarUsuarioProfesional()
    gustos = preguntarUsuarioGustos()
    diferente = preguntarUsuarioDiferente()
    UserDict = {"usuario": Usuario ,"contrasena": Contrasena ,"sexo": Sexo , "orientacion": OS,"tiene_pareja": Pareja ,"app_citas" : apps, "dificultad_citas":citas, "importancia_hobbies":hobbies, "importancia_estudios": trabajo, "gusto_musical":musica, "misma_region": region, "gusto_diferente":diferente, "Buenos_habitos": habitos, "Metas_similares":metas, "vida_profesional":profesional,"gustos_similares": gustos}
    return UserDict
    
    