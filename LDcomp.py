def match(suitor, partner):
    p_likes,s_likes,p_dislikes,s_dislikes = \
        partner['Likes'], \
        suitor['Likes'], \
        partner['Dislikes'], \
        suitor['Dislikes']
    totalsim = len(p_likes & s_likes | p_dislikes & s_dislikes)
    totaldif = len(p_likes & s_dislikes | s_likes & p_dislikes)
    score = totalsim - totaldif
    totalm, totalf = \
        len(p_likes | p_dislikes), \
        len(s_likes | s_dislikes)
    mpercentage = score / totalm * 100
    fpercentage = score / totalf * 100
    finalscore = round((mpercentage + fpercentage) / 2, 2)
    if finalscore < 0:
        finalscore = 0
    return float(finalscore)
    
#comparing a user(filename) to all the other genders and print the top 3 matches. 2 variabled called should be filename and directory
def LDMatch(suitor, potential_partners, n=3):
    scorelist = {}
    for id in potential_partners:
        partner = potential_partners[id]
        pairname = suitor['Name'].strip() + "+" + partner['Name'].strip()
        scorelist[pairname] = match(suitor,partner)
    return sorted(scorelist.items(), key=lambda x: x[1], reverse=True)[:n]