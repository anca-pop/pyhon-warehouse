from tkinter import *
import gui_addCategory as cat
import gui_addProduct as prod
import gui_addOption as opt
import gui_createDb as ddl
import gui_graphic as grafic


def show_category_window():
    gui_cat = cat.GUI_Category()
    gui_cat.draw(root)

def show_product_window():
    gui_prod = prod.GUI_Product()
    gui_prod.draw(root)

def show_operation_window():
    gui_opt = opt.GUI_Operation()
    gui_opt.draw(root)

def show_table_window():
    gui_ddl = ddl.GUI_CreateTables()
    gui_ddl.draw(root)

def show_graphic_window():
    gui_ddl = grafic.GUI_Graphic()
    gui_ddl.draw(root)

root = Tk()

menubar = Menu(root)

newmenu = Menu(menubar, tearoff=0)
newmenu.add_command(label="Categorie", command=show_category_window)
newmenu.add_command(label="Produs", command=show_product_window)
newmenu.add_command(label="Operatiune", command=show_operation_window)
menubar.add_cascade(label="Adauga", menu=newmenu)
menubar.add_cascade(label="Tabele", command=show_table_window)
menubar.add_cascade(label="Grafic", command=show_graphic_window)


root.config(menu=menubar)
root.mainloop()