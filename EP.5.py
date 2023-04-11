# นักเตะที่ยิงประตูได้มากกว่าเท่ากับ 15 ประตู ใน Premier League 2022-23
def checkage(player):
    for p in player.items():
        if p[1] >=15:
            print(p[0], p[1])

player = {'Haaland':30,'Harry Kane':23,'Ivan Toney':18,'Rashford':15,'Martinelli':14,'Salah':13,'Saka':12,'Rodrigo':10,'Odegaard':10,'Foden':9}    

checkage(player)