class Library():
    def __init__(self, number, name, author, year):
        self.number=number
        self.name=name
        self.author=author
        self.year=year
    def description(self):
        desc=str(self.number)+" "+self.name+" "+self.author+" "+str(self.year)
        return desc.title()
    def del_book(self, number):
        if self.number==number :
           del self 
m="lib.txt"
n=open(m,"+w",encoding ='utf-8')
print("Додавання книг ")
while True: 
    try:
        i=input("Натисніть '1', щоб ввести книгу ")
        if i =="1":
          N=input("Введіть номер книги ")
          b=input("Введіте назву книги ")
          v=input("Введіть автора книги ")
          c=input("Введіть рік видання книги ")
          N=Library(b,v,c,N)
          n.write(N.description())
          n.write("\n")
          print("Ви ввели ", N.description()) 
          continue
        else:
            break
    except ValueError:
        print("Помилка")
print("Виберіть, що хочете зробити: 1.Вивести всі книги 2.Видалити книгу 3.Знайти книгу 4.Знайти книгу по номеру")
x=input(" ")
if x=="1":
    n=open(m,"r") 
    print(n.read())
    n.close()
elif x=="2":
    n=open(m,"w") 
    n.write()
    n.close() 
elif x=="3":
 U=input("Пошук ")
 n=open(m,"r",encoding ='utf-8')
 read=n.read() 
 if U in read :
    print("Є в бібліотеці")
 else:
    print("Немає в бібліотеці")
 n.close()
elif x=="4":
 U=int(input("Пошук по номеру "))
 n=open(m,"r",encoding ='utf-8')
 read=n.read() 
 if str(U) in read :
    print("Є в бібліотеці")
 else:
    print("Немає в бібліотеці")
 n.close() 