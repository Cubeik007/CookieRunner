import tkinter as tk

class Cenik():
    def __init__(self, parent):
        self.babicka = 100
        self.farma = 1000
        
        self.frame = tk.Frame(parent, bd=2, relief=tk.SUNKEN)
        self.frame.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        
        self.babicka_counter = Counter(self.frame, "Babička", self.babicka, 0)
        self.farma_counter = Counter(self.frame, "Farma", self.farma, 1)
        
class Counter():
    def __init__(self, parent, nazev, cena, row):
        self.label = tk.Label(parent, text=nazev)
        self.label.grid(row=row, column=0, padx=5, pady=5)
        
        self.cena = tk.Entry(parent, width=10)
        self.cena.grid(row=row, column=1, padx=5, pady=5)
        self.cena.insert(0, str(cena))  # Výchozí hodnota
