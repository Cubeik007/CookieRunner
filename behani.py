import tkinter as tk
from math import log2


class Golden_cookie:
    def __init__(self, parent, group, teams):
        self.buzzer = tk.Button(parent, text=f"Zlatý Cookie", command=self.golden_action)
        self.buzzer.grid(row = 0, column = 3, padx=5, pady=5)
        self.group = group
        self.teams = teams
        
    def golden_action(self):
        self.group.babicka.val += 1
        self.group.babicka.updatuj_mnozstvi(self.group.babicka.val)
        self.group.farma.val += 1
        self.group.farma.updatuj_mnozstvi(self.group.farma.val)
        k = self.get_total_klasik()
        self.group.celkem.val += (k*5)
        self.group.celkem.updatuj_mnozstvi(self.group.celkem.val)
        self.group.pozadu.param += 10
        
    def get_total_klasik(self):
        sum = 0
        for team in self.teams:
            sum += team.klasik.param
        return sum
        
        


class CounterRow:
    def __init__(self, parent, row, label_text, col = 0):
        self.val = 0
        self.label = tk.Label(parent, text=f"{label_text}:")
        self.label.grid(row=row, column=col , padx=5, pady=5)

        self.mnozstvi = tk.Entry(parent, width=10)
        self.mnozstvi.grid(row=row, column=col+1, padx=5, pady=5)
        self.mnozstvi.insert(0, str(0))  # Výchozí hodnota
        self.param = 0
        
    def updatuj_mnozstvi(self, new_value):
        self.mnozstvi.delete(0, tk.END)
        self.mnozstvi.insert(0, str(new_value))
        
    def updatuj_parametr(self, new_value):
        self.updatuj_mnozstvi(new_value)
    
class Obehnuti(CounterRow):
    def __init__(self, parent, row, label_text, group, default_param):
        super().__init__(parent, row, label_text)
        self.button = tk.Button(parent, text=f"Oběhnuto!", command=self.obehnuto)
        self.button.grid(row=row, column=2, padx=5, pady=5)
        self.group = group
        
        self.parametr = tk.Entry(parent, width=10)
        self.parametr.grid(row=row, column=3, padx=5, pady=5)
        self.parametr.insert(0, str(default_param))  # Výchozí hodnota
        self.param = default_param
    
    def pricti_mnozstvi(self):
        self.val = int(self.mnozstvi.get())  
        self.val += 1
        self.updatuj_mnozstvi(self.val)
 
    def obehnuto(self):
        pass
    
    def updatuj_parametr(self, new_value):
        self.parametr.delete(0, tk.END)
        self.parametr.insert(0, str(new_value))
        

class Klasik(Obehnuti):
    def __init__(self, parent, row, label_text, group, default = 1):
        super().__init__(parent, row, label_text, group, default)        

    def obehnuto(self):
        self.pricti_mnozstvi()
        self.group.celkem.val += self.group.klasik.param
        self.group.celkem.updatuj_parametr(self.group.celkem.val)
        
class Pozadu(Obehnuti):
    def __init__(self, parent, row, label_text, group, default = 10):
        super().__init__(parent, row, label_text, group, default)        

    def obehnuto(self):
        self.pricti_mnozstvi()
        if self.val % 5 == 0:
            self.group.klasik.param += self.group.pozadu.param
            self.group.klasik.updatuj_parametr(self.group.klasik.param)
        
class Poslepu(Obehnuti):
    def __init__(self, parent, row, label_text, group, default = 2):
        super().__init__(parent, row, label_text, group, default)

    def obehnuto(self):
        self.pricti_mnozstvi()
        if self.val % 5 == 0 and self.val <= 50:
            self.group.klasik.param *= self.group.poslepu.param
            self.group.klasik.updatuj_parametr(self.group.klasik.param)
        
class Valeni(Obehnuti):
    def __init__(self, parent, row, label_text, group, default = 1):
        super().__init__(parent, row, label_text, group, default)

    def obehnuto(self):
        self.pricti_mnozstvi()
        if log2(self.val).is_integer():
            self.group.poslepu.param += 1
            self.group.poslepu.updatuj_parametr(self.group.poslepu.param)