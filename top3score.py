def country_reader(x,y):
    d ={'Michael Jackson':{'Carol':1,'karen':2},'Kevin':{'Carol':2}}
    score = d[x][y]
    return score


def age_reader(x,y):
    a ={'Michael Jackson':{'Carol':1,'karen':2},'Kevin':{'Carol':2}}
    ascore = a[x][y]
    return ascore


def final_score(a,b,c,d):
    final = a * b * c * d
    return final


# Temporary input
guyName = raw_input("Please input guy name")
girlName = raw_input("Girl Name")
# End of temporary input

countryMultiplier = 1.0
cMatchscore = country_reader(guyName, girlName)
aMatchscore = age_reader(guyName, girlName)

if cMatchscore == 0:
    countryMultiplier = 0.0
elif cMatchscore == 1:
    countryMultiplier = 0.5

ageMultiplier = 1.0

if aMatchscore == 0:
    ageMultiplier = 0.0
elif aMatchscore == 1:
    ageMultiplier = 0.5

# Calculate final score. Country score x Age score x Shared Interest Score x likes & dislikes.
# To change shared interest score and likes and dislikes to their respective names
finalFDict = {}
# for i in femaleDictionary:
for i in girlName:
    # Insert sharedinterestscore here
    sharedinterestscore = 10
    # Insert likesdislikescore here
    likesdislikescore = 10
    finalScore = final_score(countryMultiplier, ageMultiplier, sharedinterestscore, likesdislikescore)
    finalFDict[girlName] = finalScore

# Add function to sort top 3

print finalFDict




