import matching


def match(suitor, partner):
    score = 0
    if suitor['Country'] in partner['Acceptable_country']:
        score += 1
    if partner['Country'] in suitor['Acceptable_country']:
        score += 1
    return score


@matching.matches
def matches(suitor, potential_partners):
    return match(suitor, potential_partners)


@matching.all_matches
def all_matches(suitors, partners, symmetric=False):
    return matches(suitors, partners)



