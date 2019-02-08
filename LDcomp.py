def match(suitor, partner):
    p_likes,s_likes,p_dislikes,s_dislikes = \
        partner['Likes'], \
        suitor['Likes'], \
        partner['Dislikes'], \
        suitor['Dislikes']
    score = float(
            len(p_likes & s_likes | p_dislikes & s_dislikes)\
            +len(p_likes & s_dislikes | s_likes & p_dislikes)
            )
    p_percentage = score / len(p_likes | p_dislikes)
    s_percentage = score / len(s_likes | s_dislikes)
    final_score = round((p_percentage + s_percentage) / 0.02, 2)
    if final_score < 0:
        final_score = 0
    return float(final_score)
    
#comparing a user(filename) to all the other genders and print the top 3 matches. 2 variabled called should be filename and directory
def best_match(suitor, potential_partners, n=3):
    score_list = {}
    for key in potential_partners:
        partner = potential_partners[key]
        pair_name = suitor['Name'].strip() + "+" + partner['Name'].strip()
        score_list[pair_name] = match(suitor,partner)
    return sorted(score_list.items(), key=lambda x: x[1], reverse=True)[:n]