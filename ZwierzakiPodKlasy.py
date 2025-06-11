from dataclasses import dataclass
from Zwierzak import Zwierzak

@dataclass
class Waz(Zwierzak):
    """
        Klasa definiująca węża. (Emberoon)
    """
    imie: str = ""
    nazwa: str = "Emberoon"
    imgPath: str = "img/Emberoon_bg.png"
    id_color: int = 1
    JEDZENIE_FOOD_DELTA: int = 1
    JEDZENIE_FUN_DELTA:  int = -1
    ZABAWA_FOOD_DELTA:   int = -1
    ZABAWA_FUN_DELTA:    int = 1


@dataclass
class Lis(Zwierzak):
    """
        Klasa definiująca lisa. (Snowy)
    """
    imie: str = ""
    nazwa: str = "Snowy"
    imgPath: str = "img/Snowy_bg.png"
    id_color: int = 2
    JEDZENIE_FOOD_DELTA: int = 1
    JEDZENIE_FUN_DELTA:  int = -1
    ZABAWA_FOOD_DELTA:   int = -1
    ZABAWA_FUN_DELTA:    int = 1

@dataclass
class Ptak(Zwierzak):
    """
        Klasa definiująca ptaka. (Eisenklopfer)
    """
    imie: str = ""
    nazwa: str = "Eisenklopfer"
    imgPath: str = "img/Eisenklopfer_bg.png"
    id_color: int = 3
    JEDZENIE_FOOD_DELTA: int = 1
    JEDZENIE_FUN_DELTA:  int = -1
    ZABAWA_FOOD_DELTA:   int = -1
    ZABAWA_FUN_DELTA:    int = 1

@dataclass
class Rockyroo(Zwierzak):
    """
        Klasa definiująca pancernika. (Rockyroo)
    """
    imie: str = ""
    nazwa: str = "Rockyroo"
    imgPath: str = "img/Rockyroo_bg.png"
    id_color: int = 4
    JEDZENIE_FOOD_DELTA: int = 1
    JEDZENIE_FUN_DELTA:  int = -1
    ZABAWA_FOOD_DELTA:   int = -1
    ZABAWA_FUN_DELTA:    int = 1