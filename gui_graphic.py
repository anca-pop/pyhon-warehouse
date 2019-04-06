from tkinter import *
import pygal
import dbConn
from tkcalendar import Calendar
import helper
import functools
import repository_operation as op
from datetime import datetime

class GUI_Graphic(helper.Helper):
    db = ''
    connectionObject = ''

    def __init__(self):
        self.db = dbConn.DB()
        self.connectionObject = self.db.get_connect()

    def show_calendar(self, event, param):
        def print_sel():
            param.set(cal.selection_get())
            top.destroy()

        top = Toplevel(self.create_graphic_window)
        cal = Calendar(top, font="Arial 14", selectionMode='day', locale='en_US',
                       cursor="hand1", year=2018, month=2, day=5)

        cal.pack(fill="both", expand=True)
        Button(top, text="ok", command=print_sel).pack()

    def generate_graphic(self, event):
        start = datetime.strftime(datetime.strptime(self.picked_start_date.get(), '%Y-%m-%d'), '%Y-%m-%d')
        end = datetime.strftime(datetime.strptime(self.picked_end_date.get(), '%Y-%m-%d'), '%Y-%m-%d')
        product_name = self.product_selected.get()
        product_id = self.products[product_name]
        operationInstance = op.Operation(self.connectionObject)
        response = operationInstance.get_operation_by_product_and_date(product_id, start, end)
        print(response)
        self.process_data_for_graphic(response,product_name)


    def draw(self, root):
        self.create_graphic_window = Toplevel(root)
        self.create_graphic_window.title('Genereaza grafic')
        
        #chose product
        Label(self.create_graphic_window, text='selecteaza un produs: ').pack(side=LEFT)
        self.products = self.get_all_products(self.connectionObject)
        options = list(self.products.keys())
        self.product_selected = StringVar()
        self.product_selected.set(options[0])  # default value
        product_menu = OptionMenu(self.create_graphic_window, self.product_selected, *options)
        product_menu.pack()
        
        #chose start date from calendar
        Label(self.create_graphic_window, text='Data de inceput aleasa:').pack()
        self.picked_start_date = StringVar()
        label_calendar = Label(self.create_graphic_window, textvariable=self.picked_start_date)
        label_calendar.pack()
        pick_start_date = Button(self.create_graphic_window, text='Alege data de inceput', fg='red')
        pick_start_date.bind('<Button-1>', functools.partial(self.show_calendar,param=self.picked_start_date))
        pick_start_date.pack()

        # chose start date from calendar
        Label(self.create_graphic_window, text='Data de sfarsit aleasa:').pack()
        self.picked_end_date = StringVar()
        label_calendar = Label(self.create_graphic_window, textvariable=self.picked_end_date)
        label_calendar.pack()
        pick_end_date = Button(self.create_graphic_window, text='Alege data de final', fg='red')
        pick_end_date.bind('<Button-1>', functools.partial(self.show_calendar,param=self.picked_end_date))
        pick_end_date.pack()

        button_save = Button(self.create_graphic_window, text='Genereaza graficul', fg='red')
        button_save.bind('<Button-1>', self.generate_graphic)
        button_save.pack()
