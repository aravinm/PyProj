import matching


def match(suitor, partner, symmetric = True):
    score = 0
    if suitor['Age'] in partner['Acceptable_age_range'] and symmetric:
        score += 1
    if partner['Age'] in suitor['Acceptable_age_range']:
        score += 1
    return score


@matching.matches
def matches(suitor, potential_partners):
    return match(suitor, potential_partners, symmetric=False)


@matching.all_matches
def all_matches(suitors, partners, symmetric=False):
    return matches(suitors, partners)