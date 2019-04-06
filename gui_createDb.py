from tkinter import *
import DDLquerys
import dbConn

class GUI_CreateTables:

    db = ''
    connectionObject = ''

    def __init__(self):
        self.db = dbConn.DB()
        self.connectionObject = self.db.get_connect()

    def set_tables(self, event):
        response = DDLquerys.DDLquerys(self.connectionObject).create_tables()
        print("response:{}".format(response))
        self.label_text.set(response['msg'])

    def draw(self, root):
        create_table_window = Toplevel(root)
        create_table_window.title('Creeaza tabele')
        self.label_text = StringVar()
        Label(create_table_window, textvariable=self.label_text).pack(side=LEFT)
        button_save = Button(create_table_window, text='Creeaza tabelele', fg='red')
        button_save.bind('<Button-1>', self.set_tables)
        button_save.pack(side=LEFT)