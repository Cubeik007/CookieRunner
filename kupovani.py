import tkinter as tk
from math import log2, floor

class Obchod:
    def __init__(self, parent, row, label_text, group, cenik):
        self.cenik = cenik
        self.group = group
        self.label = tk.Label(parent, text=f"{label_text}:")
        self.label.grid(row=row, column=4, padx=5, pady=5)
        
        self.mnozstvi = tk.Entry(parent, width=10)
        self.mnozstvi.grid(row=row, column=5, padx=5, pady=5)
        self.mnozstvi.insert(0, str(0))  # Výchozí hodnota
        
        self.button = tk.Button(parent, text=f"Koupit!", command=self.koupit)
        self.button.grid(row=row, column=6, padx=5, pady=5)
        self.group = group
        
        
    def koupit(self):
        pass
    
    def zaplatit(self, cena):
        if self.group.susenky < cena:
            return False
        self.group.celkem.obehy.delete(0, tk.END)
        self.group.susenky -= cena
        self.group.celkem.obehy.insert(0, str(self.group.susenky))  # Přidá novou hodnotu
        return True

    
class Babicka(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
        
    def koupit(self):
        if self.zaplatit(self.cenik.babicka):
            self.mnozstvi.delete(0, tk.END) 
            self.group.b += 1
            self.mnozstvi.insert(0, str(self.group.b)) 
            self.cenik.babicka_counter.cena.delete(0, tk.END)
            self.cenik.babicka = floor(self.cenik.babicka*1.2)
            self.cenik.babicka_counter.cena.insert(0, str(self.cenik.babicka))

class Farma(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
        
    def koupit(self):
        if self.zaplatit(self.cenik.farma):
            self.mnozstvi.delete(0, tk.END)  
            self.group.f += 1
            self.mnozstvi.insert(0, str(self.group.f))
            self.cenik.farma_counter.cena.delete(0, tk.END)
            self.cenik.farma = floor(self.cenik.farma*1.2)
            self.cenik.farma_counter.cena.insert(0, str(self.cenik.farma))

            
class Dalnice(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
     
    def koupit(self):
        if self.group.d == 0 and self.zaplatit(self.cenik.dalnice):
            self.mnozstvi.delete(0, tk.END)
            self.group.d += 1
            self.mnozstvi.insert(0, str(self.group.d))
            
class Org(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
     
    def koupit(self):
        if self.group.o == 0 and self.zaplatit(self.cenik.org):
            self.mnozstvi.delete(0, tk.END)
            self.group.o += 1
            self.mnozstvi.insert(0, str(self.group.o))
    
class Xorg(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
     
    def koupit(self):
        if self.group.x == 0 and self.zaplatit(self.cenik.xorg):
            self.mnozstvi.delete(0, tk.END)
            self.group.x += 1
            self.mnozstvi.insert(0, str(self.group.x))