import tkinter as tk
from math import log2, floor
from behani import CounterRow

class Obchod(CounterRow):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, 4)
        self.cenik = cenik
        self.group = group    
        self.button = tk.Button(parent, text=f"Koupit! ({chr(row+ord("a"))})", command=self.koupit)
        self.button.grid(row=row, column=6, padx=5, pady=5)
        
    def koupit(self):
        pass
    
    def zaplatit(self, counter, nova_cena = 0):
        if self.group.celkem.val < counter.val:
            return False
        self.group.celkem.val -= counter.val
        self.group.celkem.updatuj_mnozstvi(self.group.celkem.val)
        self.val += 1
        self.updatuj_mnozstvi(self.val)
        self.zvedni_ceny(counter, nova_cena)
        self.group.achievements.check_achievements(self.group)
        return True        
    
    def zvedni_ceny(self, counter, nova_cena):
        print(nova_cena)
        counter.updatuj_mnozstvi(nova_cena)
        
    
class Babicka(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
        
    def koupit(self):
        self.zaplatit(self.cenik.babicka_counter, floor(self.cenik.babicka_counter.val*1.2))

class Farma(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
        
    def koupit(self):
        self.zaplatit(self.cenik.farma_counter, floor(self.cenik.farma_counter.val*1.2))
            
class Dalnice(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
     
    def koupit(self):
        if self.val == 0:
            self.zaplatit(self.cenik.dalnice_counter, self.cenik.dalnice_counter.val)
            
class Org(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
     
    def koupit(self):
        self.zaplatit(self.cenik.org_counter, floor(self.cenik.org_counter.val*2))
    
class Xorg(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
     
    def koupit(self):
        self.zaplatit(self.cenik.xorg_counter, floor(self.cenik.xorg_counter.val*2))

class Jail(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
     
    def koupit(self):
        if self.val == 0:
            print("Hello", self.cenik.jail_counter.val)
            self.zaplatit(self.cenik.jail_counter, self.cenik.jail_counter.val*2)