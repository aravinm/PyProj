
#thinking on how to compare likes with dislikes
def best_match(male_profiles, female_profiles):
    similarLD = {}
    for x in male_profiles:
        femalescore = {}
        for y in female_profiles:
            maleprofile, femaleprofile = male_profiles[x], female_profiles[y]
            mlike, mdislike, flike, fdislike = \
                getLikes(maleprofile,"Likes"), \
                getLikes(maleprofile,"Dislikes"), \
                getLikes(femaleprofile,"Likes"), \
                getLikes(femaleprofile,"Dislikes")
            similarlikes, similardislikes, likedislike, dislikelike, totalem = \
                len(set(mlike) & set(flike)), \
                len(set(mdislike) & set(fdislike)), \
                len(set(mlike) & set(fdislike)), \
                len(set(mdislike) & set(flike)), \
                len(mlike) + len(mdislike)
            totalsim = similarlikes + similardislikes
            totaldif = likedislike + dislikelike
            finalscore = totalsim - totaldif
            percentage = 100 * totalsim / totalem
            fname,mname = femaleprofile['Name'], maleprofile['Name']
            femalescore[fname] = percentage
            similarLD[mname] = femalescore
    return similarLD

def getLikes(dict,key):
    profiledict = dict
    listoflikes = []
    listoflikes = profiledict[key].rstrip().split(',',)
    listoflikes = [x.replace(" ","") for x in listoflikes]
    return listoflikes


