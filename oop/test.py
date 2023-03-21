# class Song:
#     def __init__(self, author, title, year):
#         self.author = author
#         self.title = title
#         self.year = year
#     def show_author(self):
#         return f'Автор этой песни {self.author}'
#     def show_title(self):
#         return f'Название этой песни {self.title}'
#     def show_year(self):
#         return f'Эта песня вышла в {self.year} году'
#     def __str__(self):
#         return f'{self.author},{self.title},{self.year}'
# song = Song(author = 'Pharrell Williams', title = 'Happy',year = 2013)
# print(song.show_title())
# print(song.show_author())
# print(song.show_year())



class Contact:
    __phone = None
    @property
    def phone(self):
        return self.__phone
  
        
obj = Contact()
obj.phone = 123