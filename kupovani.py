import tkinter as tk
from math import log2

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
        
        self.cena = tk.Entry(parent, width=10)
        self.cena.grid(row=row, column=7, padx=5, pady=5)
        self.cena.insert(0, str(0))  # Výchozí hodnota
        
        
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
        self.cena.delete(0, tk.END)
        self.cena.insert(0, str(self.cenik.babicka))
        
    def koupit(self):
        if self.zaplatit(self.cenik.babicka):
            self.mnozstvi.delete(0, tk.END)  # Smaže současný text
            self.group.b += 1
            self.mnozstvi.insert(0, str(self.group.b))  # Přidá novou hodnotu

class Farma(Obchod):
    def __init__(self, parent, row, label_text, group, cenik):
        super().__init__(parent, row, label_text, group, cenik)
        self.cena.delete(0, tk.END)
        self.cena.insert(0, str(self.cenik.farma))
        
    def koupit(self):
        if self.zaplatit(self.cenik.farma):
            self.mnozstvi.delete(0, tk.END)  # Smaže současný text
            self.group.f += 1
            self.mnozstvi.insert(0, str(self.group.f))  # Přidá novou hodnotu
            