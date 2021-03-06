# -*- coding: utf-8 -*-
def degree_to_rhumb(degrees):
    """
    convert degrees to rhumb
    :param degrees:
    """
    i = int((degrees + 11.25) / 22.5)
    result_raw = i % 16
    return result_raw  # meteorological rhumb 1/16 of turn


def rhumb_to_direction(rhumb):
    """
    return direction
    :param rhumb:
    """
    directions = {0: "Северный",
                  1: "Северо-Северо-Восточный",
                  2: "Северо-Восточный",
                  3: "Восточный-Северо-Восточный",
                  4: "Восточный",
                  5: "Восточный-Юго-Восточный",
                  6: "Юго-Восточный",
                  7: "Юго-Юго-Восточный",
                  8: "Южный",
                  9: "Юго-Юго-Западный",
                  10: "Юго-Западный",
                  11: "Запад-Юго-Западный",
                  12: "Западный",
                  13: "Западно-Северо-Западный",
                  14: "Северо-Западный",
                  15: "Северо-Северо-Западный"}
    return directions[rhumb]


def degree(deg_val, mode=True):
    """
    Return direction of wind
    :param deg_val: degree value
    :param mode:    True - return absolute direction
                    False - return absolute direction in rhumb
    :return:
    """
    if mode:
        rhumb = degree_to_rhumb(deg_val)
        direction = rhumb_to_direction(rhumb)
    else:
        direction = degree_to_rhumb(deg_val)
    return direction
