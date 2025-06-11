from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass      #Poprostu dla wygody (troche se pooglądałem filmików na yt)
class Zwierzak(ABC):
    """
        Klasa bazowa zwierząt, która tworzy podstawowe atrybuty oraz funkcje takie jak:
            - Imię zwierzaka
            - Nazwa gatunku zwierzaka
            - imgPath, czyli ścieżka do pliku graficznego zwierzaka
            - ID koloru potrzebny do późniejszych operacji
            - Jedzenie - startowa wartość nasycenia dla wszystkich gatunków
            - Zabawa - startowa wartość zabawy dla wszystkich gatunków
            - Wartości DELTA ustalające domyślne wartości zmian jedzenia i zabawy
    """
    imie: str
    nazwa: str
    imgPath: str
    id_color: int
    jedzenie = 10   #tutaj możemy pozmieniać by dla każdego zwierzaka innczej było
    zabawa = 10     #bardzo łatwe do zainicjanowania

    JEDZENIE_FOOD_DELTA: int = 0    # o ile wzrasta jedzenie przy jedzeniu
    JEDZENIE_FUN_DELTA: int = 0     # o ile spada zabawa przy jedzeniu
    ZABAWA_FOOD_DELTA: int = 0      # o ile spada jedzenie przy zabawie
    ZABAWA_FUN_DELTA: int = 0       # o ile wzrasta zabawa przy zabawie

    def jedz(self):
        """
            Domyślna funkcja karmiąca zwierze, jednocześnie zmniejsza stan ubawienia.
        """
        self.jedzenie += self.JEDZENIE_FOOD_DELTA
        self.zabawa  += self.JEDZENIE_FUN_DELTA

    def baw_sie(self):
        """
            Domyślna funkcja zabawy ze zwierzakiem, jednocześnie zmniejsza nasycenie.
        """
        self.jedzenie += self.ZABAWA_FOOD_DELTA
        self.zabawa  += self.ZABAWA_FUN_DELTA