from Tkinter import Tk
import Tkinter
import ttk
import tkFileDialog as fd

import os

class interface:
    def __init__(slef, root):


        slef.cur_dir = None


        style = ttk.Style()
        style.theme_use("clam")
        slef.content = ttk.Frame(root)
        frame = ttk.Frame(slef.content, borderwidth=5, relief="sunken",width="400" , height=100)
        choose_path_btn = ttk.Button(text="choose folder path", command = slef.show_dirs)


        slef.content.grid(column=0, row=0)
        frame.grid(column=0, row=0)
        choose_path_btn.grid(column=0, row=0)

    def show_dirs(slef):
        slef.cur_dir=fd.askdirectory()
        li = Tkinter.Listbox(slef.content)
        for file_name in os.listdir(slef.cur_dir):
            if file_name.endswith('.txt'):
                li.insert('end', file_name)
        li.grid(row=1, column=1)

root = Tk()
gui = interface(root)
root.mainloop()