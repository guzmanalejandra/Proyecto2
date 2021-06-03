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
    #user = "_.usuario =~ '{:s}.*'".format(str(nombres))
    #contra = "_.contra =~ '{:s}.*'".format(str(contraseña))
    #pareja = "_.tiene_pareja=~ '{:s}'".format("Si")
    lista = list(matcher.match("NUser", usuario= nombres, contra= contraseña))
    print(lista)
    if not lista: 
        Nodo= lista
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
        print("Gracias por usar Play Date.")
    else: 
        print("Usuario no existe, por favor intente de nuevo")

def agregar_usuario(matcher: NodeMatcher):
    userDict = questionario(matcher)
    database.generate_user(userDict)

def eliminaruser(matcher: NodeMatcher ):
      tf = True
      while (tf): 
            
            nombres=input("Ingrese el usuario que desea eliminar: ")
            
            user_list = list(matcher.match("Nuser").where(nombres))
            if not user_list:
                  print("Este usuario no existe, intente de nuevo para eliminar")
            else: 
                  
                  contra =input("Ingrese contraseña:")
                  user_list2= list(matcher.match("Nuser").where(nombres).where(contra))
                  if not user_list2:
                      print("Esta contraseña es incorrecta, intente de nuevo para eliminar")
                  else:
                        database.deleteUser(nombres, contra, matcher)
                        tf=False
    
print("Bienvenida,  puta")
tf=True
database.db.delete_all()
database.generateDatabase()
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
        print("Elija una opción correcta, puta.")
print("gracias, puta")
