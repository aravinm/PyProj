import Tkinter as tk
import ttk
import tkFileDialog as fd

import os

import reader

class Interface:
    def __init__(self, root):
        self.cur_dir = tk.StringVar()
        self.displayed_profile_text = tk.StringVar()

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.content = ttk.Frame(root)
        self.content.grid(column=0, row=0)

        self.notebook = ttk.Notebook(self.content)

        self.dir_page = ttk.Frame(self.notebook)
        self.cur_dir_label = ttk.LabelFrame(
            self.dir_page,
            text='current folder:'
            )
        self.cur_dir_value = ttk.Label(
            self.dir_page,
            textvariable = self.cur_dir
        )
        self.choose_path_btn = ttk.Button(
            self.dir_page,
            text="choose folder path",
            command = self.set_cur_dir
           )
        self.cur_dir_label.grid(column=0, row=0)
        self.cur_dir_value.grid(column=0, row=0)
        self.choose_path_btn.grid(column=1, row=0)

        self.profile_page = ttk.Frame(self.notebook)
        self.li = tk.Listbox(self.profile_page)
        self.li.bind("<<ListboxSelect>>", self.update_displayed_profile)
        self.displayed_profile = tk.Label(
            self.profile_page,
            textvariable = self.displayed_profile_text
            )
        self.show_all_profile_btn=ttk.Button(
            self.profile_page,
            text='show all profile',
            command = self.show_all_profiles
           )
        self.li.grid(column=0, row=0)
        self.displayed_profile.grid(column=1, row=0)
        self.show_all_profile_btn.grid(column=0, row=2)


        self.notebook.grid(column=0, row=0)
        self.notebook.add(self.dir_page, text='folder')
        self.notebook.add(self.profile_page, text='profile')

    def update_displayed_profile(self, event):
        cur_selected_profile = reader.read_txt(
            name=self.li.get(self.li.curselection()),
            directory = self.cur_dir.get()
            )
        self.displayed_profile_text.set(cur_selected_profile)


    def show_all_profiles(self):
        profiles =[self.cur_dir.get()+f for f in self.li.get(0, 'end')]
        all_profiles_text=reader.read_all_from(profiles)

        all_profile_window = tk.Toplevel()
        all_profile_window.wm_title("all profiles")
        all_profiles_textbox = tk.Text(all_profile_window)
        all_profiles_textbox.insert(1.0, all_profiles_text)
        all_profiles_textbox.configure(state='disabled')
        all_profiles_textbox.pack()


    def set_cur_dir(self):
        self.cur_dir.set(fd.askdirectory()+'/')
        self.update_file_list()

    def update_file_list(self):
        self.li.delete(0,'end')
        if os.path.isdir(self.cur_dir.get()):
            for file_name in os.listdir(self.cur_dir.get()):
                if  file_name.endswith('.txt'):
                    self.li.insert('end', file_name)



rt = tk.Tk()
gui = Interface(rt)
rt.mainloop()