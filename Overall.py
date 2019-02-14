import Age,Books,Countries,Likes
import matching


def match(suitor, partner, criteria=(Age, Books, Countries, Likes)):
    score = 1
    for criterion in criteria:
        # Calculate final score. Country score x Age score x Shared Interest Score x likes & dislikes.
        # To change shared interest score and likes and dislikes to their respective names
        score*=criterion.match(suitor, partner)
    return round(score,2)


@matching.matches
def matches(suitor, potential_partners):
    return match(suitor, potential_partners)


@matching.all_matches
def all_matches(suitors, partners, symmetric=False):
    return matches(suitors, partners)

@matching.best_match
def best_match(suitors, partners, symmetric=False):
    return all_matches(suitors, partners, symmetric)
