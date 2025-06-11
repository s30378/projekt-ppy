import os

class SaveManager:
    SAVE_DIR =  "savedFiles"

    @classmethod
    def save(cls, zw):
        """
        Funckja zapisująca do pliku stan gry.

        :param zw: obiekt zwięrzęcia
        """
        os.makedirs(cls.SAVE_DIR, exist_ok=True)

        filename = f"{zw.imie}.txt"
        path = os.path.join(cls.SAVE_DIR, filename)

        with open(path, "w", encoding="utf-8") as f:
            f.write(f"{zw.imie} "
                    f"{zw.__class__.__name__} "
                    f"{zw.nazwa} "
                    f"{zw.jedzenie} "
                    f"{zw.zabawa}")
        return path

    @classmethod
    def load(cls, filepath): #Możesz jak chcesz zwiększyć jedzenie i zabawe w plikach do wartości które normalnie były by nie możliwe
        """
        Funkcja wczytująca stan gry z pliku.

        :param filepath: ścieżka do pliku z zapisem gry
        :return: dane zwierzaka z zapisu gry
        """
        with open(filepath, "r", encoding="utf-8") as f:
            parts = f.readline().strip().split()
        imie, class_name, nazwa, jedzenie, zabawa = parts
        return imie, class_name, nazwa, int(jedzenie), int(zabawa)