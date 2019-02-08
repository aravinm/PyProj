def symmetric(operator = lambda x,y: x+y):
    def combined(function):
        def wrapped(a,b):
            return operator(function(a,b),function(b,a))
        return wrapped
    return combined

def match(suitor, partner):
    if suitor['Country'] in partner['Acceptable_country']:
        return 1
    else:
        return 0


@symmetric()
def symmetric_match(suitor, partner):
    return match(suitor,partner)


def best_match(suitor, partners):
    return dict(
        (partner['Name'],symmetric_match(suitor,partner))
        for partner in partners.itervalues()
        )


def merge_dicts(x,y):
    z=x.copy()
    z.update(y)
    return z


@symmetric(operator=merge_dicts)
def all_matches(suitors,partners):
    return dict(
        (suitor['Name'],best_match(suitor,partners))
        for suitor in suitors.itervalues()
        )


