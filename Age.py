import matching


def match(suitor, partner):
    score = 0
    if suitor['Age'] in partner['Acceptable_age_range']:
        score += 1
    if partner['Age'] in suitor['Acceptable_age_range']:
        score += 1
    return score


@matching.best_match
def best_match(suitor, potential_partners, n=3):
    return match(suitor, potential_partners)


@matching.all_matches
def all_matches(suitors, partners, symmetric=False):
    return best_match(suitors, partners)