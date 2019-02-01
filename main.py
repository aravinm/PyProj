import os
import analyser
from reader import profile


directory = './data/'
male_profiles={}
female_profiles={}

def print_profiles(profiles):
    field_names = ('Name', 'Gender', 'Country', 'Acceptable_country', 'Age', 'Acceptable_age_range', 'Likes', 'Dislikes')
    for user in profiles:
        print user
        for key in field_names:
            print key,profiles[user][key]
        for book in profiles[user]['Books']:
            print book
        print

for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(directory + filename) as f:
            profiledict = profile(f)
            for x in profiledict['Gender']:
                if x == 'Female' or x == 'F' or x == 'f':
                    female_profiles[filename]=profiledict
                elif x == "Male" or x == "M" or x == "m":
                    male_profiles[filename]=profiledict

print analyser.best_match_for("1.txt", path=directory)
print_profiles(user_profiles)
