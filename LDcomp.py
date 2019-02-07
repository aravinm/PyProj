#function to get likes, used in the below functions
def getLikes(dict):
    profiledict = dict
    listoflikes = []
    listoflikes = profiledict['Likes'].rstrip().split(',',)
    for x, y in enumerate(listoflikes):
        listoflikes[x] = y.replace(" ", "")
    return listoflikes

#function to get dislikes, used in the below functions
def getDislikes(dict):
    profiledict = dict
    listoflikes = []
    listoflikes = profiledict['Dislikes'].rstrip().split(',',)
    for x, y in enumerate(listoflikes):
        listoflikes[x] = y.replace(" ", "")
    return listoflikes

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
def LDMatch(filename,directory):
    scorelist = {}
    with open(directory + filename) as f:
        profiledict = profile(f)
        if 'Female' in profiledict['Gender'] or 'F' in profiledict['Gender'] or 'f' in profiledict['Gender']:
            malescore = {}
            for x in male_profiles:
                maleprofile, femaleprofile = male_profiles[x], profiledict
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
                    pairname = mname.strip() + "+" + fname.strip()
                    scorelist[pairname] = float(finalscore)         
                else:
                    fname,mname = femaleprofile['Name'], maleprofile['Name']
                    pairname = mname.strip() + "+" + fname.strip()
                    scorelist[pairname] = float(finalscore)
                   
        elif 'Male' in profiledict['Gender'] or 'M' in profiledict['Gender'] or 'm' in profiledict['Gender']:
            femalescore = {}
            for x in female_profiles:
                maleprofile, femaleprofile = profiledict, female_profiles[x]
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
                    pairname = mname.strip() + "+" + fname.strip()
                    scorelist[pairname] = float(finalscore)
                    
                else:
                    fname,mname = femaleprofile['Name'], maleprofile['Name']
                    pairname = mname.strip() + "+" + fname.strip()
                    scorelist[pairname] = float(finalscore)
    sortedscore = sorted(scorelist.items(), key=lambda x: x[1])
    firstmatch, secondmatch, thirdmatch = \
                sortedscore[len(sortedscore)-1],sortedscore[len(sortedscore)-2],sortedscore[len(sortedscore)-3]
    firstpair, secondpair,thirdpair = \
               str(firstmatch[0]).replace('+'," and "), \
               str(secondmatch[0]).replace('+'," and "), \
               str(thirdmatch[0]).replace('+'," and ")
    print "The top three matches for likes and dislikes with compatibility percentages are:"
    print firstpair,"%10s" %firstmatch[1]
    print secondpair,"%10s" %secondmatch[1]
    print thirdpair,"%10s" %thirdmatch[1]
