import tkinter as tk
from tkinter import messagebox, simpledialog, PhotoImage
import tkinter.font as tkfont
from tkinter.ttk import Progressbar

from SaveManager import SaveManager
import os
from Games import PlayGame
from Games import FeedGame

from ZwierzakiPodKlasy import Waz, Lis, Ptak, Rockyroo

class MyGui:
    def __init__(self):
        """
        Inicjalizuje główne okno aplikacji, ładuje grafiki, ustawia domyślną czcionkę i wywołuje ekran główny (mainMenu).
        """
        self.zw = None

        self.bg_label1 = None
        self.bg_label2 = None
        self.option_label = None
        self.load_label = None

        self.ig_pth1 = None
        self.ig_pth2 = None
        self.ig_pth3 = None
        self.ig_pth4 = None


        self.fontStyle = "Comic Sans MS"

        self.root = tk.Tk()
        self.root.geometry("1000x660")
        self.root.title("PuffyPals")

#        self.root.configure(bg="black")

        self.root.resizable(False, False)

        self.mainMenu()

        self.root.protocol("WM_DELETE_WINDOW", self.exit)

        self.root.mainloop()

    # Czyszczenie (TO NIE JEST Z CHATA PAMIETAJ KOMENTARZ != CHAT ROBIE TO DLA SIEBIE OK?!?!?)
    def clear(self):
        """
        Usuwa wszystkie widgety z głównego okna.

        Używane do przełączania ekranów (np. z menu głównego do widoku zwierzaka).
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        self.bg_label1 = None
        self.bg_label2 = None
        self.option_label = None
        self.load_label = None


    def mainMenu(self):
        """
            Tworzy ekran startowy gry z przyciskami wyboru zwierzaka.
            Czyści poprzednie widgety i ustawia tło oraz tytuł.
        """
        self.clear()

        self.ig_pth1 = PhotoImage(file="img/main_bg.png")
        self.bg_label1 = tk.Label(self.root, image=self.ig_pth1)
        self.bg_label1.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label1.lower()

        self.ig_pth3 = PhotoImage(file="img/icons/options.png")
        self.option_label = tk.Label(self.root, image=self.ig_pth3)

        self.ig_pth4 = PhotoImage(file="img/icons/load.png")
        self.load_label = tk.Label(self.root, image=self.ig_pth4)

        optionButton = tk.Button(
            self.root,
            image=self.ig_pth3,
            bd=2,
            activebackground="grey46",
            command=self.showOptions # <--------------------------------------------------- Miejsce na opcje
        )
        optionButton.place(relx=0, rely=0, anchor="nw", width=50, height=50)

        loadButton = tk.Button(
            self.root,
            image=self.ig_pth4,
            bd=2,
            activebackground="grey46",
            font=(self.fontStyle, 8),
            command=self.showLoad
        )
        loadButton.place(x=0, y=50, width=50, height=50)


        tk.Button(
            self.root,
            text="Exit",
            font=(self.fontStyle, 10),
            fg='red',
            command=self.exit
        ).pack(side='bottom', pady=10)

        frame = tk.Frame(self.root)
        frame.pack(side='bottom', fill = 'x', padx = 40, pady = 10)

        animals = [(Waz, "  Emberoon  "), (Rockyroo, " Rockyroo "), (Lis, "    Snowy    "), (Ptak, "Eisenklopfer")]
        for idx, (cls, text) in enumerate(animals):
            btn = tk.Button(
                frame,
                text=text,
                bd = 1,
                bg = "chocolate3",
                fg="black",
                activebackground="chocolate4",
                highlightthickness= 2,
                activeforeground="chartreuse2",
                font=(self.fontStyle, 12),
                command=lambda c=cls: self.askName(c)
            )

            btn.bind("<Enter>", lambda event, x=btn: self.on_enter_main(x))
            btn.bind("<Leave>", lambda event, x=btn: self.on_leave_main(x))

            btn.grid(row=0, column=idx, sticky="ew", padx=0)
            frame.columnconfigure(idx, weight=1)


    def askName(self, animal_cls) -> None:
        """
        Pyta użytkownika o imię dla nowego zwierzaka i tworzy jego instancję.

        :param animal_cls: Klasa zwierzaka
        """
        self.zw = animal_cls()

        name: str = ""
        while name == "":
            name = simpledialog.askstring(
                title="Name it",
                prompt="Enter name (max 10 characters): ",
            )
            if not name:
                return
            if len(name) > 10:
                messagebox.showerror("ALERT!!!","Name cant have more than 10 characters!!!")
                return

        self.zw.imie = name

        self.nShow()


    def nShow(self) -> None:
        """
        Główny interfejs interakcji ze zwierzakiem.
        Pokazuje tło, nazwę zwierzaka, statystyki oraz przyciski do akcji (zabawa, karmienie itd.).
        """
        self.clear()

        self.ig_pth2  = PhotoImage(file=self.zw.imgPath)
        self.bg_label2 = tk.Label(self.root, image=self.ig_pth2)
        self.bg_label2.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label2.lower()

        buttonColor: str = ""
        clickedColor: str = ""
        self.hoverColor: str = ""
        clickedText: str = ""

        match self.zw.id_color:
            case 1: #Ogien
                buttonColor: str = "firebrick3"
                clickedColor: str = "firebrick4"
                self.hoverColor: str = "medium blue"
                clickedText: str = "black"
            case 2: #Lód
                buttonColor: str = "RoyalBlue1"
                clickedColor: str = "RoyalBlue3"
                self.hoverColor: str = "red"
                clickedText: str = "black"
            case 3: #Ptak
                buttonColor: str = "DarkOliveGreen2"
                clickedColor: str = "DarkOliveGreen3"
                self.hoverColor: str = "red"
                clickedText: str = "black"
            case 4: #Ziemia
                buttonColor: str = "DarkGoldenrod2"
                clickedColor: str = "DarkGoldenrod3"
                self.hoverColor: str = "red"
                clickedText: str = "black"

        tk.Label(
            self.root,
            text=self.zw.imie,
            font=(self.fontStyle, 24)
            #miejsce na kolor w ramce
        ).pack(pady = (10,0))

        tk.Label(
            self.root,
            text=self.zw.nazwa,
            font=(self.fontStyle, 10)
            #miejsce na kolor w ramce
        ).pack()


#        tk.Button(
#            self.root,
#            text="Exit",
#            font=(self.fontStyle, 10),
#            fg='red',
#            command=self.exit
#        ).pack(side='bottom', pady=5)

        bottomFrame = tk.Frame(self.root)
        bottomFrame.pack(side='bottom', pady = 5)

        tk.Button(
            bottomFrame,
            text=" save ",
            font=(self.fontStyle, 10),
            fg='blue',
            command=self.save_game
        ).pack(side='right')

        tk.Button(
            bottomFrame,
            text="  exit ",
            font=(self.fontStyle, 10),
            fg='red',
            command=self.exit
        ).pack(side='left')

        #Jak chcemy wiecej opcji tutaj możemy pododawać
        frame = tk.Frame(self.root)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        feedButton = tk.Button(
            frame,
            text="Feed",
            bd = 1,
            bg = buttonColor,
            activebackground = clickedColor,
            activeforeground = clickedText,
            highlightthickness=2,
            font=(self.fontStyle, 12),
            command=self.jedzObjekt
        )

        feedButton.bind("<Enter>", lambda event, x=feedButton: self.on_enter_zw(x))
        feedButton.bind("<Leave>", lambda event, x=feedButton: self.on_leave_zw(x))

        feedButton.grid(row=1, column=0, sticky="ew")

        playButton = tk.Button(
            frame,
            text="Play",
            bd=1,
            bg=buttonColor,
            activebackground=clickedColor,
            activeforeground=clickedText,
            highlightthickness=2,
            font=(self.fontStyle, 12),
            command=self.bawObjekt
        )

        playButton.bind("<Enter>", lambda event, x=playButton: self.on_enter_zw(x))
        playButton.bind("<Leave>", lambda event, x=playButton: self.on_leave_zw(x))

        playButton.grid(row=1, column=1, sticky="ew")

        self.feedBar = Progressbar(
            frame,
            orient=tk.HORIZONTAL,
            length=450,
            maximum=30,  # Tutaj jeszcze może zajść zmiana
            value=self.zw.jedzenie
        )

        self.feedBar.grid(row=0, column=0, padx=5, pady=5)

        self.playBar = Progressbar(
            frame,
            orient=tk.HORIZONTAL,
            length=450,
            maximum=30,  # Tutaj jeszcze może zajść zmiana
            value=self.zw.zabawa
        )

        self.playBar.grid(row=0, column=1, padx=5, pady=5)

        frame.pack(side='bottom' , fill='x')

    def jedzObjekt(self):
        """
        Uruchamia gierke karmienia (FeedGame).
        Po zakończeniu gry aktualizuje statystyki.
        """
        if self.zw.jedzenie >= 30:
            messagebox.showerror("ALERT!!!","You can't feed your pet anymore. It's overfed.")
            return

        # self.zw.jedz()
        # self.feedText.config(text=f"food = {self.zw.jedzenie}")
        # self.playText.config(text=f"play  = {self.zw.zabawa}")
        FeedGame(self.root, self.zw, self.update_stats, self.fontStyle)

    def bawObjekt(self):
        """
        Uruchamia gierke zabawy (PlayGame).
        Po zakończeniu gry aktualizuje statystyki.
        """
        if self.zw.jedzenie == 0:
            messagebox.showerror("ALERT!!!","The pet is hungry")
            return

        # self.zw.baw_sie()
        # self.feedText.config(text=f"food = {self.zw.jedzenie}")
        # self.playText.config(text=f"play  = {self.zw.zabawa}")
        PlayGame(self.root, self.zw, self.update_stats, self.fontStyle)

    def update_stats(self):
        """
        Odświeża paski postępu jedzenia oraz zabawy.
        Wartości pobierane są z obiektu zwierzaka.
        """
        self.feedBar.config(value=self.zw.jedzenie)
        self.playBar.config(value=self.zw.zabawa)

    def showOptions(self):
        """
        Wyświetla okno opcji, umożliwiające zmianę czcionki interfejsu.
        """
        dlg = tk.Toplevel(self.root)
        dlg.title("Options")
        dlg.grab_set()

        families = sorted(set(tkfont.families()), key=str.lower)
        var_font = tk.StringVar(value=self.fontStyle)
        tk.Label(dlg, text="Font:", font=(self.fontStyle, 12)).pack(padx=20, pady=(20, 5))
        tk.OptionMenu(dlg, var_font, *families).pack(padx=20)


        btn_frame = tk.Frame(dlg)
        btn_frame.pack(pady=15)

        tk.Button(
            btn_frame,
            text="OK",
            font=(self.fontStyle, 8),
            width=8,
            command=lambda: self._apply(dlg, var_font.get())
        ).pack(side='left', padx=5)

        tk.Button(
            btn_frame,
            text="Cancel",
            font=(self.fontStyle, 8),
            fg="red",
            width=8,
            command=lambda: dlg.destroy()
        ).pack(side='left', padx=5)


    def _apply(self, dlg: tk.Toplevel, new_font):
        """
        Zmienia aktualną czcionkę interfejsu na wybraną przez użytkownika.

        :param new_font: Nazwa wybranej czcionki.
        """
        self.fontStyle = new_font
        self.mainMenu()
        dlg.destroy()

    def showLoad(self):
        """
        Wyświetla okno ładowania, z którego gracz może wczytać zapisany stan gry.
        """
        dig = tk.Toplevel(self.root)
        dig.title("Load Game")
        dig.grab_set()

        try:
            files = sorted(f for f in os.listdir(SaveManager.SAVE_DIR)
                           if f.endswith(".txt"))
        except FileNotFoundError:
            files = []

        if not files:
            tk.Label(dig, text="No saved game saved!", font=(self.fontStyle, 12)).pack(pady=20)
            tk.Button(dig, text="OK", width=10, command=dig.destroy).pack(pady=10)
            return

        var_file = tk.StringVar(value=files[0])

        tk.Label(dig, text="Chose file:", font=(self.fontStyle, 12)).pack(padx=20, pady=(20,5))
        tk.OptionMenu(dig, var_file, *files).pack(padx=20)

        btn_frame = tk.Frame(dig)
        btn_frame.pack(pady=15)

        tk.Button(
            btn_frame,
            text="Load",
            font=(self.fontStyle, 8),
            width=8,
            command=lambda: self._apply_load(dig, var_file.get())
        ).pack(side='left', padx=5)

        tk.Button(
            btn_frame,
            text="Cancel",
            font=(self.fontStyle, 8),
            fg="red",
            width=8,
            command=lambda: dig.destroy()
        ).pack(side='left', padx=5)

    def _apply_load(self, dlg: tk.Toplevel, filename: str):
        """
        Wczytuje stan gry z wybranego pliku.

        :param filename: Nazwa pliku zapisu
        """
        path = os.path.join(SaveManager.SAVE_DIR, filename)
        try:
            imie, class_name, nazwa, jedz, zab = SaveManager.load(path)
        except Exception as e:
            messagebox.showerror("Load error!!!", str(e))
            dlg.destroy()
            return

        class_map = {cls.__name__: cls for cls in (Waz, Lis, Ptak, Rockyroo)}
        if class_name not in class_map:
            messagebox.showerror("ERROR!", f"Unknown class: {class_name}")
            dlg.destroy()
            return

        zw = class_map[class_name]()
        zw.imie = imie
        zw.jedzenie = jedz
        zw.zabawa = zab
        self.zw = zw

        dlg.destroy()
        self.nShow()

    def save_game(self):
        """
        Zapisuje stan gry do pliku.
        """
        try:
            path = SaveManager.save(self.zw)
            messagebox.showinfo("Saved!", f"Game saved to:\n{path}")
        except Exception as e:
            messagebox.showerror("Error!", f"Failed to save game:\n{e}")

    def on_enter_main(self, x):
        x.configure(fg = "LightGreen")

    def on_leave_main(self, x):
        x.configure(fg = "black")

    def on_enter_zw(self, x):
        x.configure(fg = self.hoverColor)

    def on_leave_zw(self, x):
        x.configure(fg = "black")

    def exit(self):
        """
        Wyświetla okno potwierdzające zamknięcie aplikacji.
        Po potwierdzeniu użytkownika kończy działanie programu.
        """
        if messagebox.askyesno("Exit?", "Do you want to exit?"):
            self.root.destroy()
