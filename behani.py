import tkinter as tk
from math import log2


class Golden_cookie:
    def __init__(self, parent, row, label_text , group):
        self.buzzer = tk.Button(parent, text=f"Zlatý Cookie", command=self.golden_action)
        self.buzzer.grid(row = 0, column = 3, padx=5, pady=5)
        
    def golden_action(self):
        pass


class CounterRow:
    def __init__(self, parent, row, label_text, val, group):
        self.val = val
        self.label = tk.Label(parent, text=f"{label_text}:")
        self.label.grid(row=row, column=0, padx=5, pady=5)

        self.obehy = tk.Entry(parent, width=10)
        self.obehy.grid(row=row, column=1, padx=5, pady=5)
        self.obehy.insert(0, str(0))  # Výchozí hodnota
        
    def updatuj_parametr(self, new_value):
        self.obehy.delete(0, tk.END)
        self.obehy.insert(0, str(new_value))
    
class Obehnuti(CounterRow):
    def __init__(self, parent, row, label_text, val, group, default = 1):
        super().__init__(parent, row, label_text, val, group)
        self.button = tk.Button(parent, text=f"Oběhnuto!", command=self.zvedni_obeh)
        self.button.grid(row=row, column=2, padx=5, pady=5)
        self.group = group
        
        self.parametr = tk.Entry(parent, width=10)
        self.parametr.grid(row=row, column=3, padx=5, pady=5)
        self.parametr.insert(0, str(default))  # Výchozí hodnota
        self.pocet_obehu = 0
    
    def pricti_obeh(self):
        self.updatuj_obehy()
        self.pocet_obehu = int(self.obehy.get())  
        self.obehy.delete(0, tk.END)
        self.pocet_obehu += 1
        self.obehy.insert(0, self.pocet_obehu)
        
    def updatuj_obehy(self):
        self.pocet_obehu = int(self.parametr.get())
 
    def zvedni_obeh(self):
        pass
    
    def updatuj_parametr(self, new_value):
        self.parametr.delete(0, tk.END)
        self.parametr.insert(0, str(new_value))
        

class Klasik(Obehnuti):
    def __init__(self, parent, row, label_text, val, group, default = 1):
        super().__init__(parent, row, label_text, val, group, default)        

    def zvedni_obeh(self):
        self.pricti_obeh()
        self.group.celkem.val += self.group.klasik.val
        self.group.celkem.updatuj_parametr(self.group.celkem.val)
        
class Pozadu(Obehnuti):
    def __init__(self, parent, row, label_text, val, group, default = 10):
        super().__init__(parent, row, label_text, val, group, default)        

    def zvedni_obeh(self):
        self.pricti_obeh()
        if self.pocet_obehu % 5 == 0:
            self.group.klasik.val += self.group.pozadu.val
            self.group.klasik.updatuj_parametr(self.group.klasik.val)
        
class Poslepu(Obehnuti):
    def __init__(self, parent, row, label_text,val,  group, default = 2):
        super().__init__(parent, row, label_text, val, group, default)

    def zvedni_obeh(self):
        self.pricti_obeh()
        if self.pocet_obehu % 5 == 0 and self.pocet_obehu <= 50:
            self.group.klasik.val *= self.group.poslepu.val
            self.group.klasik.updatuj_parametr(self.group.klasik.val)
        
class Valeni(Obehnuti):
    def __init__(self, parent, row, label_text, val, group, default = 1):
        super().__init__(parent, row, label_text, val, group, default)

    def zvedni_obeh(self):
        self.pricti_obeh()
        if log2(self.pocet_obehu).is_integer():
            self.group.poslepu.val += 1
            self.group.poslepu.updatuj_parametr(self.group.poslepu.val)