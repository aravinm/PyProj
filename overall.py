import Age,Books,Countries,LDcomp
import matching


def match(suitor, partner, criteria=(Age,Books,Countries,LDcomp)):
    score = 1
    for criterion in criteria:
        # Calculate final score. Country score x Age score x Shared Interest Score x likes & dislikes.
        # To change shared interest score and likes and dislikes to their respective names
        score*=criterion[suitor][partner]
    return score


@matching.matches
def matches(suitor, potential_partners):
    return match(suitor, potential_partners)


@matching.all_matches
def all_matches(suitors, partners, symmetric=False):
    return best_match(suitors, partners)