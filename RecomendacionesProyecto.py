# -*- coding: utf-8 -*-
"""
Created on Sun May 30 04:06:22 2021

@author: EMenendez
"""
from py2neo import NodeMatcher

def likingdatingapps(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based if the users likes dating apps or not
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    equal_styles = list(matcher.match("User", apps=user_preferences["app_citas"] ))
    return equal_styles

def similarRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based if the users likes dating apps or not
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    similar = "_.gustos_similares=~ '{:s}'".format(user_preferences["gustos_similares"])
    equal_styles = list(matcher.match("User").where(similar))
    return equal_styles

def profesionalRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based if the users likes dating apps or not
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    profesional = "_.vida_profesional=~ '{:s}'".format(user_preferences["vida_profesional"])
    equal_styles = list(matcher.match("User").where(profesional))
    return equal_styles

def goalsRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based if the users likes dating apps or not
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    goals = "_.Metas_similares=~ '{:s}'".format(user_preferences["Metas_similares"])
    equal_styles = list(matcher.match("User").where(goals))
    return equal_styles

def difficultydates(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based if the users has difficulty on finding a date 
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    dates = "_.dificultad_citas=~ '{:s}'".format(user_preferences["dificultad_citas"])
    equal_styles = list(matcher.match("User", ))
    return equal_styles

def musictaste(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice 
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    music = "_.dificultad_citas=~ '{:s}'".format(user_preferences["gusto_musical"])
    equal_styles = list(matcher.match("User").where(music))
    return equal_styles

def sameregion(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice 
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    region = "_.misma_region=~ '{:s}'".format(user_preferences["misma_region"])
    equal_styles = list(matcher.match("User").where(region))
    return equal_styles

def samehobbies(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based on the users wanting that their future couple to 
    have similar hobbies 
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    hobbies = "_.hobbies=~ '{:s}'".format(str(user_preferences["importancia_hobbies"]))
    equal_styles = list(matcher.match("Character").where(hobbies))
    return equal_styles

def different(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice 
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    likes = "_.gusto_diferente=~ '{:s}'".format(user_preferences["gusto_diferente"])
    equal_styles = list(matcher.match("User").where(likes))
    return equal_styles

def habits(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice 
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    goodhabits = "_.buenos_habitos=~ '{:s}'".format(user_preferences["buenos_habitos"])
    equal_styles = list(matcher.match("User").where(goodhabits))
    return equal_styles

def ParejaRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice 
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    pareja = "_.tiene_pareja=~ '{:s}'".format(user_preferences["tiene_pareja"])
    equal_styles = list(matcher.match("User").where(pareja))
    return equal_styles

def study(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice 
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    studysame = "_.importancia_estudios=~ '{:s}'".format(user_preferences["importancia_estudios"])
    equal_styles = list(matcher.match("User").where(studysame))
    return equal_styles

def mainRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based on the player's responses (when none matches an existing character)
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
        *playerExperience (str)
    Returns:
        **
    """
    print("***************************************************\n          Recomendaciones principales\n"
          "***************************************************")
    pareja= ParejaRecommendation(dict, matcher)
    apps = likingdatingapps(dict, matcher)
    dificultad= difficultydates(dict, matcher)
    importancia = samehobbies(dict, matcher)
    imp= study(dict, matcher)
    gusto = musictaste(dict, matcher)
    region= sameregion(dict, matcher)
    gustoDif = different(dict, matcher)
    Habits= habits(dict, matcher)
    goals = goalsRecommendation(dict, matcher)
    prof= profesionalRecommendation(dict, matcher)
    similar = similarRecommendation(dict, matcher)
    
    listaopciones=[pareja, apps, dificultad, importancia, imp, gusto, region, gustoDif, Habits, goals, prof, similar]
    
    Prospectos={}
    for option in listaopciones:
        for element in option: 
            if Prospectos.has_key(element["nombre"]):
                Prospectos[element["nombre"]]=1
            else : 
                Prospectos[element["nombre"]]=Prospectos[element["nombre"]]+1
    
    
