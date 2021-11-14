import random
m=[]
n=[] 
print('Введіть кількість гравців ')
x=int(input())
b=[] 
v=['6','7','8','9','10','В','Д','К','А'] 
c=['Бубна','Чирва','Піка','Трефа'] 
class Card: 
  def __init__ (self,suit,value): 
      self.suit=suit
      self.value=value 
def gen (): 
    global deck 
    for z in v: 
        for l in c: 
            b.append(Card(l,z)) 
def otobr(Card): 
     print(Card.suit,Card.value) 
class Player: 
  def __init__(self,nomer,karta1, karta2, karta3, karta4, karta5, karta6): 
          self.nomer=nomer
          self.karta1=karta1
          self.karta2=karta2
          self.karta3=karta3
          self.karta4=karta4
          self.karta5=karta5
          self.karta6=karta6
def otobrpla(nomer): 
          print ('Номер гравця ',nomer+1)
          print ('Карти гравця ')
          otobr(m[nomer].karta1),otobr(m[nomer].karta3),otobr(m[nomer].karta4),otobr(m[nomer].karta5),otobr(m[nomer].karta6),otobr(m[nomer].karta2)
          print (' ')
def datkart(nomer): 
     global players
     global deck
     karta1=b.pop()
     karta2=b.pop()
     karta3=b.pop()
     karta4=b.pop()
     karta5=b.pop()
     karta6=b.pop()
     m.append(Player(nomer,karta1,karta2,karta3, karta4, karta5, karta6))
def genstol(kol): 
     global deck
     global stol
     for i in range(kol):
          n.append(b.pop())
def otobrstol():   
   global stol
   for  i in n:
     otobr(i)
gen() 
random.shuffle(b) 
for i in range (x): 
  datkart (i)
  otobrpla(i)
def show(self):
        for card in self.cards:
            print (card.show())
def shuffle(self, q=1):
        length = len(self.cards)
        for _ in range(q):
            for i in range(length-1, 0, -1):
                randi = random.randint(0, i)
                if i == randi:
                    continue
                self.cards[i], self.cards[randi] = self.cards[randi], self.cards[i]