from tkinter import *
import dbConn
import repository_category as cat

class GUI_Category:

    db = ''
    connectionObject = ''

    def __init__(self):
        self.db = dbConn.DB()
        self.connectionObject = self.db.get_connect()

    def save_category(self, event):
        category = cat.Category(self.connectionObject)
        name = self.category_name.get()
        if re.match('^([a-zA-Z]*[\s]*)*[a-zA-Z]*$', name):
            response = category.add(name)
            self.label_text.set(name + ' , Response:' + response['msg'] )
            self.entry_text.set('')
        else:
            self.label_text.set('numele trebuie sa contina doar litere si spatii')


    def draw(self, root):
        category_window = Toplevel(root)
        category_window.title('Adauga o categorie noua')
        Label(category_window, text="Numele Categoriei: ").grid(row=0,column=0)
        self.entry_text = StringVar()
        self.category_name = Entry(category_window, textvariable=self.entry_text)
        self.category_name.grid(row=0,column=1)
        self.label_text = StringVar()
        Label(category_window, textvariable=self.label_text).grid(row=1,column=0)
        button_save = Button(category_window, text='Save', fg='red')
        button_save.bind('<Button-1>', self.save_category)
        button_save.grid(row=1,column=1)
