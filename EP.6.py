class Mancity:
    # Attribute
    mancity = 'Manchester City'

    # Constructor
    def __init__(self, name):
        print('Manchester City')
        self.name = name

    #def get_name(self):
    #    return self.name    

class Stats(Mancity):
    def __init__(self, name, goalsp, assistsp, goalsu, assistsu):
        super().__init__(name)
        self.goalsp = goalsp
        self.assistsp = assistsp
        self.goalsu = goalsu
        self.assistsu = assistsu 

    def get_goalsp(self):
        return self.goalsp

    def get_assistsp(self):
        return self.assistsp

    def get_goalsu(self):
        return self.goalsu

    def get_assistsu(self):
        return self.assistsu
        

print('----------ข้อมูลนักเตะ---------')
mancity01 = Stats('Erling Haaland', 30, 5, 11, 5)
print(f'ชื่อนักเตะ : {mancity01.name}') 
print(f'ยิงประตูใน Premier : {mancity01.get_goalsp()}')
print(f'ทำแอสซิสต์ใน Premier : {mancity01.get_assistsp()}')
print(f'ยิงประตูใน Ucl : {mancity01.get_goalsu()}')
print(f'ทำแอสซิสต์ใน Ucl : {mancity01.get_assistsu()}')
print('\n----------ข้อมูลนักเตะ---------')
mancity01 = Stats("Kevin De Bruyne", 5, 14, 1, 3)
print(f'ชื่อนักเตะ : {mancity01.name}') 
print(f'ยิงประตูใน Premier : {mancity01.get_goalsp()}')
print(f'ทำแอสซิสต์ใน Premier : {mancity01.get_assistsp()}')
print(f'ยิงประตูใน Ucl : {mancity01.get_goalsu()}')
print(f'ทำแอสซิสต์ใน Ucl : {mancity01.get_assistsu()}') 
print('\n----------ข้อมูลนักเตะ---------')
mancity01 = Stats('Jack Grealish', 5, 6, 0, 1)
print(f'ชื่อนักเตะ : {mancity01.name}') 
print(f'ยิงประตูใน Premier : {mancity01.get_goalsp()}')
print(f'ทำแอสซิสต์ใน Premier : {mancity01.get_assistsp()}')
print(f'ยิงประตูใน Ucl : {mancity01.get_goalsu()}')
print(f'ทำแอสซิสต์ใน Ucl : {mancity01.get_assistsu()}') 

            





