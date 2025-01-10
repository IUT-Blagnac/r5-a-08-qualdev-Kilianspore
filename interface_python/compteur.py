import tkinter as tk

class StartPage(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Compteur")
        self.counter = 0
        self.max_value = 10  # Valeur maximale par défaut
        self.min_value = -10 # Valeur minimale par défaut

        # Étiquette pour afficher la valeur du compteur
        self.label = tk.Label(self, text=f"Compteur : {self.counter}")
        self.label.pack()

        # Boutons
        btn_augmenter = tk.Button(self, text="Augmenter", command=self.increment)
        btn_augmenter.pack()

        btn_reduire = tk.Button(self, text="Réduire", command=self.decrement)
        btn_reduire.pack()

        btn_reset = tk.Button(self, text="Réinitialiser", command=self.reset)
        btn_reset.pack()

        # Champs pour définir les seuils
        tk.Label(self, text="Valeur maximale :").pack()
        self.max_entry = tk.Entry(self)
        self.max_entry.insert(0, str(self.max_value))
        self.max_entry.pack()

        tk.Label(self, text="Valeur minimale :").pack()
        self.min_entry = tk.Entry(self)
        self.min_entry.insert(0, str(self.min_value))
        self.min_entry.pack()

        btn_set_limits = tk.Button(self, text="Définir les limites", command=self.set_limits)
        btn_set_limits.pack()

    def increment(self):
        if self.counter < self.max_value:
            self.counter += 1
            self.update_label()

    def decrement(self):
        if self.counter > self.min_value:
            self.counter -= 1
            self.update_label()

    def reset(self):
        self.counter = 0
        self.update_label()

    def set_limits(self):
        try:
            self.max_value = int(self.max_entry.get())
            self.min_value = int(self.min_entry.get())
            self.update_label()
        except ValueError:
            self.label.config(text="Erreur : limites invalides")

    def update_label(self):
        self.label.config(text=f"Compteur : {self.counter}")
