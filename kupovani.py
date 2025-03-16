import tkinter as tk
from math import log2, floor
from behani import CounterRow

class Obchod(CounterRow):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, 4)
        self.cenik = cenik
        self.group = group    
        self.button = tk.Button(parent, text=f"Koupit!", command=self.koupit)
        self.button.grid(row=row, column=6, padx=5, pady=5)
        
    def koupit(self):
        pass
    
    def zaplatit(self, counter, zvednuti = 0):
        if self.group.celkem.val < counter.val:
            return False
        self.group.celkem.val -= counter.val
        self.group.celkem.updatuj_mnozstvi(self.group.celkem.val)
        self.val += 1
        self.updatuj_mnozstvi(self.val)
        self.zvedni_ceny(counter, zvednuti)
        return True        
    
    def zvedni_ceny(self, counter, zvednuti):
        counter.updatuj_mnozstvi(zvednuti)
        
    
class Babicka(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
        
    def koupit(self):
        self.zaplatit(self.cenik.babicka_counter, floor(self.cenik.babicka_counter.val*1.2))
            # self.cenik.babicka_counter.cena.delete(0, tk.END)
            # self.cenik.babicka_counter.val = floor(self.cenik.babicka_counter.val*1.2)
            # self.cenik.babicka_counter.cena.insert(0, str(self.cenik.babicka))

class Farma(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
        
    def koupit(self):
        self.zaplatit(self.cenik.farma, floor(self.cenik.farma*1.2))
            # self.val += 1
            # self.updatuj_mnozstvi(self.val)
            # self.cenik.farma_counter.cena.delete(0, tk.END)
            # self.cenik.farma = floor(self.cenik.farma*1.2)
            # self.cenik.farma_counter.cena.insert(0, str(self.cenik.farma))

            
class Dalnice(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
     
    def koupit(self):
        if self.val == 0:
            self.zaplatit(self.cenik.dalnice)
            
class Org(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
     
    def koupit(self):
        if self.val == 0:
            self.zaplatit(self.cenik.org)
    
class Xorg(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
     
    def koupit(self):
        if self.val == 0:
            self.zaplatit(self.cenik.xorg)
