import os
import analyser
from reader import profile


directory = './data/'
user_profiles={}

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
            user_profiles[filename]=profile(f)


print analyser.best_match_for("1.txt", path=directory)
print_profiles(user_profiles)