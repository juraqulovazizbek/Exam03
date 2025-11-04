class Book:
    def __init__(self , title , author , year):
        self.title = title
        self.author = author
        self.year = year

a = Book("xamsa", "Alisher Navoiy", 1400)
b = Book("Yulduzlar jangi", "Juraqulov Azizbek", 2015)
print(a.title)
print(b.author)
print(a.year)