import os
import Age,Books,Countries,Likes,Overall
from reader import profile
from folderpathinput import folder_input


# print 'Books'
# print Books.all_matches(male_profiles, female_profiles)
# print Books.matches(profiles['8.txt'],male_profiles)
# #To get a list of scores for all male and female score for likes and dislikes
# #malefemaleLD = malefemaleLD(malescoreLD(male_profiles,female_profiles),femalescoreLD(male_profiles,femaleprofiles))
# #Using text file to find top 3 likes dislike matches
# print 'Countries'
# print Countries.all_matches(male_profiles,female_profiles)
# print Countries.matches(profiles['7.txt'],female_profiles)
#
# print 'Age'
# print Age.all_matches(male_profiles,female_profiles)
# print Age.matches(profiles['7.txt'],female_profiles)
#
# print 'likes'
# print LDcomp.all_matches(male_profiles, female_profiles)
# print LDcomp.matches(profiles['7.txt'],female_profiles)
#
# print 'overall'
# print overall.all_matches(male_profiles, female_profiles)
# print overall.matches(profiles['7.txt'],female_profiles)
#
# print
# print 'best match'
# print overall.best_match(male_profiles, female_profiles)
# print overall.best_match(female_profiles, male_profiles)
# print overall.best_match(male_profiles, female_profiles, n=None, symmetric=True)
# print overall.best_match(male_profiles, female_profiles, symmetric=True)
#
#
# def writeCsv(data):
#     with open('tt.csv', 'ab') as csvfile:
#         spamwriter = csv.writer(csvfile,
#                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
#         spamwriter.writerow(data)
# tempList1=[]
# for index, i in enumerate(overall.best_match(male_profiles, female_profiles)):
#     # print overall.best_match(male_profiles, female_profiles)
#     print profiles[overall.best_match(male_profiles, female_profiles)[index][0]]["Name"]
#     tempList1.append(profiles[overall.best_match(male_profiles, female_profiles)[index][0]]["Name"])
# writeCsv(["Best Match for Male"])
#
# writeCsv(tempList1)
#
# tempList2=[]
# for index, i in enumerate(overall.best_match(female_profiles, male_profiles)):
#     print profiles[overall.best_match(female_profiles, male_profiles)[index][0]]["Name"]
#     tempList2.append(profiles[overall.best_match(female_profiles, male_profiles)[index][0]]["Name"])
# writeCsv(["Best Match for Female"])
# writeCsv(tempList2)
#
# tempList3=[]
# for index, i in enumerate(overall.best_match(male_profiles, female_profiles, n=None, symmetric=True)):
#     print profiles[overall.best_match(male_profiles, female_profiles, n=None, symmetric=True)[index][0]]["Name"]
#     tempList3.append(profiles[overall.best_match(male_profiles, female_profiles, n=None, symmetric=True)[index][0]]["Name"])
# writeCsv(["Best Match for Female & Male"])
# writeCsv(tempList3)
