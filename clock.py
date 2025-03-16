import tkinter as tk 
import time

class Timer():
    def __init__(self, parent, text, row, column):
        self.t = time.time()
        self.paused = False
        
        self.text = text
        self.frame = tk.Frame(parent, bd=2, relief=tk.SUNKEN)
        self.frame.grid(row=row, column=column, padx=10, pady=10, sticky="w")
        
        self.timer_label = tk.Label(self.frame, text=f"{text}: 0")
        self.timer_label.grid(row=0, column=0, padx=5, pady=5)
         
    def reset(self):
        self.t = time.time()
        
    def pause_resume(self):
        if not self.paused:
            self.dif = time.time()-self.t
            self.paused = True
        else:
            self.t = time.time() - self.dif
            self.paused = False
    
    def get_time(self):
        if self.paused:
            return self.dif
        print(self.t - time.time())
        return time.time() - self.t
    
    def change_label(self):
        formatted = time.strftime("%M:%S", time.gmtime(self.get_time()))
        self.timer_label.config(text = f"{self.text}: {formatted}")
