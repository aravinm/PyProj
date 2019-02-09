import os
import Age,Books,Countries,LDcomp,overall
from reader import profile
from folderpathinput import folder_input


def print_profiles(profiles):
    field_names = ('Name', 'Gender', 'Country', 'Acceptable_country', 'Age', 'Acceptable_age_range', 'Likes', 'Dislikes')
    for user in profiles:
        print user
        for key in field_names:
            print key,profiles[user][key]
        for book in profiles[user]['Books']:
            print book
        print


def merge_dicts(x,y):
    z=x.copy()
    z.update(y)
    return z

directory = None
while directory is None:
    directory = folder_input()

male_profiles, female_profiles = {},{}
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        with open(directory + filename) as f:
            profiledict = profile(f)
            if 'Female' in profiledict['Gender'] or 'F' in profiledict['Gender'] or 'f' in profiledict['Gender']:
                female_profiles[filename]=profiledict
            elif 'Male' in profiledict['Gender'] or 'M' in profiledict['Gender'] or 'm' in profiledict['Gender']:
                male_profiles[filename]=profiledict
profiles =  merge_dicts(male_profiles, female_profiles)


print 'Books'
print Books.all_matches(male_profiles, female_profiles)
print Books.matches(profiles['8.txt'],male_profiles)
#To get a list of scores for all male and female score for likes and dislikes
#malefemaleLD = malefemaleLD(malescoreLD(male_profiles,female_profiles),femalescoreLD(male_profiles,femaleprofiles))
#Using text file to find top 3 likes dislike matches
print 'Countries'
print Countries.all_matches(male_profiles,female_profiles)
print Countries.matches(profiles['7.txt'],female_profiles)

print 'Age'
print Age.all_matches(male_profiles,female_profiles)
print Age.matches(profiles['7.txt'],female_profiles)

print 'likes'
print LDcomp.all_matches(male_profiles, female_profiles)
print LDcomp.matches(profiles['7.txt'],female_profiles)

print 'overall'
print overall.all_matches(male_profiles, female_profiles)
print overall.matches(profiles['7.txt'],female_profiles)

print
print 'best match'
print overall.best_match(male_profiles, female_profiles)
print overall.best_match(female_profiles, male_profiles)
print overall.best_match(male_profiles, female_profiles, n=None, symmetric=True)
print overall.best_match(male_profiles, female_profiles, symmetric=True)