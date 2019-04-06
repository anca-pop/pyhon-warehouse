from tkinter import *
import dbConn
import repository_category as cat
import repository_product as prod
import re

class GUI_Product:

    db = ''
    connectionObject = ''

    def __init__(self):
        self.db = dbConn.DB()
        self.connectionObject = self.db.get_connect()

    def get_all_categories(self):
        categoryInstance = cat.Category(self.connectionObject)
        categories = categoryInstance.get_all_categories()
        result = {}
        for category in categories:
            result[category['denc']] = category['idc']
        return result

    def save_product(self, event):
        self.label_text.set('')
        name = self.product_name.get()
        if not re.match('^([a-zA-Z]*[\s]*)*[a-zA-Z]*$', name):
            self.label_text.set('Denumirea trebuie sa contrina doar litere si spatii')
            return
        price = self.product_price.get()
        if not re.match('^[0-9]*[.]{0,1}[0-9]*$', price):
            self.label_text.set('pretul trebuie sa contina doar cifre')
            return
        else:
            price = float(self.product_price.get())
        category_name = self.category_selected.get()
        category_id = self.categories[category_name]
        productInstance = prod.Product(self.connectionObject)
        response = productInstance.add(category_id,name,price)
        self.label_text.set(name + ' , Response:' + response['msg'])
        self.entry_price.set('')
        self.entry_name.set('')

    def draw(self, root):
        product_window = Toplevel(root)
        product_window.title('Adauga un produs nou')
        Label(product_window, text="Numele Produsului: ").grid(row=0,column=0)
        self.entry_name = StringVar()
        self.product_name = Entry(product_window, textvariable=self.entry_name)
        self.product_name.grid(row=0,column=1)

        Label(product_window, text="Pretul Produsului: ").grid(row=1,column=0)
        self.entry_price = StringVar()
        self.product_price = Entry(product_window, textvariable=self.entry_price)
        self.product_price.grid(row=1,column=1)

        Label(product_window, text="Alege categoria: ").grid(row=2,column=0)
        self.categories = self.get_all_categories()
        options = list(self.categories.keys())
        self.category_selected = StringVar(product_window)
        self.category_selected.set(options[0]) # default value
        self.category_menu = OptionMenu(product_window, self.category_selected, *options)
        self.category_menu.grid(row=2,column=1)

        self.label_text = StringVar()
        Label(product_window, textvariable=self.label_text).grid(row=3,column=1)

        button_save = Button(product_window, text='Save', fg='red')
        button_save.bind('<Button-1>', self.save_product)
        button_save.grid(row=3,column=0)


