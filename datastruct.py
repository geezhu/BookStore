'''create table book(title varchar(20), scor varchar(10)" \
                        ", author varchar(20), price varchar(10)" \
                        ", Ptime varchar(50), publish varchar(20)" \
                        ", person varchar(10), translator varchar(10)" \
                        ", tag varchar(10), brief varchar(500)" \
                        ", ISBN varchar(20) primary key)'''
class book():

    def __init__(self, title, scor,author,price,Ptime,publish,person,translator,tag,brief,ISBN):
        self.title = title
        self.scor = scor
        self.author = author
        self.price = price
        self.Ptime =Ptime
        self.publish = publish
        self.person = person
        self.translator = translator
        self.tag = tag
        self.brief = brief
        self.ISBN = ISBN


class userevalue():

    def __init__(self, username,evale,score):
        self.username = username
        self.evale = evale
        self.score = score


