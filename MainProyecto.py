# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 23:39:04 2021

@author: EMenendez
"""
from py2neo import NodeMatcher, Node
from RecomendacionesProyecto import mainRecommendation
from Questionario import questionario
import BaseDatosProyecto as database

User={}

def EntrarUsuario(nombres: str, contraseña: str, matcher:NodeMatcher):
    lista = list(matcher.match("NUser", usuario= nombres, contra= contraseña))
    if not lista: 
        print("Usuario no existe, por favor intente de nuevo")
    else: 
        Nodo= lista[0]
        userDict={}
        userDict["usuario"] = Nodo["usuario"]
        userDict["contrasena"] = Nodo["contra"]
        userDict["sexo"] = Nodo["sexo"]
        userDict["orientacion"] = Nodo["orientacion"]
        userDict["tiene_pareja"] = Nodo["tiene_pareja"]
        userDict["app_citas"] = Nodo["app_citas"]
        userDict["dificultad_citas"] = Nodo["dificultad_citas"]
        userDict["importancia_hobbies"] = Nodo["importancia_hobbies"]
        userDict["importancia_estudios"] = Nodo["importancia_estudios"]
        userDict["gusto_musical"] = Nodo["gusto_musical"]
        userDict["misma_region"] = Nodo["misma_region"]
        userDict["gusto_diferente"] = Nodo["gusto_diferente"]
        userDict["Buenos_habitos"] = Nodo["buenos_habitos"]
        userDict["Metas_similares"] = Nodo["metas_similares"]
        userDict["vida_profesional"] = Nodo["vida_profesional"]
        userDict["gustos_similares"] = Nodo["gustos_similares"]
        mainRecommendation(userDict, matcher)

def agregar_usuario(matcher: NodeMatcher):
    userDict = questionario(matcher)
    database.generate_user(userDict)
    database.diccionario_archivo("BaseNUsers.csv", userDict)

def eliminaruser(matcher: NodeMatcher ):
      tf = True
      while (tf): 
            
            nombres=input("Ingrese el usuario que desea eliminar:")
            
            user_list = list(matcher.match("NUser", usuario= nombres))
            if not user_list:
                  print("Este usuario no existe, intente de nuevo para eliminar")
            else: 
                  
                  contrase =input("Ingrese contraseña:")
                  user_list2= list(matcher.match("NUser", usuario= nombres, contra= contrase))
                  if not user_list2:
                      print("Esta contraseña es incorrecta, intente de nuevo para eliminar")
                  else:
                        database.deleteUser(nombres, contrase, matcher)
                        database.db.delete_all()
                        database.generateDatabase()
                        database.generateNUsers()
                        tf=False
    
print("Bienvenidx a PlayDate, tu mejor opción para encontrar el amor. ")
tf=True
database.db.delete_all()
database.generateDatabase()
database.generateNUsers()

while (tf):
    print("Que desea hacer?\n1) Crear un nuevo usuario \n2) Ingresar a su cuenta\n3) Eliminar su usuario\n4) Salir")
    respuesta=input()
    if respuesta=="1":
        User=agregar_usuario(database.matcher)
    elif respuesta=="2":
        print("¿Cual es su nombre de usuario?")
        nombre= input()
        print("¿Cual es su contraseña?")
        contra=input()
        EntrarUsuario(nombre, contra, database.matcher)
    elif respuesta=="3": 
        eliminaruser(database.matcher)
    elif respuesta=="4": 
        tf=False
    else: 
        print("Por favor, elija una opción correcta.")
print("Gracias por usar nuestro programa")
