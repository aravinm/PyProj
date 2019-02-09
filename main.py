import os
import Books
import Countries
import LDcomp
from reader import profile
from matching import merge_dicts

#from __future__ import division


directory = './data/'
male_profiles, female_profiles = {},{}

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
            if 'Female' in profiledict['Gender'] or 'F' in profiledict['Gender'] or 'f' in profiledict['Gender']:
                female_profiles[filename]=profiledict
            elif 'Male' in profiledict['Gender'] or 'M' in profiledict['Gender'] or 'm' in profiledict['Gender']:
                male_profiles[filename]=profiledict
profiles =  merge_dicts(male_profiles, female_profiles)


print Books.best_match_for("1.txt", path=directory)
#To get a list of scores for all male and female score for likes and dislikes
#malefemaleLD = malefemaleLD(malescoreLD(male_profiles,female_profiles),femalescoreLD(male_profiles,femaleprofiles))
#Using text file to find top 3 likes dislike matches
print Countries.all_matches(male_profiles,female_profiles,True)
print Countries.best_match(profiles['8.txt'],male_profiles, n=100)
print LDcomp.all_matches(male_profiles,female_profiles,True)
print LDcomp.best_match(profiles['9.txt'], male_profiles, n=100)
