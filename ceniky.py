import tkinter as tk
from behani import CounterRow

BABICKA = 100
FARMA = 1000
DALNICE = 10000
ORG = 200
XORG = 500
JAIL = 2500

class Cenik():
    def __init__(self, parent):
        self.frame = tk.Frame(parent, bd=2, relief=tk.SUNKEN)
        self.frame.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        
        self.babicka_counter = Counter(self.frame, 0, "Babička", BABICKA)
        self.farma_counter = Counter(self.frame, 1, "Farma", FARMA)
        self.dalnice_counter = Counter(self.frame, 0, "Dalnice", DALNICE, 6)
        self.org_counter = Counter(self.frame, 0, "Org", ORG, 3)
        self.xorg_counter = Counter(self.frame, 1, "Xorg", XORG, 3)
        self.jail_counter = Counter(self.frame, 1, "Jail free", JAIL, 6)
        
        self.radky = [self.babicka_counter, self.farma_counter, self.dalnice_counter, self.org_counter, self.xorg_counter, self.jail_counter]
        
class Counter(CounterRow):
    def __init__(self, parent, row, label_text, val, col = 0):
        super().__init__(parent, row, label_text, col)
        self.val = val
        self.updatuj_mnozstvi(val)

