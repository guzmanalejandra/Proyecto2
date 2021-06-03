# -*- coding: utf-8 -*-
"""
Created on Sat May 29 22:36:01 2021

@author: EMenendez
"""
import csv
from py2neo import Graph, Node, Relationship, NodeMatcher
import numpy as np
import pandas as pd

db = Graph("bolt://localhost:7687", auth=("neo4j", "1234"))


# Node matcher
matcher = NodeMatcher(db)
data = pd.read_csv('BaseDatos.csv', sep=';', header=0)


def generateDatabase():
    """Generates Neo4j database for Smash Bros. Main recommendation system
    Args:
        **
    Returns:
        **
    """
    # we open the csv file and create a dictionary of key = character names and value = list with attributes
    with open('BaseDatos.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print(csv_reader)
        userDict = {}

        for row in csv_reader:
            print(row)
            try:
                userDict[row[0]] = [row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                                    row[11], row[12], row[13], row[14], row[15]]
            except IndexError:
                pass
    # we need to know which category each character belongs to
    for user in userDict:
        nombre = userDict[user][0]
        sexo = userDict[user][1]
        os = userDict[user][2]
        pareja = userDict[user][3]
        apps = userDict[user][4]
        dificultad = userDict[user][5]
        importancia = userDict[user][6]
        imp = userDict[user][7]
        gusto = userDict[user][8]
        region = userDict[user][9]
        gustoDif = userDict[user][10]
        Habits = userDict[user][11]
        goals = userDict[user][12]
        prof = userDict[user][13]
        similar = userDict[user][14]
        userDict[user] = Node("User", nombre=userDict[user][0],
                              sexo=userDict[user][1],
                              os=userDict[user][2], pareja=userDict[user][3],
                              apps=userDict[user][4], dificultad=userDict[user][5],
                              importancia=userDict[user][6], imp=userDict[user][7],
                              gusto=userDict[user][8], region=userDict[user][9],
                              gustoDif=userDict[user][10], Habits=userDict[user][11],
                              goals=userDict[user][12], prof=userDict[user][13],
                              similar=userDict[user][14])
        # Tiene pareja o no tiene pareja
        if pareja == "Si":
            db.create(Relationship(userDict[user], "tiene_pareja", siPareja))
        elif pareja == "No":
            db.create(Relationship(userDict[user], "tiene_pareja", noPareja))

        # Considera buenas las aplicaciones de citas
        if apps == "Si":
            db.create(Relationship(userDict[user], "app_citas", siApps))
        elif apps == "Tal vez":
            db.create(Relationship(userDict[user], "app_citas", tvApps))
        elif apps == "No":
            db.create(Relationship(userDict[user], "app_citas", noApps))

        # Dificultad para encontrar citas
        if dificultad == "1":
            db.create(Relationship(userDict[user], "dificultad_citas", unoDif))
        elif dificultad == "2":
            db.create(Relationship(userDict[user], "dificultad_citas", dosDif))
        elif dificultad == "3":
            db.create(Relationship(userDict[user], "dificultad_citas", tresDif))
        elif dificultad == "4":
            db.create(Relationship(userDict[user], "dificultad_citas", cuatroDif))
        elif dificultad == "5":
            db.create(Relationship(userDict[user], "dificultad_citas", cincoDif))

        # Importancia en igualdad de hobbies
        if importancia == "Si, si es importante":
            db.create(Relationship(userDict[user], "importancia_hobbies", siImportancia))
        elif importancia == "No, no es importante":
            db.create(Relationship(userDict[user], "importancia_hobbies", noImportancia))

        # Importancia de trabajar o estudiar en lugares similares
        if imp == "Si":
            db.create(Relationship(userDict[user], "importancia_estudios", siImporta))
        elif imp == "No":
            db.create(Relationship(userDict[user], "importancia_estudios", noImporta))

        # Importancia Gusto musical
        if gusto == "Si":
            db.create(Relationship(userDict[user], "gusto_musical", siGusto))
        elif gusto == "No":
            db.create(Relationship(userDict[user], "gusto_musical", noGusto))

        # Misma región
        if region == "Si":
            db.create(Relationship(userDict[user], "misma_region", siRegion))
        elif region == "No":
            db.create(Relationship(userDict[user], "misma_region", noRegion))

        # Gustos diferentes es bueno
        if gustoDif == "Si":
            db.create(Relationship(userDict[user], "gusto_diferente", siDiferente))
        elif gustoDif == "No":
            db.create(Relationship(userDict[user], "gusto_diferente", noDiferente))
        # Good Habits
        if Habits == "Si":
            db.create(Relationship(userDict[user], "Buenos_habitos", goodhabits))
        elif Habits == "No":
            db.create(Relationship(userDict[user], "Buenos_habitos", Nogoodhabits))

        # Goals
        if goals == "Si":
            db.create(Relationship(userDict[user], "Metas_similares", Goals))
        elif goals == "No":
            db.create(Relationship(userDict[user], "Metas_similares", nogoals))

        # Profesional life
        if prof == "Si":
            db.create(Relationship(userDict[user], "vida_profesional", yesprof))
        elif prof == "No":
            db.create(Relationship(userDict[user], "vida_profesional", noprof))

        # Similar
        if similar == "Si":
            db.create(Relationship(userDict[user], "gustos_similares", Similar))
        elif similar == "No":
            db.create(Relationship(userDict[user], "gustos_similares", nosimilar))


def generate_user(user_preferences: dict):
    user = Node("NUser", usuario=user_preferences["usuario"], contra=user_preferences["contrasena"],
                sexo=user_preferences["sexo"]
                , orientacion=user_preferences["orientacion"], tiene_pareja=user_preferences["tiene_pareja"],
                app_citas=user_preferences["app_citas"]
                , dificultad_citas=user_preferences["dificultad_citas"],
                importancia_hobbies=user_preferences["importancia_hobbies"]
                , importancia_estudios=user_preferences["importancia_estudios"],
                gusto_musical=user_preferences["gusto_musical"]
                , misma_region=user_preferences["misma_region"], gusto_diferente=user_preferences["gusto_diferente"]
                , buenos_habitos=user_preferences["Buenos_habitos"], metas_similares=user_preferences["Metas_similares"]
                , vida_profesional=user_preferences["vida_profesional"],
                gustos_similares=user_preferences["gustos_similares"])

    db.create(user)

    # Tiene pareja
    if user_preferences["tiene_pareja"] == "Si":
        db.create(Relationship(user, "tiene_pareja", siPareja))
    elif user_preferences["tiene_pareja"] == "No":
        db.create(Relationship(user, "tiene_pareja", noPareja))

    # Considera buenas las aplicaciones de citas
    if user_preferences["app_citas"] == "Si":
        db.create(Relationship(user, "app_citas", siApps))
    elif user_preferences["app_citas"] == "Tal vez":
        db.create(Relationship(user, "app_citas", tvApps))
    elif user_preferences["app_citas"] == "No":
        db.create(Relationship(user, "app_citas", noApps))

    # Dificultad para encontrar citas
    if user_preferences["dificultad_citas"] == "1":
        db.create(Relationship(user, "dificultad_citas", unoDif))
    elif user_preferences["dificultad_citas"] == "2":
        db.create(Relationship(user, "dificultad_citas", dosDif))
    elif user_preferences["dificultad_citas"] == "3":
        db.create(Relationship(user, "dificultad_citas", tresDif))
    elif user_preferences["dificultad_citas"] == "4":
        db.create(Relationship(user, "dificultad_citas", cuatroDif))
    elif user_preferences["dificultad_citas"] == "5":
        db.create(Relationship(user, "dificultad_citas", cincoDif))

    # Importancia en igualdad de hobbies
    if user_preferences["importancia_hobbies"] == "Si, si es importante":
        db.create(Relationship(user, "importancia_hobbies", siImportancia))
    elif user_preferences["importancia_hobbies"] == "No, no es importante":
        db.create(Relationship(user, "importancia_hobbies", noImportancia))

    # Importancia de trabajar o estudiar en lugares similares
    if user_preferences["importancia_estudios"] == "Si":
        db.create(Relationship(user, "importancia_estudios", siImporta))
    elif user_preferences["importancia_estudios"] == "No":
        db.create(Relationship(user, "importancia_estudios", noImporta))

    # Importancia gustos musicales
    if user_preferences["gusto_musical"] == "Si":
        db.create(Relationship(user, "gusto_musical", siGusto))
    elif user_preferences["gusto_musical"] == "No":
        db.create(Relationship(user, "gusto_musical", noGusto))

    # Misma región
    if user_preferences["misma_region"] == "Si":
        db.create(Relationship(user, "misma_region", siRegion))
    elif user_preferences["misma_region"] == "No":
        db.create(Relationship(user, "misma_region", noRegion))

    # Gustos diferentes es bueno
    if user_preferences["gusto_diferente"] == "Si":
        db.create(Relationship(user, "gusto_diferente", siDiferente))
    elif user_preferences["gusto_diferente"] == "No":
        db.create(Relationship(user, "gusto_diferente", noDiferente))

    # Buenos habitos
    if user_preferences["Buenos_habitos"] == "Si":
        db.create(Relationship(user, "gusto_diferente", goodhabits))
    elif user_preferences["Buenos_habitos"] == "No":
        db.create(Relationship(user, "gusto_diferente", Nogoodhabits))

    # Metas en la vida
    if user_preferences["Metas_similares"] == "Si":
        db.create(Relationship(user, "Metas_similares", Goals))
    elif user_preferences["Metas_similares"] == "No":
        db.create(Relationship(user, "Metas_similares", nogoals))

    # Vida Profesional
    if user_preferences["vida_profesional"] == "Si":
        db.create(Relationship(user, "vida_profesional", yesprof))
    elif user_preferences["vida_profesional"] == "No":
        db.create(Relationship(user, "vida_profesional", noprof))

    # Similar
    if user_preferences["gustos_similares"] == "Si":
        db.create(Relationship(user, "gustos_similares", Similar))
    elif user_preferences["gustos_similares"] == "No":
        db.create(Relationship(user, "gustos_similares", nosimilar))

    return user_preferences


def deleteUser(nombre: str, contraseña: str, matcher: NodeMatcher):
    try:
        db.delete(matcher.match("NUser").where(nombre).where(contraseña))
    except:
        print("Usuario o contraseña incorrecto")


def leer_archivo(ruta: str, n: int):
    archivo = open(ruta, encoding='latin-1')
    lector = archivo.read()
    datos = lector.split("\n")
    try:
        for i in range(0, len(datos)):
            l = datos[i].split(",")
            if len(l) != n:
                datos.pop(i)
    except IndexError:
        pass

    return datos

def diccionario_archivo(ruta: str, diccionario: dict):
    valores = list(diccionario.values())
    lista_datos = leer_archivo(ruta, len(valores))
    strValor = ",".join(valores)
    lista_datos.append(strValor)
    escribir = "\n".join(lista_datos)
    try:
        archivo_w = open(ruta, 'r+')
    except PermissionError:
        print("Cierre su archivo")

    try:
        archivo_w.write(escribir)
    except PermissionError:
        print("Cierre su archivo")
    archivo_w.close()

def generateNUsers():
    """Generates Neo4j database for Smash Bros. Main recommendation system
    Args:
        **
    Returns:
        **
    """
    # we open the csv file and create a dictionary of key = character names and value = list with attributes
    with open('BaseDatos4.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print(csv_reader)
        userDict = {}

        for row in csv_reader:
            print(row)
            try:
                userDict[row[0]] = [row[0], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10],
                                    row[11], row[12], row[13], row[14], row[15]]
            except IndexError:
                pass
    # we need to know which category each character belongs to
    for user in userDict:
        nombre = userDict[user][0]
        sexo = userDict[user][1]
        os = userDict[user][2]
        pareja = userDict[user][3]
        apps = userDict[user][4]
        dificultad = userDict[user][5]
        importancia = userDict[user][6]
        imp = userDict[user][7]
        gusto = userDict[user][8]
        region = userDict[user][9]
        gustoDif = userDict[user][10]
        Habits = userDict[user][11]
        goals = userDict[user][12]
        prof = userDict[user][13]
        similar = userDict[user][14]
        userDict[user] = Node("NUser", nombre=userDict[user][0],
                              sexo=userDict[user][1],
                              os=userDict[user][2], pareja=userDict[user][3],
                              apps=userDict[user][4], dificultad=userDict[user][5],
                              importancia=userDict[user][6], imp=userDict[user][7],
                              gusto=userDict[user][8], region=userDict[user][9],
                              gustoDif=userDict[user][10], Habits=userDict[user][11],
                              goals=userDict[user][12], prof=userDict[user][13],
                              similar=userDict[user][14])
        # Tiene pareja o no tiene pareja
        if pareja == "Si":
            db.create(Relationship(userDict[user], "tiene_pareja", siPareja))
        elif pareja == "No":
            db.create(Relationship(userDict[user], "tiene_pareja", noPareja))

        # Considera buenas las aplicaciones de citas
        if apps == "Si":
            db.create(Relationship(userDict[user], "app_citas", siApps))
        elif apps == "Tal vez":
            db.create(Relationship(userDict[user], "app_citas", tvApps))
        elif apps == "No":
            db.create(Relationship(userDict[user], "app_citas", noApps))

        # Dificultad para encontrar citas
        if dificultad == "1":
            db.create(Relationship(userDict[user], "dificultad_citas", unoDif))
        elif dificultad == "2":
            db.create(Relationship(userDict[user], "dificultad_citas", dosDif))
        elif dificultad == "3":
            db.create(Relationship(userDict[user], "dificultad_citas", tresDif))
        elif dificultad == "4":
            db.create(Relationship(userDict[user], "dificultad_citas", cuatroDif))
        elif dificultad == "5":
            db.create(Relationship(userDict[user], "dificultad_citas", cincoDif))

        # Importancia en igualdad de hobbies
        if importancia == "Si, si es importante":
            db.create(Relationship(userDict[user], "importancia_hobbies", siImportancia))
        elif importancia == "No, no es importante":
            db.create(Relationship(userDict[user], "importancia_hobbies", noImportancia))

        # Importancia de trabajar o estudiar en lugares similares
        if imp == "Si":
            db.create(Relationship(userDict[user], "importancia_estudios", siImporta))
        elif imp == "No":
            db.create(Relationship(userDict[user], "importancia_estudios", noImporta))

        # Importancia Gusto musical
        if gusto == "Si":
            db.create(Relationship(userDict[user], "gusto_musical", siGusto))
        elif gusto == "No":
            db.create(Relationship(userDict[user], "gusto_musical", noGusto))

        # Misma región
        if region == "Si":
            db.create(Relationship(userDict[user], "misma_region", siRegion))
        elif region == "No":
            db.create(Relationship(userDict[user], "misma_region", noRegion))

        # Gustos diferentes es bueno
        if gustoDif == "Si":
            db.create(Relationship(userDict[user], "gusto_diferente", siDiferente))
        elif gustoDif == "No":
            db.create(Relationship(userDict[user], "gusto_diferente", noDiferente))
        # Good Habits
        if Habits == "Si":
            db.create(Relationship(userDict[user], "Buenos_habitos", goodhabits))
        elif Habits == "No":
            db.create(Relationship(userDict[user], "Buenos_habitos", Nogoodhabits))

        # Goals
        if goals == "Si":
            db.create(Relationship(userDict[user], "Metas_similares", Goals))
        elif goals == "No":
            db.create(Relationship(userDict[user], "Metas_similares", nogoals))

        # Profesional life
        if prof == "Si":
            db.create(Relationship(userDict[user], "vida_profesional", yesprof))
        elif prof == "No":
            db.create(Relationship(userDict[user], "vida_profesional", noprof))

        # Similar
        if similar == "Si":
            db.create(Relationship(userDict[user], "gustos_similares", Similar))
        elif similar == "No":
            db.create(Relationship(userDict[user], "gustos_similares", nosimilar))

# Tiene pareja o no tiene pareja
siPareja = Node("Tiene_Pareja", name="SiPareja")
noPareja = Node("Tiene_Pareja", name="NoPareja")

# Considera buenas las aplicaciones
siApps = Node("App_Citas", name="SiApps")
tvApps = Node("App_Citas", name="TvApps")
noApps = Node("App_Citas", name="NoApps")

# Dificultad para encontrar citas
unoDif = Node("Dificultad_Citas", name="UnoDif")
dosDif = Node("Dificultad_Citas", name="DosDif")
tresDif = Node("Dificultad_Citas", name="TresDif")
cuatroDif = Node("Dificultad_Citas", name="CuatroDif")
cincoDif = Node("Dificultad_Citas", name="CincoDif")

# Importancia en la igualdad de hobbies
siImportancia = Node("Importancia_Hobbies", name="SiImportancia")
noImportancia = Node("Importancia_Hobbies", name="NoImportancia")

# Importancia de trabajar o estudiar en lugares similares
siImporta = Node("Importancia_Estudios", name="SiImporta")
noImporta = Node("Importancia_Estudios", name="NoImporta")

# Importancia de gusto musical
siGusto = Node("Gusto_Musical", name="SiGusto")
noGusto = Node("Gusto_Musical", name="NoGusto")

# Misma región
siRegion = Node("Misma_Region", name="SiRegion")
noRegion = Node("Misma_Redion", name="NoRegion")

# Gustos diferentes es bueno
siDiferente = Node("Gusto_Diferente", name="SiDiferente")
noDiferente = Node("Gusto_Diferente", name="NoDiferente")

# Problemas por diferencia de gustos
Similar = Node("Gustos_Similares", name="Similar")
nosimilar = Node("Gustos_Similares", name="NoSimilar")

# Carreras profesionales similares
yesprof = Node("Vida_Profesional", name="YesProf")
noprof = Node("Vida_Profesional", name="NoProf")

# Metas similares en la vida
Goals = Node("Metas_Similares", name="Goals")
nogoals = Node("Metas_Similares", name="NoGoals")

# Buenos Hábitos
goodhabits = Node("Buenos_Habitos", name="GoodHabits")
Nogoodhabits = Node("Buenos_Habitos", name="NoGoodHabits")