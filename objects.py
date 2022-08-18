class Medium:
    def __init__(self, title, year):
        self._title = title           # Protected in order to be inherited
        self._year = year             # Protected in order to be inherited
            

class Book(Medium):
    def __init__(self, title, author, publication_year, subtitle, pagecount):
        self.__author = author        # Private, therefore not inheritable
        self.__subtitle = subtitle    # Private, therefore not inheritable
        self.__pagecount = pagecount  # Private, therefore not inheritable

        Medium.__init__(self,title,publication_year)

    
    def __del__(self):
        print(f'The book instance "{self._title}" was successfully deleted.')
    
    def book_info(self):
        print('Title:', self._title)
        if self.__subtitle != '':
            print('Subtitle:', self.__subtitle)
        print('Author:', self.__author)
        print('Publication:', self._year)
        print('Pages:', self.__pagecount)


    
        
int_invest = Book('The Intelligent Investor','Benjamin Graham',1949,'',640)
uni_berk_hath = Book(
    'University of Berkshire Hathaway',
    'Daniel Pecaut and Corey Wrenn',
    2017,
    '30+ Years of Lessons Learned from Warren Buffett & Charlie Munger',
    378)
oneup_wallstreet = Book('One Up on Wall Street','Peter Lynch',1989,'',318)

int_invest.book_info()
uni_berk_hath.book_info()
oneup_wallstreet.book_info()

