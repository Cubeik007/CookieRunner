import tkinter as tk
from math import log2

class CounterRow:
    def __init__(self, parent, row, label_text, group):
        self.label = tk.Label(parent, text=f"{label_text}:")
        self.label.grid(row=row, column=0, padx=5, pady=5)

        self.obehy = tk.Entry(parent, width=10)
        self.obehy.grid(row=row, column=1, padx=5, pady=5)
        self.obehy.insert(0, str(0))  # Výchozí hodnota
        
    
class Obehnuti(CounterRow):
    def __init__(self, parent, row, label_text, group, default = 1):
        super().__init__(parent, row, label_text, group)
        self.button = tk.Button(parent, text=f"Oběhnuto!", command=self.zvedni_obeh)
        self.button.grid(row=row, column=2, padx=5, pady=5)
        self.group = group
        
        self.parametr = tk.Entry(parent, width=10)
        self.parametr.grid(row=row, column=3, padx=5, pady=5)
        self.parametr.insert(0, str(default))  # Výchozí hodnota
        self.pocet_obehu = 0
    
    def pricti_obeh(self):
        self.updatuj_hodnoty()
        self.pocet_obehu = int(self.obehy.get())  
        self.obehy.delete(0, tk.END)
        self.pocet_obehu += 1
        self.obehy.insert(0, self.pocet_obehu)
        
    def updatuj_hodnoty(self):
        self.pocet_obehu = int(self.parametr.get())
        self.group.celkem.susenky = int(self.group.celkem.obehy.get())
        self.group.k = int(self.group.klasik.parametr.get())
        self.group.v = int(self.group.valeni.parametr.get())
        self.group.z = int(self.group.pozadu.parametr.get())
        self.group.s = int(self.group.poslepu.parametr.get())
 

    
    def zvedni_obeh(self):
        pass
        

class Klasik(Obehnuti):
    def __init__(self, parent, row, label_text, group, default = 1):
        super().__init__(parent, row, label_text, group, default)        

    def zvedni_obeh(self):
        self.pricti_obeh()
        self.group.celkem.obehy.delete(0, tk.END)  # Smaže současný text
        self.group.susenky += self.group.k
        self.group.celkem.obehy.insert(0, str(self.group.susenky))  # Přidá novou hodnotu
        
class Pozadu(Obehnuti):
    def __init__(self, parent, row, label_text, group, default = 10):
        super().__init__(parent, row, label_text, group, default)        

    def zvedni_obeh(self):
        self.pricti_obeh()
        if self.pocet_obehu % 5 == 0:
            self.group.klasik.parametr.delete(0, tk.END)  # Smaže současný text
            self.group.k += self.group.z
            self.group.klasik.parametr.insert(0, str(self.group.k))  # Přidá novou hodnotu
        
class Poslepu(Obehnuti):
    def __init__(self, parent, row, label_text, group, default = 2):
        super().__init__(parent, row, label_text, group, default)

    def zvedni_obeh(self):
        self.pricti_obeh()
        if self.pocet_obehu % 5 == 0 and self.pocet_obehu <= 50:
            self.group.klasik.parametr.delete(0, tk.END)  # Smaže současný text
            self.group.k *= self.group.s
            self.group.klasik.parametr.insert(0, str(self.group.k))  # Přidá novou hodnotu
        
class Valeni(Obehnuti):
    def __init__(self, parent, row, label_text, group, default = 1):
        super().__init__(parent, row, label_text, group, default)

    def zvedni_obeh(self):
        self.pricti_obeh()
        if log2(self.pocet_obehu).is_integer():
            self.group.poslepu.parametr.delete(0, tk.END)  # Smaže současný text
            self.group.s += 1
            self.group.poslepu.parametr.insert(0, str(self.group.s))  # Přidá novou hodnotu
            

class CounterGroup:
    def __init__(self, parent, row_start, column_start):
        """Vytvoří skupinu počítadel s vlastními labely a přírůstky."""
        self.susenky = 0
        self.k = 1
        self.z = 10
        self.s = 2
        self.v = 1
        self.frame = tk.Frame(parent, bd=2, relief=tk.SUNKEN)
        self.frame.grid(row=row_start, column=column_start, padx=10, pady=10, sticky="w")
        
        self.celkem = CounterRow(self.frame, 0, "Celkem", self)
        self.klasik = Klasik(self.frame, 1, "Klasik", self)
        self.pozadu = Pozadu(self.frame, 2, "Pozadu", self)
        self.poslepu = Poslepu(self.frame, 3, "Poslepu", self)
        self.valeni = Valeni(self.frame, 4, "Valeni", self)
        
        self.label = tk.Label(self.frame, text=f"Tým číslo {row_start+3*column_start+1}")
        self.label.grid(row=0, column=2, padx=5, pady=5)

# Vytvoření hlavního okna
root = tk.Tk()
root.title("Více skupin počítadel s názvy")

# Vytvoření více skupin s různými názvy labelů a přírůstky
for i in range(3):
    group1 = CounterGroup(root, i, 0)
for i in range(3):
    group1 = CounterGroup(root, i, 1)



# Spuštění hlavní smyčky
root.mainloop()