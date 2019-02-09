from collections import Counter

def matches(match_on):
    def wrapped(suitor, potential_partners,n=None):
        score = Counter()
        for key, partner in potential_partners.iteritems():
            score[key] = match_on(suitor, partner)
        return score.most_common(n)
    return wrapped


def all_matches(match_on):
    def wrapped(suitors, partners, symmetric=False):
        matches={}
        for key, suitor in suitors.iteritems():
            matches[key] = match_on(suitor, partners)
        if symmetric:
            matches.update(wrapped(partners, suitors, False))
            #run the function again with the input reversed to get a two way mapping
        return matches
    return wrapped


