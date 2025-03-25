import tkinter as tk



class Achievements():
    def __init__(self, parent, teams):
        self.frame = tk.Frame(parent, bd=2, relief=tk.SUNKEN)
        self.frame.grid(row=0, column=2, rowspan=3, padx=10, pady=10, sticky="w")
        
        self.teams = teams
        
        self.names = ["Rychlík", "Lenoch", "Pracháč", "Milionář", "Slepec", "Ničitel", "Úplatkář", "Samotář", "Inovátor", "Ochranář"]
        self.claimed = [0 for _ in range(len(self.names))]
        self.milestones = []
        for i, mile in enumerate(self.names):
            self.milestones.append(Milestone(self.frame, mile, 2*i))
            
    def check_achievements(self, team):
        for i, val in enumerate(self.claimed):
            if int(self.milestones[i].team.get()) != 0:
                    self.claimed[i] = 1
                    val = 1
            if not val:
                change = False
                match i:
                    case 0:
                        if team.celkem.val > 0: 
                            change = True
                            team.pozadu.param += 2
                            team.pozadu.updatuj_parametr(team.pozadu.param)
                    case 1:
                        if self.lenoch():
                            change = True
                            team.celkem.val += 50
                            team.celkem.updatuj_mnozstvi(team.celkem.val)
                    case 2:
                        if team.celkem.val >= 1000:
                            change = True
                            team.pozadu.param += 15
                            team.pozadu.updatuj_parametr(team.pozadu.param )
                    case 3:
                        if team.celkem.val >= 1000000:
                            change = True
                            team.babicka.val += 5
                            team.babicka.updatuj_mnozstvi(team.babicka.val)
                    case 4:
                        if team.poslepu.val >= 15:
                            change = True
                            team.poslepu.param += 1
                            team.poslepu.updatuj_parametr(team.poslepu.param)
                    case 5:
                        if team.xorg.val >= 3:
                            change = True
                            team.celkem.val += 5000
                            team.celkem.updatuj_mnozstvi(team.celkem.val)
                    case 6:
                        if team.jail.val > 0:
                            change = True
                            team.celkem.val += 15000
                            team.celkem.updatuj_mnozstvi(team.celkem.val)
                    case 7: 
                        if self.samotar():
                            change = True
                            team.babicka.val += 2
                            team.babicka.updatuj_mnozstvi(team.babicka.val)
                    case 8:
                        if self.inovator(team):
                            change = True
                            team.farma.val += 2
                            team.farma.updatuj_mnozstvi(team.farma.val)

                    case 9:
                        if self.ochranar():
                            change=True
                            team.celkem.val += 20000
                            team.celkem.updatuj_mnozstvi(team.celkem.val)
                if change == True:
                    self.milestones[i].nastav_team(team.id)
                    self.claimed[i] = 1
      
    def ochranar(self):
        i = 0
        for team in self.teams:
            if team.dalnice.val > 0:
                i += 1
        if i == len(self.teams):
            return True  
                    
    def lenoch(self):
        i = 0
        for team in self.teams:
            if team.celkem.val > 0:
                i += 1
        if i == len(self.teams):
            return True
    
    def samotar(self):
        i = 0
        for team in self.teams:
            if team.babicka.val > 0:
                i += 1
        if i == len(self.teams):
            return True
        
    # def uplatkar(self):
    #     i = 0
    #     for team in self.teams:
    #         if team.jail.val > 0:
    #             i += 1
    #     if i == 3:
    #         return True
        
    def inovator(self, team):
        return team.farma.val - 3 >= team.babicka.val 
        
                     

class Milestone():
    def __init__(self, parent, label_text, row):
        self.label = tk.Label(parent, text=f"{label_text}:")
        self.label.grid(row=row, column=0 , padx=5, pady=5)
        self.team = tk.Entry(parent, width=10)
        self.team.grid(row=row+1, column=0, padx=5, pady=5)
        self.team.insert(0, str(0))  # Výchozí hodnota
    
    def nastav_team(self, id):  
        self.team.delete(0, tk.END)
        self.team.insert(0, str(id))


# class FirstCookie(Achievements):
    