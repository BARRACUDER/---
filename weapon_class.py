far_weapon_list=[["пистолет",7,9,300,1,35],["автомат",120,30,450,1,45],["снайперская винтовка",0.7,25,1200,1,90]]
clos_weapon_list=[['sword' , 1.7, 2, 1.2 , 65],['spear' , 1.1 , 2 ,5 ,45 ],['morgenstern',0.9,2,1.5,80]]
magic_weapon_list=[["wooden posoh",300,160,0,5,30,1,0.9],["iron posoh",400,180,0,5,30,2,1],["gold posoh",450,190,1,45,3,1.2]]


class weapon:
    def __init__(self,name,far,damage,speed):
        self.name=name
        self.far=far
        self.damage=damage
        self.speed=speed
class far(weapon):
    def __init__(self,name,speed,capac,far,mult,damage):
        super().__init__(name,speed,far,damage)
        self.speed=speed
        self.capac=capac
        self.far=far
        self.mult=mult
    def __str__(self):
        return "name="+str(self.name)+" speed="+str(self.speed)+" capac="+str(self.capac)+" far="+str(self.far)+" mult="+str(self.mult)+" damage="+str(self.damage)
    
class clos(weapon):
    def __init__(self,name,size,far,damage,speed):
        super().__init__(name,far,damage,speed)
        self.size=size
    def __str__(self):
        return str(f"name={self.name} sped={self.speed} size={self.size} far={self.far} damage={self.damage}")
class magic(weapon):
    def __init__(self, name, far,cost,level,damage,splash,speed):
        super().__init__(name, far,damage,speed)
        self.cost=cost
        self.level=level
        self.splash=splash
    def __str__(self):
        return str(f"name={self.name} speed={self.speed} far={self.far} cost={self.cost} level={self.level} splash={self.splash} damage={self.damage}")
    
for i in far_weapon_list:
    wep=far(i[0],i[1],i[2],i[3],i[4],i[5])
    print(wep)
for i in clos_weapon_list:
    wep=clos(i[0],i[1],i[2],i[3],i[4])
    print(wep)
for i in magic_weapon_list:
    wep=magic(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
    print(wep)

