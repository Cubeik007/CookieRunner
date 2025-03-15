import tkinter as tk
from math import log2, floor
from behani import *
from kupovani import *

class Cenik():
    def __init__(self):
        self.babicka = 100
        self.farma = 1000

class CounterGroup:
    def __init__(self, parent, row_start, column_start, cenik):
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
        
        self.babicka = Babicka(self.frame, 0, "Babicka", self, cenik)
        self.b = 0
        
        self.babicka = Farma(self.frame, 1, "Farma", self, cenik)
        self.b = 0
        self.f = 0
        
        self.label = tk.Label(self.frame, text=f"Tým číslo {row_start+3*column_start+1}")
        self.label.grid(row=0, column=2, padx=5, pady=5)

class Game():
    def __init__(self, parent, pocet):
        self.parent = parent
        self.teams = []
        self.cenik = Cenik()
        col = 0
        for i in range(pocet):
            if i == 3:
                col += 1
            self.teams.append(CounterGroup(parent, i % 3, col, self.cenik))
        self.autoclick()
        self.updatuj_hodnoty()
           
    def autoclick(self):
        for team in self.teams:
            team.susenky 
            team.celkem.obehy.delete(0, tk.END)  # Smaže současný text
            team.susenky = floor(team.susenky * (11/10)**team.f)
            team.susenky = team.susenky + (team.b*team.k) 
            team.celkem.obehy.insert(0, str(team.susenky))  # Přidá novou hodnotu
        root.after(5000, self.autoclick)
        
    def updatuj_hodnoty(self):
        for team in self.teams:
            try:
                team.celkem.susenky = int(team.celkem.obehy.get())
                team.k = int(team.klasik.parametr.get())
                team.v = int(team.valeni.parametr.get())
                team.z = int(team.pozadu.parametr.get())
                team.s = int(team.poslepu.parametr.get())
                team.b = int(team.babicka.mnozstvi.get())
            except:
                pass
        root.after(500, self.updatuj_hodnoty)
        
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Více skupin počítadel s názvy")
    game = Game(root, 5)
    root.mainloop()