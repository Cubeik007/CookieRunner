import tkinter as tk
from math import log2


class Golden_cookie:
    def __init__(self, parent, row, label_text , group):
        self.buzzer = tk.Button(parent, text=f"Zlatý Cookie", command=self.golden_action)
        self.buzzer.grid(row = 0, column = 3, padx=5, pady=5)
        
    def golden_action(self):
        pass


class CounterRow:
    def __init__(self, parent, row, label_text, group):
        self.val = 0
        self.label = tk.Label(parent, text=f"{label_text}:")
        self.label.grid(row=row, column=0, padx=5, pady=5)

        self.mnozstvi = tk.Entry(parent, width=10)
        self.mnozstvi.grid(row=row, column=1, padx=5, pady=5)
        self.mnozstvi.insert(0, str(0))  # Výchozí hodnota
        
    def updatuj_parametr(self, new_value):
        self.mnozstvi.delete(0, tk.END)
        self.mnozstvi.insert(0, str(new_value))
    
class Obehnuti(CounterRow):
    def __init__(self, parent, row, label_text, group, default_param):
        super().__init__(parent, row, label_text, group)
        self.button = tk.Button(parent, text=f"Oběhnuto!", command=self.zvedni_obeh)
        self.button.grid(row=row, column=2, padx=5, pady=5)
        self.group = group
        
        self.parametr = tk.Entry(parent, width=10)
        self.parametr.grid(row=row, column=3, padx=5, pady=5)
        self.parametr.insert(0, str(default_param))  # Výchozí hodnota
        self.param = default_param
    
    def pricti_mnozstvi(self):
        # self.updatuj_mnozstvi()
        self.val = int(self.mnozstvi.get())  
        self.mnozstvi.delete(0, tk.END)
        self.val += 1
        self.mnozstvi.insert(0, self.val)
 
    def zvedni_obeh(self):
        pass
    
    def updatuj_parametr(self, new_value):
        self.parametr.delete(0, tk.END)
        self.parametr.insert(0, str(new_value))
        

class Klasik(Obehnuti):
    def __init__(self, parent, row, label_text, group, default = 1):
        super().__init__(parent, row, label_text, group, default)        

    def zvedni_obeh(self):
        self.pricti_mnozstvi()
        self.group.celkem.val += self.group.klasik.param
        self.group.celkem.updatuj_parametr(self.group.celkem.val)
        
class Pozadu(Obehnuti):
    def __init__(self, parent, row, label_text, val, default = 10):
        super().__init__(parent, row, label_text, val, default)        

    def zvedni_obeh(self):
        self.pricti_mnozstvi()
        if self.val % 5 == 0:
            self.group.klasik.param += self.group.pozadu.param
            self.group.klasik.updatuj_parametr(self.group.klasik.param)
        
class Poslepu(Obehnuti):
    def __init__(self, parent, row, label_text, group, default = 2):
        super().__init__(parent, row, label_text, group, default)

    def zvedni_obeh(self):
        self.pricti_mnozstvi()
        if self.val % 5 == 0 and self.val <= 50:
            self.group.klasik.param *= self.group.poslepu.param
            self.group.klasik.updatuj_parametr(self.group.klasik.param)
        
class Valeni(Obehnuti):
    def __init__(self, parent, row, label_text, group, default = 1):
        super().__init__(parent, row, label_text, group, default)

    def zvedni_obeh(self):
        self.pricti_mnozstvi()
        if log2(self.val).is_integer():
            self.group.poslepu.param += 1
            self.group.poslepu.updatuj_parametr(self.group.poslepu.param)