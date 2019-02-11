import matching

'''This module includes the functions to calculate the compability score between two profiles.'''


def match(suitor, partner):
    """This function compares the number of similar likes and dislikes with the number of different like/dislikes and dislike/likes.
       The score is calculated by the sum of total similarities (similar likes and dislikes) minus the differences of each profile's
       likes and dislikes divided by total elements * 100 to get a percentage. The percentage for both profiles is then divded by 
       2 to get the average score. This function returns the score (rounded to 2 decimal place) of the compatability of the 2 profiles       
    """
        
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
@matching.matches
def matches(suitor, potential_partners):
    return match(suitor, potential_partners)

@matching.all_matches
def all_matches(suitors, partners,symmetric=False):
    return matches(suitors, partners)
