import tkinter as tk
import random


class PlayGame:
    def __init__(self, parent, zwierzak, onfinish, fontStyle):
        """
        Inicjalizuje okno gierki 'Kółko i krzyżyk'.

        :param parent: Obiekt GUI
        :param zwierzak: Obiekt zwierzaka
        :param onfinish: Funkcja wywoływana po zakończeniu gry
        :param fontStyle: Wybrana czcionka interfejsu
        """
        self.parent = parent
        self.zw = zwierzak
        self.on_finish = onfinish
        self.fontStyle = fontStyle

        self.window = tk.Toplevel(self.parent)
        self.window.title("Tic tac toe")
        self.window.geometry("400x450")
        self.window.resizable(False, False)
        self.window.grab_set()

        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        self.status_label = tk.Label(self.window, text="Your turn (X)", font=(self.fontStyle, 12))
        self.status_label.pack(pady=10)

        self.frame = tk.Frame(self.window)
        self.frame.pack(padx=10, pady=5)

        self.create_board()

    def create_board(self):
        """
        Tworzy siatkę 3x3 przycisków do gry w kółko i krzyżyk.
        """
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.frame, text="", width=5, height=2,
                                font=("Arial", 24), command=lambda x=i, y=j: self.click(x, y))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn

    def click(self, x, y):
        """
        Obsługuje kliknięcie gracza w wybrane pole.

        :param x: Wiersz przycisku.
        :param y: Kolumna przycisku.
        """
        btn = self.buttons[x][y]
        if btn["text"] == "" and self.current_player == "X":
            btn.config(text="X", state="disabled")

            if self.check_win("X"):
                self.end_game("X")
            elif self.check_draw():
                self.end_game("draw")
            else:
                self.current_player = "O"
                self.status_label.config(text="PC's turn (O)")
                self.window.after(500, self.ai_move)

    def ai_move(self):
        """
        Wykonuje ruch komputera w losowe dostępne pole.
        """
        empty = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j]["text"] == ""]
        if not empty:
            return

        i, j = random.choice(empty)
        self.buttons[i][j].config(text="O", state="disabled")

        if self.check_win("O"):
            self.end_game("O")
            return
        elif self.check_draw():
            self.end_game("draw")
            return

        self.current_player = "X"
        self.status_label.config(text="Your turn (X)")

    def check_win(self, symbol):
        """
        Sprawdza, czy podany gracz wygrał grę.

        :param symbol: Symbol gracza
        :return: Zwraca True gdy ktoś wygrał, False gdy gra toczy się dalej.
        """
        for i in range(3):
            if all(self.buttons[i][j]["text"] == symbol for j in range(3)):
                return True
            if all(self.buttons[j][i]["text"] == symbol for j in range(3)):
                return True
        if all(self.buttons[i][i]["text"] == symbol for i in range(3)):
            return True
        if all(self.buttons[i][2 - i]["text"] == symbol for i in range(3)):
            return True
        return False

    def check_draw(self):
        """
        Sprawdza, czy gra kończy się remisem.,

        :return: True gdy koniec przez remis, False gdy nie.
        """
        return all(self.buttons[i][j]["text"] != "" for i in range(3) for j in range(3))

    def end_game(self, result):
        """
        Kończy grę i wyświetla odpowiedni komunikat, modyfikuje statystyki zwierzaka.

        :param result: Symbol wygranego gracza lub "draw"
        """
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(state="disabled")

        if result == "X":
            self.status_label.config(text="You won! +2 fun")
            if self.zw.zabawa < 30:
                self.zw.zabawa += 2
            else:
                self.zw.zabawa = 30
        elif result == "draw":
            self.status_label.config(text="Draw! +1 fun")
            if self.zw.zabawa < 30: self.zw.zabawa += 1
        else:
            self.status_label.config(text="You lost")

        if self.zw.jedzenie >= 2:
            self.zw.jedzenie -= 2
        else:
            self.zw.jedzenie = 0

        if self.on_finish:
            self.on_finish()

        tk.Button(self.window, text="Exit", command=self.window.destroy, font=(self.fontStyle, 12)).pack(pady=10)


