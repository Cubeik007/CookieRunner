import tkinter as tk
from math import log2
from behani import *

class Obchod:
    def __init__(self, parent, row, label_text, group):
        self.label = tk.Label(parent, text=f"{label_text}:")
        self.label.grid(row=row, column=4, padx=5, pady=5)
        
        self.mnozstvi = tk.Entry(parent, width=10)
        self.mnozstvi.grid(row=row, column=5, padx=5, pady=5)
        self.mnozstvi.insert(0, str(0))  # Výchozí hodnota
        
        self.button = tk.Button(parent, text=f"Koupit!", command=self.koupit())
        self.button.grid(row=row, column=6, padx=5, pady=5)
        self.group = group
        
        self.cenik = tk.Entry(parent, width=10)
        self.cenik.grid(row=row, column=7, padx=5, pady=5)
        self.cenik.insert(0, str(0))  # Výchozí hodnota
        
    def koupit(self):
        pass
    


class CounterGroup:
    def __init__(self, parent, row_start, column_start, game):
        """Vytvoří skupinu počítadel s vlastními labely a přírůstky."""
        self.susenky = 0
        self.k = 1
        self.z = 10
        self.s = 2
        self.v = 1
        self.frame = tk.Frame(parent, bd=2, relief=tk.SUNKEN)
        self.frame.grid(row=row_start, column=column_start, padx=10, pady=10, sticky="w")
        
        self.celkem = CounterRow(self.frame, 0, "Celkem", self)
        self.klasik = Klasik(self.frame, 1, "Klasik", self)
        self.pozadu = Pozadu(self.frame, 2, "Pozadu", self)
        self.poslepu = Poslepu(self.frame, 3, "Poslepu", self)
        self.valeni = Valeni(self.frame, 4, "Valeni", self)
        
        self.babicka = Obchod(self.frame, 0, "Babicka", self)
        
        self.label = tk.Label(self.frame, text=f"Tým číslo {row_start+3*column_start+1}")
        self.label.grid(row=0, column=2, padx=5, pady=5)

class Game():
    def __init__(self, parent, pocet):
        self.parent = parent
        self.teams = []
        col = 0
        for i in range(pocet):
            if i == 3:
                col += 1
            self.teams.append(CounterGroup(parent, i % 3, col, self))
    


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Více skupin počítadel s názvy")
    game = Game(root, 5)
    root.mainloop()