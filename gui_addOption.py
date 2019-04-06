from tkinter import *
import dbConn
import repository_operation as op
from tkcalendar import Calendar
from datetime import datetime
import helper
import re

class GUI_Operation(helper.Helper):

    db = ''
    connectionObject = ''

    def __init__(self):
        self.db = dbConn.DB()
        self.connectionObject = self.db.get_connect()

    def show_calendar(self, event):
        def print_sel():
            self.picked_date.set(cal.selection_get())
            top.destroy()

        top = Toplevel(self.operation_window)
        cal = Calendar(top, font="Arial 14", selectmode='day', locale='en_US',
                       cursor="hand1", year=2018, month=2, day=5)

        cal.pack(fill="both", expand=True)
        Button(top, text="ok", command=print_sel).pack()

    def save_operation(self, event):
        product_name = self.product_selected.get()
        product_id = self.products[product_name]
        type = int(self.var.get())
        quantity = self.product_quantity.get()
        if not re.match('^[0-9]*[.]{0,1}[0-9]*$', quantity):
            self.label_text.set('cantitatea trebuie sa contina doar cifre')
            return
        else:
            quantity = float(self.product_quantity.get())
        operation_data = datetime.strftime(datetime.strptime(self.picked_date.get(), '%Y-%m-%d'), '%Y-%m-%d')
        operationInstance = op.Operation(self.connectionObject)
        response = operationInstance.add(product_id, type, quantity, operation_data)
        self.label_text.set('Response:' + response['msg'])

    def draw(self, root):
        self.operation_window = Toplevel(root)
        self.operation_window.title('Adauga o operatiune noua')

        Label(self.operation_window, text="Selecteaza produsul: ").grid(row=0,column=0)
        self.products = self.get_all_products(self.connectionObject)
        options = list(self.products.keys())
        self.product_selected = StringVar(self.operation_window)
        self.product_selected.set(options[0])  # default value
        product_menu = OptionMenu(self.operation_window, self.product_selected, *options)
        product_menu.grid(row=0,column=1)

        Label(self.operation_window, text="Tipul operatiunii: ").grid(row=1,column=0)
        self.var = IntVar()
        inOp = Radiobutton(self.operation_window, text="intrare", variable=self.var, value=1)
        inOp.grid(row=1,column=1)
        outOp = Radiobutton(self.operation_window, text="iesire", variable=self.var, value=2)
        outOp.grid(row=2,column=1)

        Label(self.operation_window, text="cantitate: ").grid(row=3,column=0)
        self.product_quantity = Entry(self.operation_window)
        self.product_quantity.grid(row=3,column=1)

        # calendar
        button_show_calendar = Button(self.operation_window, text='Afiseaza calendarul', fg='red')
        button_show_calendar.bind('<Button-1>', self.show_calendar)
        button_show_calendar.grid(row=4,column=0)
        Label(self.operation_window, text='Data aleasa:').grid(row=4,column=1)
        self.picked_date = StringVar()
        label_calendar = Label(self.operation_window, textvariable=self.picked_date)
        label_calendar.grid(row=4,column=2)

        self.label_text = StringVar()
        Label(self.operation_window, textvariable=self.label_text).grid(row=5,column=1)

        button_save = Button(self.operation_window, text='Save', fg='red')
        button_save.bind('<Button-1>', self.save_operation)
        button_save.grid(row=5,column=0)
