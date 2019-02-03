import os

#below are temp to be transferred to main
directory = 'C:/Users/jacob/Desktop/Sampledata/'
male_profiles, female_profiles, similarLD = ({} for i in range(3))

def getLikes(dict):
    profiledict = dict
    listoflikes = []
    listoflikes = profiledict['Likes'].rstrip().split(',',)
    for x, y in enumerate(listoflikes):
        listoflikes[x] = y.replace(" ", "")
    return listoflikes

def getDislikes(dict):
    profiledict = dict
    listoflikes = []
    listoflikes = profiledict['Dislikes'].rstrip().split(',',)
    for x, y in enumerate(listoflikes):
        listoflikes[x] = y.replace(" ", "")
    return listoflikes

#thinking on how to compare likes with dislikes
for x in male_profiles:
    femalescore = {}
    for y in female_profiles:
        maleprofile, femaleprofile = male_profiles[x], female_profiles[y]
        mlike, mdislike, flike, fdislike = getLikes(maleprofile), getDislikes(maleprofile), getLikes(femaleprofile), getDislikes(femaleprofile)
        similarlikes, similardislikes, likedislike, dislikelike, totalem = len(set(mlike) & set(flike)), len(set(mdislike) & set(fdislike)), len(set(mlike) & set(fdislike)), len(set(mdislike) & set(flike)), len(mlike) + len(mdislike)
        totalsim = similarlikes + similardislikes
        totaldif = likedislike + dislikelike
        finalscore = totalsim - totaldif
        percentage = 100 * totalsim / totalem
        fname,mname = femaleprofile['Name'], maleprofile['Name']
        femalescore[fname] = percentage
        similarLD[mname] = femalescore
        
   
print similarLD
