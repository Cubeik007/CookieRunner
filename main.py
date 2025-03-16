import tkinter as tk
from math import log2, floor
from behani import *
from kupovani import *
from ceniky import *
import time
from clock import *


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
        
        self.celkem = CounterRow(self.frame, 0, "Počet cookies", self)
        self.klasik = Klasik(self.frame, 1, "Klasik", self)
        self.pozadu = Pozadu(self.frame, 2, "Pozadu", self)
        self.poslepu = Poslepu(self.frame, 3, "Poslepu", self)
        self.valeni = Valeni(self.frame, 4, "Bez noh", self)
        
        self.babicka = Babicka(self.frame, 0, "Babicka", self, cenik)
        self.b = 0
        
        self.farma = Farma(self.frame, 1, "Farma", self, cenik)
        self.f = 0
        
        self.team_label = tk.Label(self.frame, text=f"Tým číslo {row_start+3*column_start+1}")
        self.team_label.grid(row=0, column=2, padx=5, pady=5)
        

class Game():
    def __init__(self, parent, pocet):
        self.parent = parent
        self.teams = []
        self.cenik = Cenik(parent)
        col = 0
        for i in range(pocet):
            if i == 3:
                col += 1
            self.teams.append(CounterGroup(parent, i % 3, col, self.cenik))
            
        root.bind("<p>", self.pause_resume)
        
        self.timer = Timer(parent, "Autoclick", 4, 1) 
        self.total_Time = Timer(parent, "Celkový čas", 5, 1)
        self.autoclick_interval = 60
        
        
        self.autoclick()
        self.updatuj_hodnoty()
        

           
    def autoclick(self):
        self.timer.change_label()
        self.total_Time.change_label()
        if self.timer.get_time() > self.autoclick_interval:
            for team in self.teams:
                team.susenky 
                team.celkem.obehy.delete(0, tk.END)  # Smaže současný text
                team.susenky = floor(team.susenky * (11/10)**team.f)
                team.susenky = team.susenky + (team.b*team.k) 
                team.celkem.obehy.insert(0, str(team.susenky))  # Přidá novou hodnotu
            self.timer.reset()
        self.parent.after(500, self.autoclick)
        
    def updatuj_hodnoty(self):
        for team in self.teams:
            try:
                team.susenky = int(team.celkem.obehy.get())
                team.k = int(team.klasik.parametr.get())
                team.v = int(team.valeni.parametr.get())
                team.z = int(team.pozadu.parametr.get())
                team.s = int(team.poslepu.parametr.get())
                team.b = int(team.babicka.mnozstvi.get())
                team.f = int(team.farma.mnozstvi.get())
            except ValueError:
                pass
        try:
            self.cenik.farma = int(self.cenik.farma_counter.cena.get())
            self.cenik.babicka = int(self.cenik.babicka_counter.cena.get())
        except ValueError:
            pass
        # except:
        #     print("help")
        self.parent.after(500, self.updatuj_hodnoty)
        
    def pause_resume(self, event = None):
        self.timer.change_label()
        self.total_Time.change_label()
        self.timer.pause_resume()
        self.total_Time.pause_resume()
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Více skupin počítadel s názvy")
    game = Game(root, 6)
    root.mainloop()