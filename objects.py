class Book:
    def __init__(self, title):
        self.__title = title
    
    def __del__(self):
        print(f'The book instance "{self.__title}" was successfully deleted.')
    
    def display_book(self):
        print('Book title:', self.__title)

    

int_invest = Book('The Intelligent Investor')

print(int_invest)

#print('Public member title of book:', int_invest.__title)

int_invest.display_book()

del int_invest
