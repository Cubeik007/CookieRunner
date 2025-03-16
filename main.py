import tkinter as tk
from math import log2, floor
from behani import *
from kupovani import *
from ceniky import *
import time
from clock import *

# Zakladni nastaveni parametru
SUSENKY = 0
KLASIK = 1
POZADU = 10
POSLEPU = 2
VALENI = 1

AUTOCLICK_INTERVAL = 5
GAME_LENGTH = 3600


class CounterGroup:
    def __init__(self, parent, row_start, column_start, cenik):        
        self.frame = tk.Frame(parent, bd=2, relief=tk.SUNKEN)
        self.frame.grid(row=row_start, column=column_start, padx=10, pady=10, sticky="w")
        
        self.celkem = CounterRow(self.frame, 0, "Počet cookies", self)
        self.klasik = Klasik(self.frame, 1, "Klasik", self, KLASIK)
        self.pozadu = Pozadu(self.frame, 2, "Pozadu", self, POZADU)
        self.poslepu = Poslepu(self.frame, 3, "Poslepu", self, POSLEPU)
        self.valeni = Valeni(self.frame, 4, "Bez noh", self, VALENI)
        self.radky = [self.celkem, self.klasik, self.pozadu, self.poslepu, self.valeni]
        
        self.babicka = Babicka(self.frame, 0, "Babicka", self, cenik)
        self.b = 0
        
        self.farma = Farma(self.frame, 1, "Farma", self, cenik)
        self.f = 0
        
        self.dalnice = Dalnice(self.frame, 2, "Dalnice", self, cenik)
        self.d = 0
        
        self.org = Org(self.frame, 3, "Org", self, cenik)
        self.o = 0
        
        self.xorg = Xorg(self.frame, 4, "Xorg", self, cenik)
        self.x = 0
        
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
        self.total_Time = Timer(parent, "Celkový čas", 4, 2)
        self.autoclick_interval = AUTOCLICK_INTERVAL
        self.game_length = GAME_LENGTH
        
        self.change_time()
        
    def change_time(self):
        self.timer.change_label()
        self.total_Time.change_label()
        self.updatuj_hodnoty()
        if self.timer.get_time() > self.autoclick_interval:
            self.autoclick()
            self.timer.reset()
        self.parent.after(100, self.change_time)

           
    def autoclick(self):
        for team in self.teams:
            team.celkem.val = floor(team.celkem.val * (11/10)**team.f)
            team.celkem.val = team.celkem.val + (team.b*team.klasik.val) 
            team.celkem.updatuj_parametr(team.celkem.val)
        
    def updatuj_hodnoty(self):
        for team in self.teams:
            try:
                for radek in team.radky:
                    try:
                        radek.param = int(radek.parametr.get())
                    except AttributeError:
                        pass
                    radek.val = int(radek.mnozstvi.get())
                # team.celkem.val = int(team.celkem.obehy.get())
                # team.klasik.val = int(team.klasik.parametr.get())
                # team.pozadu.val = int(team.valeni.parametr.get())
                # team.z = int(team.pozadu.parametr.get())
                # team.s = int(team.poslepu.parametr.get())
                # team.b = int(team.babicka.mnozstvi.get())
                # team.f = int(team.farma.mnozstvi.get())
                # team.d = int(team.dalnice.mnozstvi.get())
                # team.o = int(team.org.mnozstvi.get())
                # team.x = int(team.xorg.mnozstvi.get())
            except ValueError:
                pass
        try:
            self.cenik.dalnice = int(self.cenik.dalnice_counter.cena.get())
            self.cenik.farma = int(self.cenik.farma_counter.cena.get())
            self.cenik.babicka = int(self.cenik.babicka_counter.cena.get())
            self.cenik.org = int(self.cenik.org_counter.cena.get())
            self.cenik.xorg = int(self.cenik.xorg_counter.cena.get())
        except ValueError:
            pass

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