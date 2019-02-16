import Tkinter as tk
import ttk
import tkFileDialog as fd

import os,csv

import reader
import Age,Books,Countries,Likes,Overall
from utils import ignored
from textwrap import dedent


class Interface:
    def __init__(self, root):
        root.resizable(False,False)

        self.cur_dir = tk.StringVar()
        self.cur_user = tk.StringVar()
        self.cur_usr_name = tk.StringVar()
        self.displayed_profile_text = tk.StringVar()
        self.filter_by_country = tk.BooleanVar(value=True)
        self.filter_by_age = tk.BooleanVar(value=True)
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
            textvariable=self.cur_usr_name
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
        self.cur_dir_label.grid(column=0, row=0)
        self.cur_dir_value.grid(column=0, row=0)
        self.choose_path_btn.grid(column=1, row=0)

        self.profile_page = ttk.Frame(self.notebook)
        self.li = tk.Listbox(self.profile_page, height=16)
        self.li.bind("<<ListboxSelect>>", self.update_displayed_profile)
        self.displayed_profile = tk.Label(
            self.profile_page,
            textvariable = self.displayed_profile_text,
            height = 17,
            width = 50,
            anchor='nw',
            justify='left'
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
            command=self.update_matches
        )
        self.filter_by_age_check = tk.Checkbutton(
            self.match_page,
            text="filter by age",
            variable=self.filter_by_age,
            command=self.update_matches
        )

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

        self.new_prof_page = ttk.Frame(self.notebook)
        self.name = tk.StringVar()
        self.gender = tk.StringVar(value='Male')
        self.country = tk.StringVar()
        self.acceptable_country = tk.StringVar()
        self.likes = tk.StringVar()
        self.dislikes = tk.StringVar()
        self.book = tk.StringVar()
        self.acceptable_country_str = tk.StringVar()
        self.likes_str = tk.StringVar()
        self.dislikes_str = tk.StringVar()
        self.books_str = tk.StringVar()
        self.displayed_acceptable_country_frame =  ttk.LabelFrame(
            self.new_prof_page,
            text="Acceptable Countries:"
        )
        tk.Label(
            self.displayed_acceptable_country_frame,
            textvariable=self.acceptable_country_str
        ).grid()
        self.displayed_likes_frame =  ttk.LabelFrame(
            self.new_prof_page,
            text="Likes:"
        )
        tk.Label(
            self.displayed_likes_frame,
            textvariable=self.likes_str
        ).grid()
        self.displayed_dislikes_frame =  ttk.LabelFrame(
            self.new_prof_page,
            text="Dislikes:"
        )
        tk.Label(
            self.displayed_dislikes_frame,
            textvariable=self.dislikes_str
        ).grid()
        self.displayed_books_frame =  ttk.LabelFrame(
            self.new_prof_page,
            text="Books:"
        )
        tk.Label(
            self.displayed_books_frame,
            textvariable=self.books_str
        ).grid()
        self.profile_str = tk.StringVar()
        self.display_new_profile = tk.Label(
            self.new_prof_page,
            textvariable=self.profile_str
        )
        tk.Label(self.new_prof_page, text="Name").grid(row=1)
        tk.Label(self.new_prof_page, text="Gender").grid(row=2)
        tk.Label(self.new_prof_page, text="Country").grid(row=3)
        tk.Label(self.new_prof_page, text="Acceptable Country").grid(row=4)
        tk.Label(self.new_prof_page, text="Age").grid(row=5)
        tk.Label(self.new_prof_page, text="Acceptable Age Range").grid(row=6)
        tk.Label(self.new_prof_page, text="Likes").grid(row=7)
        tk.Label(self.new_prof_page, text="Dislikes").grid(row=8)
        tk.Label(self.new_prof_page, text="Books").grid(row=9)
        self.name_entry = tk.Entry(self.new_prof_page,
                                   width=31,
                                   textvariable=self.name
                                   )
        self.r_male = tk.Radiobutton(self.new_prof_page,
                                     text="Male",
                                     variable=self.gender,
                                     value="Male"
                                     )
        self.r_female = tk.Radiobutton(self.new_prof_page, text="Female", variable=self.gender, value="Female")
        self.country_entry = tk.Entry(self.new_prof_page, width=31, textvariable=self.country)
        self.acceptable_country_entry = tk.Entry(self.new_prof_page, width=31, textvariable=self.acceptable_country)
        self.age = tk.Spinbox(self.new_prof_page, from_=16, to=100, width=2)
        self.min_age = tk.Spinbox(self.new_prof_page, from_=16, to=100, width=2)
        self.max_age = tk.Spinbox(self.new_prof_page, from_=16, to=100, width=2)
        self.likes_entry = tk.Entry(self.new_prof_page, width=31, textvariable=self.likes)
        self.dislikes_entry = tk.Entry(self.new_prof_page, width=31, textvariable=self.dislikes)
        self.books_entry = tk.Entry(self.new_prof_page, width=31, textvariable=self.book)
        self.add_country_btn = tk.Button(self.new_prof_page, text="Add Acceptable Country", command=self.addacceptablecountry)
        self.add_like_btn = tk.Button(self.new_prof_page, text="Add A Like", command=self.addlikes)
        self.add_dislike_btn = tk.Button(self.new_prof_page, text="Add A Dislike", command=self.adddislikes)
        self.add_book_btn = tk.Button(self.new_prof_page, text="Add A Book", command=self.addbook)
        self.verify_btn = tk.Button(self.new_prof_page, text="Verify Profile", command=self.confirm)
        self.name_entry.grid(row=1, column=1, columnspan=2)
        self.r_male.grid(row=2, column=1)
        self.r_female.grid(row=2, column=2)
        self.country_entry.grid(row=3, column=1, columnspan=2)
        self.acceptable_country_entry.grid(row=4, column=1, columnspan=2)
        self.age.grid(row=5, column=1, columnspan=2)
        self.min_age.grid(row=6, column=1)
        self.max_age.grid(row=6, column=2)
        self.likes_entry.grid(row=7, column=1, columnspan=2)
        self.dislikes_entry.grid(row=8, column=1, columnspan=2)
        self.books_entry.grid(row=9, column=1, columnspan=2)
        self.add_country_btn.grid(row=4, column=3)
        self.add_like_btn.grid(row=7, column=3)
        self.add_dislike_btn.grid(row=8, column=3)
        self.add_book_btn.grid(row=9, column=3)
        self.verify_btn.grid(row=10, column=3)
        self.displayed_acceptable_country_frame.grid(row=1, column=4)
        self.displayed_likes_frame.grid(row=3, column=4)
        self.displayed_dislikes_frame.grid(row=5, column=4)
        self.displayed_books_frame.grid(row=7, column=4)
        self.confirm_btn = tk.Button(self.new_prof_page, text="Confirm", command=self.write_new_profile)
        self.cancel_btn = tk.Button(self.new_prof_page, text="Cancel", command=self.clear_new_profile_form)

        self.notebook.grid(column=0, row=1)
        self.notebook.add(self.dir_page, text='folders')
        self.notebook.add(self.profile_page, text='profiles')
        self.notebook.add(self.match_page, text='matches')
        self.notebook.add(self.all_matches_page, text='best match')
        self.notebook.add(self.new_prof_page, text='Create Profile')

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
        if self.male_profiles and self.female_profiles:
            self.best_match_label.grid(column=0, row=2, sticky='sw')
            self.likes_radio_btn.grid(column=0, row=3, sticky='sw')
            self.books_radio_btn.grid(column=0, row=4, sticky='sw')
            self.overall_radio_btn.grid(column=0, row=5, sticky='sw')
            self.csv_export_btn.grid(column=1, row=6, sticky='ne')
        else:
            self.best_match_label.grid_forget()
            self.likes_radio_btn.grid_forget()
            self.books_radio_btn.grid_forget()
            self.overall_radio_btn.grid_forget()
            self.csv_export_btn.grid_forget()

    def set_cur_user(self):
        usr = self.get_cur_selected_value()
        self.cur_user.set(usr)
        self.cur_usr_name.set(self.get_profile_name(usr))
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
            map(lambda m: self.match.set(''.join((criteria_name,m[0])),
                                         field,
                                         potential_partners[m[0]][field]
                                         ),
                matches
                )
        criteria_name = criteria.__name__
        if criteria_name in self.match.get_children(''):
            self.match.delete(criteria_name)
        map(lambda t: self.match.heading(t, text=t), self.match['columns'])
        self.match.insert('', 'end',criteria_name,
                          text=criteria_name, open=True
                          )
        matches = criteria.matches(cur_user, potential_partners).most_common()
        map(lambda m: self.match.insert(criteria_name,
                                        'end',
                                        ''.join((criteria_name,m[0])),
                                        text=m[0],
                                        ),
            matches
            )
        map(lambda m: self.match.set(''.join((criteria_name,m[0])),
                                     'Score',
                                     m[1]),
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

    def addacceptablecountry(self):
        self.acceptable_country_str.set(self.acceptable_country_str.get() + self.acceptable_country.get() + ",")
        self.acceptable_country_entry.delete(0, 'end')

    def addlikes(self):
        self.likes_str.set(self.likes_str.get() + self.likes.get() + ",")
        self.likes_entry.delete(0, 'end')

    def adddislikes(self):
        self.dislikes_str.set(self.dislikes_str.get() + self.dislikes.get() + ",")
        self.dislikes_entry.delete(0, 'end')

    def addbook(self):
        self.books_str.set(self.books_str.get() + self.book.get() + "\n")
        self.books_entry.delete(0, 'end')

    def confirm(self):
        self.verify_btn.grid_forget()
        new_profile_text=dedent(
            """\
            Name: {}
            Gender: {}
            Country: {}
            Acceptable_country: {}
            Age: {}
            Acceptable_age_range: {}-{}
            Likes: {}
            Dislikes: {}
            
            Books:
            {}
            """
        ).format(
            self.name.get(),
            self.gender.get(),
            self.country.get(),
            self.acceptable_country_str.get(),
            self.age.get(),
            self.min_age.get(),self.max_age.get(),
            self.likes_str.get(),
            self.dislikes_str.get(),
            self.books_str.get())

        self.profile_str.set(new_profile_text)
        self.display_new_profile.grid(row=10, columnspan=3)
        self.confirm_btn.grid(row=11, column=0)
        self.cancel_btn.grid(row=11, column=1)

    def write_new_profile(self):
        file_name = fd.asksaveasfilename(defaultextension=".txt",
            filetypes=(("text files","*.txt"),("all files","*.*")))
        if file_name:
            with open(file_name,"w+") as f:
                f.write(self.profile_str.get())
        self.clear_new_profile_form()
        self.verify_btn.grid(row=10, column=3)

    def clear_new_profile_form(self):
        self.name_entry.delete(0, 'end')
        self.country_entry.delete(0, 'end')
        self.acceptable_country_entry.delete(0, 'end')
        self.likes_entry.delete(0, 'end')
        self.dislikes_entry.delete(0, 'end')
        self.books_entry.delete(0, 'end')
        self.cancel_btn.grid_forget()
        self.confirm_btn.grid_forget()
        self.display_new_profile.grid_forget()
        self.verify_btn.grid(row=10, column=3)
rt = tk.Tk()
gui = Interface(rt)
rt.mainloop()
