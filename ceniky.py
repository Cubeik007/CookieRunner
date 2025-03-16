import tkinter as tk

class Cenik():
    def __init__(self, parent):
        self.babicka = 100
        self.farma = 1000
        self.dalnice = 10000
        self.org = 5000
        self.xorg = 6000
        
        self.frame = tk.Frame(parent, bd=2, relief=tk.SUNKEN)
        self.frame.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        
        self.babicka_counter = Counter(self.frame, "Babička", self.babicka, 0, 0)
        self.farma_counter = Counter(self.frame, "Farma", self.farma, 1, 0)
        self.dalnice_counter = Counter(self.frame, "Dalnice", self.dalnice, 2, 0)
        self.org_counter = Counter(self.frame, "Org", self.org, 0, 2)
        self.xorg_counter = Counter(self.frame, "Xorg", self.xorg, 1, 2)
        
class Counter():
    def __init__(self, parent, nazev, cena, row, col):
        self.label = tk.Label(parent, text=nazev)
        self.label.grid(row=row, column=col, padx=5, pady=5)
        
        self.cena = tk.Entry(parent, width=10)
        self.cena.grid(row=row, column=col+1, padx=5, pady=5)
        self.cena.insert(0, str(cena))  # Výchozí hodnota
