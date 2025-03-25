#!/usr/bin/env python

import tkinter as tk
from math import log2, floor
from behani import *
from kupovani import *
from ceniky import *
import time
from clock import *
from achievements import *

# Zakladni nastaveni parametru
SUSENKY = 0
KLASIK = 1
POZADU = 10
POSLEPU = 1
VALENI = 1

AUTOCLICK_INTERVAL = 10789
GAME_LENGTH = 3600
POCET_TEAMU = 6


class CounterGroup:
    def __init__(self, parent, row_start, column_start, cenik, game, id):
        self.id = id
        self.frame = tk.Frame(parent, bd=2, relief=tk.SUNKEN)
        self.frame.grid(row=row_start, column=column_start, padx=5, pady=5, sticky="w")
        
        self.celkem = CounterRow(self.frame, 0, "Cookies C")
        self.klasik = Klasik(self.frame, 1, "Klasik K", self, KLASIK)
        self.pozadu = Pozadu(self.frame, 2, "Pozadu Z", self, POZADU)
        self.poslepu = Poslepu(self.frame, 3, "Poslepu S", self, POSLEPU)
        self.valeni = Valeni(self.frame, 4, "Bez noh V", self, VALENI)
        self.obihani = [self.celkem, self.klasik, self.pozadu, self.poslepu, self.valeni]
        
        self.babicka = Babicka(self.frame, 0, "Babicka B", self, cenik)  
        self.farma = Farma(self.frame, 1, "Farma F", self, cenik)  
        self.dalnice = Dalnice(self.frame, 2, "Dalnice D", self, cenik)  
        self.org = Org(self.frame, 3, "Org O", self, cenik)
        self.xorg = Xorg(self.frame, 4, "Xorg X", self, cenik)
        self.jail = Jail(self.frame, 5, "Jail free card J", self, cenik)
        self.kupovani = [self.babicka, self.farma, self.dalnice, self.org, self.xorg, self.jail]
        
        self.golden = Golden_cookie(self.frame, self, game.teams)
        
        self.team_label = tk.Label(self.frame, text=f"Tým číslo {row_start+3*column_start+1}")
        self.team_label.grid(row=0, column=2, padx=5, pady=5)
        self.achievements = game.achievements
        
        # root.bind("<1>", self.update_stuff)


class Game():
    def __init__(self, parent, pocet):
        self.parent = parent
        self.teams = []
        self.cenik = Cenik(parent)
        self.achievements = Achievements(parent, self.teams)
        col = 0
        for i in range(pocet):
            if i == 3:
                col += 1
            self.teams.append(CounterGroup(parent, i % 3, col, self.cenik, self, i+1))
            
        # parent.bind("<p>", self.pause_resume)
        parent.bind("<KeyPress>", self.check_keyboard_input)

        
        self.timer = Timer(parent, "Autoclick", 4, 1) 
        self.total_Time = Timer(parent, "Celkový čas", 4, 2)
        self.autoclick_interval = AUTOCLICK_INTERVAL
        self.game_length = GAME_LENGTH
        
        self.change_time()
        self.last_team = 1
        
    def change_time(self):
        self.timer.change_label()
        self.total_Time.change_label()
        self.updatuj_hodnoty()
        if self.timer.get_time() > self.autoclick_interval:
            self.autoclick()
            self.timer.reset()
        self.parent.after(50, self.change_time)

           
    def autoclick(self):
        for team in self.teams:
            team.celkem.val = floor(team.celkem.val * (11/10)**team.farma.val)
            team.celkem.val = team.celkem.val + (team.babicka.val*team.klasik.param//2) 
            team.celkem.updatuj_parametr(team.celkem.val)
        
    def updatuj_hodnoty(self):
        for team in self.teams:
            try:
                for par in (team.obihani, team.kupovani):
                    for radek in par:
                        try:
                            radek.param = int(radek.parametr.get())
                        except AttributeError:
                            pass
                        radek.val = int(radek.mnozstvi.get())
            except ValueError:
                pass
        for par in self.cenik.radky:
            try:
                par.val = int(par.mnozstvi.get())
            except ValueError:
                pass

    def pause_resume(self, event = None):
        self.timer.change_label()
        self.total_Time.change_label()
        self.timer.pause_resume()
        self.total_Time.pause_resume()
        
    def check_keyboard_input(self, event):
        print(event.keycode)
        keycode = 0
        if event.char:
            keycode = ord(event.char)
        if event.keycode == 36:
            self.parent.focus()
        if event.char == "p":
            self.pause_resume()
        if event.char and keycode > ord("0") and keycode <= ord("0")+len(self.teams):
            self.teams[self.last_team].frame.configure(bg="lightgrey")
            id = keycode - ord("1") 
            # print(len(self.teams))
            self.last_team = id
            self.teams[id].frame.configure(bg="lightgreen")
        if event.char and keycode >= ord("a") and keycode < ord("a")+7:
            # for i in self.teams[self.last_team].kupovani: print(i)
            print(keycode, chr(keycode))
            if chr(keycode) == "g":
                self.teams[self.last_team].jail.val = 0
                self.teams[self.last_team].jail.updatuj_mnozstvi(0)
            else:
                self.teams[self.last_team].kupovani[keycode-ord("a")].koupit()
        
        

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Více skupin počítadel s názvy")
    game = Game(root, POCET_TEAMU)
    root.mainloop()