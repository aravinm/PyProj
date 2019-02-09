def best_match(match_on):
    def wrapped(suitor, potential_partners, n=3):
        score_list = {}
        for partner in potential_partners.itervalues():
            score_list[partner["Name"]] = match_on(suitor,partner)
        return sorted(score_list.items(), key=lambda x: x[1], reverse=True)[:n]
    return wrapped

def all_matches(match_on):
    def wrapped(suitors, partners, symmetric=False):
        matches={}
        for suitor in suitors.itervalues():
            matches[suitor['Name']] = match_on(suitor, partners)
        if symmetric:
            matches.update(wrapped(partners, suitors, False))
            #run the function again with the input reversed to get a two way mapping
        return matches
    return wrapped


