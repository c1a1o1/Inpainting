# -*- coding: utf-8 -*-
""" Ce module contient toutes les méthodes et fonctions n'ayant pas pu être rangées dans un module précis. Il est
souvent réutilisé dans plusieurs modules différents, et doit donc être en bout de chaîne pour éviter les dépendances
cycliques.
"""

import numpy as np
from typing import Union

Number = Union[int, float]


def normalize(array: np.ndarray, floor: Number = 0, ceil: Number = 1, origin_floor: Number = None,
              origin_ceil: Number = None):
    """ Normalise un tableau dans un seuil minimal et maximal.
    :param: array, le tableau à normaliser.
    :param: floor, le seuil bas de la normalisation.
    :param: ceil, le seuil haut de la normalisation.
    :param: origin_floor, la valeur minimale dans le tableau de départ.
    :param: origin_ceil, le valeur maximale dans le tableau de départ.
    :return: Le tableau normalisé.
    """
    array_min = origin_floor if origin_floor is not None else array.min()
    array_max = origin_ceil if origin_ceil is not None else array.max()
    upper = (ceil - floor) / (array_max - array_min)
    lower = (ceil - upper * array_max)  # or (floor - upper * array_min)
    return upper * array + lower


def norme_1(w: np.ndarray) -> Number:
    """ Calcule la norme 1 d'un vecteur.
    :param w: Le vecteur dont on veut calculer la norme.
    :return: La valeur de la norme 1 de `w`.
    """
    return sum([np.abs(w_i) for w_i in w])


def norme_2(w: np.ndarray) -> Number:
    """ Calcule la norme 2 d'un vecteur.
    :param w: Le vecteur dont on veut calculer la norme.
    :return: La valeur de la norme 2 de `w`.
    """
    return np.sqrt(sum([np.power(w_i, 2) for w_i in w]))


if __name__ == "__main__":
    pass