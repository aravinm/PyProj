import os
import Books
import Countries
import LDcomp
from reader import profile
#from __future__ import division


directory = './data/'
male_profiles, female_profiles = {},{}
profiles =  {'m':male_profiles, 'f':female_profiles}

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

print Books.best_match_for("1.txt", path=directory)
#To get a list of scores for all male and female score for likes and dislikes
#malefemaleLD = malefemaleLD(malescoreLD(male_profiles,female_profiles),femalescoreLD(male_profiles,femaleprofiles))
#Using text file to find top 3 likes dislike matches
print Countries.all_profile_country_match(male_profiles,female_profiles)
print LDcomp.LDMatch(profiles['m']['1.txt'], profiles['f'], n=100)
