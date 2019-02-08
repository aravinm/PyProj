#function to get likes, used in the below functions
def getLikes(dict):
    return [y.strip() for y in dict['Likes'].split(',',)]

#function to get dislikes, used in the below functions
def getDislikes(dict):
    return [y.strip() for y in dict['Dislikes'].split(',',)]


#function to get dictionary of scores for each male to all females
def malescoreLD(maleprof, femaleprof):
    similarLD = {}
    for x in maleprof:
        femalescore = {}
        for y in femaleprof:
            maleprofile, femaleprofile = male_profiles[x], female_profiles[y]
            mlike, mdislike, flike, fdislike = \
                   getLikes(maleprofile), \
                   getDislikes(maleprofile), \
                   getLikes(femaleprofile), \
                   getDislikes(femaleprofile)
            similarlikes, similardislikes, likedislike, dislikelike, totalm, totalf = \
                          len(set(mlike) & set(flike)), \
                          len(set(mdislike) & set(fdislike)), \
                          len(set(mlike) & set(fdislike)), \
                          len(set(mdislike) & set(flike)), \
                          len(mlike) + len(mdislike), \
                          len(flike) + len(fdislike)
            totalsim = similarlikes + similardislikes
            totaldif = likedislike + dislikelike
            score = totalsim - totaldif
            mpercentage = score / totalm * 100
            fpercentage = score / totalf * 100
            finalscore = round((mpercentage + fpercentage) / 2 ,2)
            
            if finalscore < 0 :
                finalscore = 0
                fname,mname = femaleprofile['Name'], maleprofile['Name']
                femalescore[fname] = float(finalscore)
                similarLD[mname] = femalescore
       
            else:
                fname,mname = femaleprofile['Name'], maleprofile['Name']
                femalescore[fname] = float(finalscore)
                similarLD[mname] = femalescore

    return similarLD

#function to get dictionary of scores for each female to all males
def femalescoreLD(maleprof, femaleprof):
    similarLD = {}
    for x in femaleprof:
        malescore = {}
        for y in maleprof:
            maleprofile, femaleprofile = male_profiles[y], female_profiles[x]
            mlike, mdislike, flike, fdislike = \
                   getLikes(maleprofile), \
                   getDislikes(maleprofile), \
                   getLikes(femaleprofile), \
                   getDislikes(femaleprofile)
            similarlikes, similardislikes, likedislike, dislikelike, totalm, totalf = \
                          len(set(mlike) & set(flike)), \
                          len(set(mdislike) & set(fdislike)), \
                          len(set(mlike) & set(fdislike)), \
                          len(set(mdislike) & set(flike)), \
                          len(mlike) + len(mdislike), \
                          len(flike) + len(fdislike)
            
            totalsim = similarlikes + similardislikes
            totaldif = likedislike + dislikelike
            score = totalsim - totaldif
            mpercentage = score / totalm * 100
            fpercentage = score / totalf * 100
            finalscore = round((mpercentage + fpercentage) / 2 ,2)
            
            if finalscore < 0 :
                finalscore = 0
                fname,mname = femaleprofile['Name'], maleprofile['Name']
                malescore[mname] = float(finalscore)
                similarLD[fname] = malescore
       
            else:
                fname,mname = femaleprofile['Name'], maleprofile['Name']
                malescore[mname] = float(finalscore)
                similarLD[fname] = malescore

    return similarLD

#Function to get a dictionary of scores for each male female. 2 variable called should be the other 2 functions malescoreLD and femalescoreLD
def malefemaleLD(maledict,femaledict):
    z = maledict.copy()
    z.update(femaledict)
    return z
    
#comparing a user(filename) to all the other genders and print the top 3 matches. 2 variabled called should be filename and directory
def LDMatch(suitor, potential_partners, n=3):
    scorelist = {}
    for id in potential_partners:
        partner = potential_partners[id]
        mlike, mdislike, flike, fdislike = \
               getLikes(partner), \
               getDislikes(partner), \
               getLikes(suitor), \
               getDislikes(suitor)
        similarlikes, similardislikes, likedislike, dislikelike, totalm, totalf = \
                      len(set(mlike) & set(flike)), \
                      len(set(mdislike) & set(fdislike)), \
                      len(set(mlike) & set(fdislike)), \
                      len(set(mdislike) & set(flike)), \
                      len(mlike) + len(mdislike), \
                      len(flike) + len(fdislike)
        totalsim = similarlikes + similardislikes
        totaldif = likedislike + dislikelike
        score = totalsim - totaldif
        mpercentage = score / totalm * 100
        fpercentage = score / totalf * 100
        finalscore = round((mpercentage + fpercentage) / 2 ,2)
        if finalscore < 0 :
            finalscore = 0
            fname,mname = suitor['Name'], partner['Name']
            pairname = mname.strip() + "+" + fname.strip()
            scorelist[pairname] = float(finalscore)
        else:
            fname,mname = suitor['Name'], partner['Name']
            pairname = mname.strip() + "+" + fname.strip()
            scorelist[pairname] = float(finalscore)

    return sorted(scorelist.items(), key=lambda x: x[1], reverse=True)[:n]