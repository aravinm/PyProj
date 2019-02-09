import matching

def match(suitor, partner):
    p_likes,s_likes,p_dislikes,s_dislikes = \
        partner['Likes'], \
        suitor['Likes'], \
        partner['Dislikes'], \
        suitor['Dislikes']
    similarity = len((s_likes & p_likes) | (s_dislikes & p_dislikes))
    difference = len((s_likes & p_dislikes) | (s_dislikes & p_likes))
    score = float(similarity-difference)
    score = (score / len(s_likes | s_dislikes)
             + score / len(p_likes | p_dislikes))
    score *= 0.5 * 100
    if score < 0:
        score = 0
    return round(score,2)
    
#comparing a user(filename) to all the other genders and print the top 3 matches. 2 variabled called should be filename and directory
@matching.best_match
def best_match(suitor, partners, n=3):
    return match(suitor, partners)

@matching.all_matches
def all_matches(suitors, partners,symmetric=False):
    return best_match(suitors, partners)