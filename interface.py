import Tkinter as tk
import ttk
import tkFileDialog as fd

import os,csv

import reader
import Age,Books,Countries,Likes,Overall
from utils import ignored


class Interface:
    def __init__(self, root):
        root.resizable(False,False)

        self.cur_dir = tk.StringVar()
        self.cur_user = tk.StringVar()
        self.displayed_profile_text = tk.StringVar()
        self.filter_by_country = tk.BooleanVar()
        self.filter_by_country.set(True)
        self.filter_by_age = tk.BooleanVar()
        self.filter_by_age.set(True)
        self.criteria = tk.StringVar(None, 'Overall')
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
        self.li = tk.Listbox(self.profile_page, height=12)
        self.li.bind("<<ListboxSelect>>", self.update_displayed_profile)
        self.displayed_profile = tk.Label(
            self.profile_page,
            textvariable = self.displayed_profile_text
            )
        self.cur_user_btn=ttk.Button(
            self.profile_page,
            text = 'set current user',
            command = self.set_cur_user
            )
        self.cur_user_btn.grid(column=0, row=1)
        self.disable_if_empty()

        self.match_page = ttk.Frame(self.notebook)
        self.match = ttk.Treeview(
            self.match_page,
            columns=('Name', 'Country', 'Age', 'Score')
        )
        self.show_all_profile_btn=ttk.Button(
            self.match_page,
            text='show all profiles',
            command = self.show_all_profiles
           )
        self.filter_by_country_check = tk.Checkbutton(
            self.match_page,
            text="filter by country",
            variable=self.filter_by_country,
            command=self.update_matches)
        self.filter_by_age_check = tk.Checkbutton(
            self.match_page,
            text="filter by age",
            variable=self.filter_by_age,
            command=self.update_matches)

        self.all_matches_page = ttk.Frame(self.notebook)
        self.all_matches = ttk.Treeview(
            self.all_matches_page,
            columns=('Name', 'Country','Gender' , 'Age', 'Score'),
            show = 'headings'
        )
        self.best_match_label = tk.Label(self.all_matches_page,
                                         text = 'show best match based on:')
        self.likes_radio_btn = ttk.Radiobutton(self.all_matches_page,
            text='Likes',variable=self.criteria,value='Likes',
            command = self.update_all_matches
                                              )
        self.books_radio_btn = ttk.Radiobutton(self.all_matches_page,
            text='Books',variable=self.criteria,value='Books',
            command = self.update_all_matches
                                              )
        self.overall_radio_btn = ttk.Radiobutton(self.all_matches_page,
            text='Overall',variable=self.criteria,value='Overall',
            command = self.update_all_matches
                                                )
        self.csv_export_btn = tk.Button(self.all_matches_page
                                        ,text = 'export matches to csv'
                                        ,command=self.all_best_match_to_csv
                                        )
        self.best_match_label.grid(column=0, row=2, sticky='sw')
        self.likes_radio_btn.grid(column=0,row=3, sticky='sw')
        self.books_radio_btn.grid(column=0,row=4, sticky='sw')
        self.overall_radio_btn.grid(column=0,row=5, sticky='sw')
        self.csv_export_btn.grid(column=1,row=6, sticky='ne')

        self.notebook.grid(column=0, row=1)
        self.notebook.add(self.dir_page, text='folders')
        self.notebook.add(self.profile_page, text='profiles')
        self.notebook.add(self.match_page, text='matches')
        self.notebook.add(self.all_matches_page, text='best match')


    def get_cur_selected_value(self):
        with ignored(tk.TclError):
            return self.li.get(self.li.curselection())


    def disable_if_empty(self):
        if not self.li.get(0):
            self.li.grid_forget()
            self.cur_user_btn.configure(state='disabled')
        else:
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
        def set_fields(field, profiles_dict):
            map(lambda m: profiles.set(m,
                                       field,
                                       profiles_dict[m][field]
                                       ),
                profiles_dict
                )
        all_profile_window = tk.Toplevel()
        all_profile_window.resizable(False,False)
        profiles = ttk.Treeview(all_profile_window,
                                columns=("Name", "Gender",'Age'),
                                show="headings",
                                )
        map(lambda t: profiles.heading(t, text=t), profiles['columns'])
        map(lambda p: profiles.insert('', 'end', p, text=p),
            self.male_profiles
            )
        map(lambda p: profiles.insert('', 'end', p, text=p),
            self.female_profiles
            )
        map(lambda s: set_fields(s, self.male_profiles), profiles['columns'])
        map(lambda s: set_fields(s, self.female_profiles), profiles['columns'])
        profiles.pack()

    def set_cur_dir(self):
        self.cur_dir.set(fd.askdirectory()+'/')
        self.update_file_list()
        self.displayed_profile_text.set('')
        self.update_profiles()
        self.update_profile_page()
        self.update_trees()
        self.update_all_matches()


    @staticmethod
    def filter_profiles(condition, criteria,cur_user, potential_partners):
        if condition.get():
            return {
                k:v for (k,v) in potential_partners.iteritems()
                if criteria.match(cur_user,
                                   potential_partners[k],
                                   symmetric=False)>0
                }
        else:
            return potential_partners


    def update_matches(self):
        user = self.get_user_profile(self.cur_user.get())
        partners = self.get_potential_partners(self.cur_user.get())
        partners = self.filter_profiles(self.filter_by_country,
                                        Countries, user, partners
                                        )
        partners = self.filter_profiles(self.filter_by_age, Age, user, partners)
        map(lambda c: self.show_match(user, partners, c),
            (Books, Likes, Overall)
            )


    def update_all_matches(self):
        self.show_all_match(globals()[self.criteria.get()])


    def set_cur_user(self):
        usr_name = self.get_profile_name(self.get_cur_selected_value())
        self.cur_user.set(usr_name)
        self.update_profile_page()
        self.update_matches()


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


    def update_profile_page(self):
        if self.male_profiles and self.female_profiles:
            self.show_all_profile_btn.grid(column=0, row=2, stick='se')
            self.filter_by_age_check.grid(column=0, row=3, stick='sw')
            self.filter_by_country_check.grid(column=0, row=2, stick='sw')
        else:
            self.show_all_profile_btn.grid_forget()
            self.filter_by_age_check.grid_forget()
            self.filter_by_country_check.grid_forget()


    def update_trees(self):
        if self.male_profiles and self.female_profiles:
            self.match.grid(column=0, row=1)
            self.all_matches.grid(column=0, row=1)
        else:
            self.match.grid_forget()
            self.all_matches.grid_forget()


    def get_user_profile(self, key):
        if key in self.female_profiles:
            return self.female_profiles[key]
        elif key in self.male_profiles:
            return self.male_profiles[key]
        else:
            return None

    def get_profile_name(self, key):
        profiles = self.get_user_profile(key)
        if profiles:
            return profiles['Name']
        else:
            return None

    def get_potential_partners(self, key):
        if key in self.female_profiles:
            return self.male_profiles
        elif key in self.male_profiles:
            return self.female_profiles
        else:
            return None



    def show_match(self, cur_user, potential_partners, criteria):
        def set_field(field):
            map(lambda m: self.match.set(criteria_name.join(m),
                                         field,
                                         potential_partners[m][field]
                                         ),
                matches
                )
        criteria_name = criteria.__name__
        if criteria_name in self.match.get_children(''):
            self.match.delete(criteria_name)
        map(lambda t: self.match.heading(t, text=t), self.match['columns'])
        self.match.insert('', 'end', criteria_name, text=criteria_name)
        matches = criteria.matches(cur_user, potential_partners)
        map(lambda m: self.match.insert(criteria_name,
                                        'end',
                                        criteria_name.join(m),
                                        text=m),
            matches
            )
        map(lambda m: self.match.set(criteria_name.join(m),
                                     'Score',
                                     matches[m]),
            matches
            )
        map(set_field, ('Name','Country','Age'))
        self.match.grid(column=0, row=1)


    def show_all_match(self, criteria):
        def set_field(field):
            map(lambda m: self.all_matches.set(m,
                                         field,
                                         self.get_user_profile(m)[field]
                                         ),
                users
                )
        for child in self.all_matches.get_children(''):
            self.all_matches.delete(child)
        map(lambda t: self.all_matches.heading(t, text=t),
            self.all_matches['columns'])
        if self.male_profiles and self.female_profiles:
            matches = criteria.best_match(self.male_profiles,
                                          self.female_profiles,
                                          symmetric = True
                                          )
            users,scores = zip(*matches)
            map(lambda p: self.all_matches.insert('', 'end', p, text=p),
                users)
            map(set_field, ('Name', 'Country', 'Gender', 'Age'))
            map(lambda m: self.all_matches.set(m[0],'Score',m[1]),matches)
            self.all_matches.grid(column=0, row=1)


    @staticmethod
    def to_csv(name, data,title = '' , fields=''):
        with open(name, 'ab') as out:
            csv_out = csv.writer(out)
            csv_out.writerow(title)
            csv_out.writerow(fields)
            for row in data:
                csv_out.writerow(row)


    def criteria_best_match_to_csv(self,criteria,file_name):
        matches = criteria.best_match(self.female_profiles,
                                     self.male_profiles,
                                     n=None,
                                     symmetric=True
                                    )
        data = [(self.get_profile_name(f),''.join((self.cur_dir.get(),f)),s)
                for (f,s) in matches]
        self.to_csv(file_name,data,
                    title=[''.join(('Based on ',criteria.__name__))],
                    fields=('name','file','score')
                    )


    def all_best_match_to_csv(self):
        file_name = fd.asksaveasfilename(defaultextension=".csv",
            filetypes=(("csv files","*.csv"),("all files","*.*")))
        map(lambda d: self.criteria_best_match_to_csv(d, file_name=file_name),
            (Overall,Books,Likes)
            )

rt = tk.Tk()
gui = Interface(rt)
rt.mainloop()