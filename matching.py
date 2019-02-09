from collections import Counter

def matches(match_on):
    def wrapped(suitor, potential_partners):
        score = Counter()
        for key, partner in potential_partners.iteritems():
            score[key] = match_on(suitor, partner)
        return score
    return wrapped


def all_matches(match_on):
    def wrapped(suitors, partners, symmetric=False):
        scores={}
        for key, suitor in suitors.iteritems():
            scores[key] = match_on(suitor, partners)
        if symmetric:
            scores.update(wrapped(partners, suitors, False))
            #run the function again with the input reversed to get a two way mapping
        return scores
    return wrapped


def best_match(function):
    def wrapped(suitors, partners, n=3, symmetric=False):
        scores = function(suitors, partners, symmetric)
        best_matches = Counter()
        for  suitor in scores.itervalues():
            key, value = suitor.most_common(1)[0]
            #counter.most_common return a list so a [0] is needed to get the tuple out of the list
            best_matches[key] += value
        return best_matches.most_common(n)
    return wrapped
