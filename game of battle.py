class Move:
    def __init__(self,name,damage):
        self.name=name
        self.damage=damage
m1=Move("Fireball",30)
m2=Move("Punch",20)
m3=Move("SLASH",10)
m4=Move("Kick",20)
class Creature:
    def __init__(self,name,hp):
        self.name=name
        self.hp=hp
        self.moves=[]
    def add_move(self,move):
        self.moves.append(move)
    def show_moves(self):
        for i,move in enumerate(self.moves):
            print(i+1,move.name)
    def take_damage(self,damage):
        self.hp-=damage
    def attack(self,enemy,move):
        enemy.take_damage(move.damage)
        print(enemy.name,"has",enemy.hp,"HP left")
        print(self.name,"used",move.name)
        print(enemy.name,"lost",move.damage,"HP")
    def is_alive(self):
        return self.hp>0
c1=Creature("Dragon",100)
c2=Creature("Knight",100)
c1.add_move(m1)
c1.add_move(m3)
c2.add_move(m2)
c2.add_move(m4)
class Battle:
    def __init__(self,c1,c2):
        self.c1=c1
        self.c2=c2
    def start(self):
        print("CREATURE BATTLE GAME")
        while self.c1.is_alive() and self.c2.is_alive():
            print(self.c1.name,"TURN")
            self.c1.show_moves()
            choice=int(input("CHOOSE MOVE: "))
            selected_move=self.c1.moves[choice-1]
            self.c1.attack(self.c2,selected_move)
            if not self.c2.is_alive():
                break
            print(self.c2.name,"TURN")
            self.c2.show_moves()
            choice=int(input("CHOOSE MOVE: "))
            selected_move=self.c2.moves[choice-1]
            self.c2.attack(self.c1,selected_move)
            if not self.c1.is_alive():
                break
        if self.c1.is_alive():
             print(self.c1.name,"WINS")
        else:
             print(self.c2.name,"WINS")
b1=Battle(c1,c2)
b1.start()