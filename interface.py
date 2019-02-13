import Tkinter as tk
import ttk
import tkFileDialog as fd

import os

import reader
import Age,Books,Countries,LDcomp,overall
from utils import ignored


class Interface:
    def __init__(self, root):
        root.resizable(False,False)

        self.cur_dir = tk.StringVar()
        self.cur_user = tk.StringVar()
        self.displayed_profile_text = tk.StringVar()
        self.male_profiles,self.female_profiles = None, None

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.content = ttk.Frame(root)
        self.content.grid()

        self.notebook = ttk.Notebook(self.content)

        self.cur_user_label = ttk.LabelFrame(
            self.content,
            text = 'Current user:'
        )
        self.cur_user_value = tk.Label(
            self.cur_user_label,
            textvariable=self.cur_user
        )
        self.cur_user_label.grid(column=0, row=0, sticky='w')
        self.cur_user_value.grid(column=0, row=0)

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
            command = self.set_cur_dir,
           )
        self.cur_dir_label.grid(column=0, row=0, )
        self.cur_dir_value.grid(column=0, row=0)
        self.choose_path_btn.grid(column=1, row=0)

        self.profile_page = ttk.Frame(self.notebook)
        self.li = tk.Listbox(self.profile_page, height=15)
        self.li.bind("<<ListboxSelect>>", self.update_displayed_profile)
        self.displayed_profile = tk.Label(
            self.profile_page,
            textvariable = self.displayed_profile_text
            )
        self.show_all_profile_btn=ttk.Button(
            self.profile_page,
            text='show all profiles',
            command = self.show_all_profiles
           )
        self.cur_user_btn=ttk.Button(
            self.profile_page,
            text = 'set current user',
            command = self.set_cur_user
            )
        self.cur_user_btn.grid(column=0, row=1)
        self.show_all_profile_btn.grid(column=0, row=2)
        self.disable_if_empty()

        self.match_page = ttk.Frame(self.notebook)
        self.match = ttk.Treeview(
            self.match_page,
            columns=('name', 'score')
        )

        self.notebook.grid(column=0, row=1)
        self.notebook.add(self.dir_page, text='folders')
        self.notebook.add(self.profile_page, text='profiles')
        self.notebook.add(self.match_page, text='best match')


    def get_cur_selected_value(self):
        with ignored(tk.TclError):
            return self.li.get(self.li.curselection())


    def disable_if_empty(self):
        if not self.li.get(0):
            self.li.grid_forget()
            self.show_all_profile_btn.configure(state='disabled')
            self.cur_user_btn.configure(state='disabled')
        else:
            self.show_all_profile_btn.configure(state='enabled')
            self.cur_user_btn.configure(state='enabled')
            self.li.grid(column=0, row=0)


    def update_displayed_profile(self, event):
        if self.li.get(0):
            cur_selected_profile = reader.read_txt(
                name = self.get_cur_selected_value(),
                directory = self.cur_dir.get()
                )
            self.displayed_profile_text.set(cur_selected_profile)
            if self.displayed_profile_text.get():
                self.displayed_profile.grid(column=1, row=0, sticky='n')
            else:
                self.displayed_profile.grid_forget()


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
        self.displayed_profile_text.set('')

    def set_cur_user(self):
        self.cur_user.set(self.get_cur_selected_value())
        self.update_profiles()
        self.show_match()


    def update_file_list(self):
        self.li.delete(0,'end')
        if os.path.isdir(self.cur_dir.get()):
            for file_name in os.listdir(self.cur_dir.get()):
                if  file_name.endswith('.txt'):
                    self.li.insert('end', file_name)
        self.disable_if_empty()


    def update_profiles(self):
        self.male_profiles, self.female_profiles =\
            reader.profiles_from(self.cur_dir.get())

    def get_user_profile(self, key):
        if key in self.female_profiles:
            return self.female_profiles[key]
        elif key in self.male_profiles:
            return self.male_profiles[key]
        else:
            return None

    def get_potential_partners(self, key):
        if key in self.female_profiles:
            return self.male_profiles
        elif key in self.male_profiles:
            return self.female_profiles
        else:
            return None


    def show_match(self):
        if 'ld' in self.match.get_children(''):
            self.match.delete('ld')
        map(lambda t: self.match.heading(t, text=t), self.match['columns'])
        self.match.insert('', 'end', 'ld', text='likes / dislikes')
        cur_user = self.get_user_profile(self.cur_user.get())
        potential_partners = self.get_potential_partners(self.cur_user.get())
        ld_matches = LDcomp.matches(cur_user, potential_partners)
        print ld_matches
        map(lambda m: self.match.insert('ld', 'end', 'ld'.join(m), text=m),
            ld_matches
            )
        map(lambda m: self.match.set('ld'.join(m),
                                     'score',
                                     ld_matches[m]),
            ld_matches
            )
        map(lambda m: self.match.set('ld'.join(m),
                                     'name',
                                     potential_partners[m]['Name']
                                    ),
            ld_matches
            )
        self.match.grid(column=0, row=1)


rt = tk.Tk()
gui = Interface(rt)
rt.mainloop()