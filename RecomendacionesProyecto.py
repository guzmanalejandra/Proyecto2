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
    appsPreferidas = user_preferences["app_citas"]
    equal_styles = list(matcher.match("User", apps = appsPreferidas))
    return equal_styles


def similarRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based if the users likes dating apps or not
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    similarE = user_preferences["gustos_similares"]
    equal_styles = list(matcher.match("User",similar = similarE))
    return equal_styles


def profesionalRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based if the users likes dating apps or not
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    profesional = user_preferences["vida_profesional"]
    equal_styles = list(matcher.match("User", prof = profesional))
    return equal_styles


def goalsRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based if the users likes dating apps or not
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    goalsE = user_preferences["Metas_similares"]
    equal_styles = list(matcher.match("User", goals = goalsE))
    return equal_styles


def difficultydates(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based if the users has difficulty on finding a date
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    dates = user_preferences["dificultad_citas"]
    equal_styles = list(matcher.match("User"), dificultad = dates)
    return equal_styles


def musictaste(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    music = user_preferences["gusto_musical"]
    equal_styles = list(matcher.match("User", gusto = music))
    return equal_styles


def sameregion(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    regionE = user_preferences["misma_region"]
    equal_styles = list(matcher.match("User", region = regionE))
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
    hobbies = user_preferences["importancia_hobbies"]
    equal_styles = list(matcher.match("User", importancia = hobbies))
    return equal_styles


def different(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    likes = user_preferences["gusto_diferente"]
    equal_styles = list(matcher.match("User", gustoDif = likes))
    return equal_styles


def habits(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    goodhabits = user_preferences["Buenos_habitos"]
    equal_styles = list(matcher.match("User", Habits = goodhabits))
    return equal_styles


def ParejaRecommendation(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    parejaE = user_preferences["tiene_pareja"]
    equal_styles = list(matcher.match("User", pareja = parejaE))
    return equal_styles


def study(user_preferences: dict, matcher: NodeMatcher):
    """Calculates a recommendation based users choice
    Args:
        *user_preferences (dict)
        *matcher (NodeMatcher)
    Returns:
        **
    """
    studysame = user_preferences["importancia_estudios"]
    equal_styles = list(matcher.match("User", imp = studysame))
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
    pareja = ParejaRecommendation(dict, matcher)
    apps = likingdatingapps(dict, matcher)
    dificultad = difficultydates(dict, matcher)
    importancia = samehobbies(dict, matcher)
    imp = study(dict, matcher)
    gusto = musictaste(dict, matcher)
    region = sameregion(dict, matcher)
    gustoDif = different(dict, matcher)
    Habits = habits(dict, matcher)
    goals = goalsRecommendation(dict, matcher)
    prof = profesionalRecommendation(dict, matcher)
    similar = similarRecommendation(dict, matcher)

    listaopciones = [pareja, apps, dificultad, importancia, imp, gusto, region, gustoDif, Habits, goals, prof, similar]

    Prospectos = {}
    for option in listaopciones:
        for element in option:
            if Prospectos.has_key(element["nombre"]):
                Prospectos[element["nombre"]] = 1
            else:
                Prospectos[element["nombre"]] = Prospectos[element["nombre"]] + 1