class FeedGame:
    def __init__(self, parent, zwierzak, onfinish, fontStyle):
        """
        Inicjalizuje okno gierki karmienia zwierzaka.

        :param parent: Obiekt GUI
        :param zwierzak: Obiekt zwierzaka
        :param onfinish: Funkcja wywoływana po zakończeniu gry
        :param fontStyle: Wybrana czcionka interfejsu
        """
        self.parent = parent
        self.zw = zwierzak
        self.on_finish = onfinish
        self.fontStyle = fontStyle
        self.clicks = 0
        self.running = True

        self.window = tk.Toplevel(self.parent)
        self.window.title("Feeding game")
        self.window.geometry("400x450")
        self.window.resizable(False, False)
        self.window.grab_set()

        self.status_label = tk.Label(self.window, text="Click on food!", font=(self.fontStyle, 12))
        self.status_label.pack(pady=10)

        self.food_img = tk.PhotoImage(file="img/jagoda.png")
        match self.zw.id_color:
            case 1:
                self.food_img = tk.PhotoImage(file="img/steak.png")
            case 2:
                self.food_img = tk.PhotoImage(file="img/jagoda.png")
            case 3:
                self.food_img = tk.PhotoImage(file="img/robak.png")
            case 4:
                self.food_img = tk.PhotoImage(file="img/mrówka.png")

        self.canvas = tk.Canvas(self.window, width=400, height=340, bg="white")
        self.canvas.pack()

        self.bg_img = tk.PhotoImage(file="img/backgrounds/table_bg.png")
        self.canvas.create_image(0, 0, image=self.bg_img, anchor="nw")

        self.holes = [
            (67, 52), (200, 52), (335, 52), (67, 167), (200, 167), (335, 167), (67, 284), (200, 284), (335, 284)
        ]

        self.food_id = None
        self.current_pos = (-1, -1)
        self.canvas.bind("<Button-1>", self.hit)

        self.spawn_food()
        self.window.after(10000, self.end_game)

    def spawn_food(self):
        """
        Losowo umieszcza jedzenie na planszy w jednej z 9 pól.
        Odświeżane co 800 ms.
        """
        if not self.running:
            return

        if self.food_id is not None:
            self.canvas.delete(self.food_id)

        i = random.randint(0, 8)
        self.current_pos = i

        x, y = self.holes[i]
        self.food_id = self.canvas.create_image(x, y, image=self.food_img)
        self.window.after(800, self.spawn_food)

    def hit(self, event):
        """
        Obsługuje kliknięcia gracza. Jeśli kliknięto w jedzenie – zalicza punkt.

        :param event: Obiekt zdarzenia kliknięcia myszy.
        """
        if not self.running or self.current_pos == -1:
            return

        x_click = event.x
        y_click = event.y
        x, y = self.holes[self.current_pos]

        if x - 40 <= x_click <= x + 40 and y - 40 <= y_click <= y + 40:
            self.clicks += 1
            self.status_label.config(text=f"Count: {self.clicks}")
            self.canvas.delete(self.food_id)
            self.food_id = None
            self.current_pos = -1

    def end_game(self):
        """
        Kończy grę, podsumowuje wynik i aktualizuje statystyki zwierzaka.
        """
        self.running = False
        if self.food_id:
            self.canvas.delete(self.food_id)

        if self.clicks >= 13:
            if self.zw.jedzenie < 30:
                self.zw.jedzenie += 4
            else:
                self.zw.jedzenie = 30
            msg = "PERFECT! +4 food"
        elif self.clicks >= 10:
            if self.zw.jedzenie < 30:
                self.zw.jedzenie += 2
            else:
                self.zw.jedzenie = 30
            msg = "Super! +2 food"
        elif self.clicks >= 6:
            if self.zw.jedzenie < 30: self.zw.jedzenie += 1
            msg = "So close +1 food"
        else:
            msg = "You lost..."

        if self.zw.zabawa >= 2:
            self.zw.zabawa -= 2
        else:
            self.zw.zabawa = 0

        self.status_label.config(text=msg)
        if self.on_finish:
            self.on_finish()

        tk.Button(self.window, text="Exit", command=self.window.destroy, font=(self.fontStyle, 12)).pack(pady=10)
