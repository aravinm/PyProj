from collections import Counter
import re
import matching

# todo import nltk word stemming?

"""
extracts meaningful words from the list of books then then count the frequency
"""


def word_stems(words):
    # tries to get base word so it can count plural,singulaer, noun,verb,etc forms as the same word
    # very crude and not perfect, will cut experiences to experienc, summation to summa , will not equate christianity to christian,etc
    word_stems = []
    suffixes = (('ious', 'ment'), ('ies', 'ing', 'ive',), ('ed', 'es', 'ly'),'s')
    for word in words:
        if len(word) > 3:
        # prvent the choping of short words like "red" to 'r'
            for i in range(-4, 0):
                if word[i:] in suffixes[i]:
                    word = word[:i]
                    break
        word_stems.append(word)
    return word_stems


def stop_words_removed(words):
    # removes words that are to be ignore when calculating similarity
    stop_words = ('a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't",
                  'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by',
                  "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't",
                  'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have',
                  "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him',
                  'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is',
                  "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself',
                  'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our',
                  'ourselves', 'ours', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's",
                  'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs',
                  'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're",
                  "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't",
                  'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's",
                  'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't",
                  'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself',
                  'yourselves')
    return [word for word in words if word not in stop_words]


def sanitised(sentence):
    # return list of word in sentence after converting to lower case
    sentence = sentence.lower()
    sentence = re.sub('[^a-z ]', '', sentence)
    # remove not alphabetic characters
    sentence = sentence.strip().split()
    sentence = stop_words_removed(sentence)
    sentence = word_stems(sentence)
    return sentence


def interests(sentences):
    interests_count = Counter()
    for sentence in sentences:
        interests_count += Counter(sanitised(sentence))
    return interests_count


def match(suitor, partner):
    s_interests,p_interests = interests(suitor['Books']),interests(partner['Books'])
    shared_interests = set(s_interests) & set(p_interests)
    score = 0
    for interest in shared_interests:
        score +=  s_interests[interest] + p_interests[interest]
    return score


@matching.matches
def matches(suitor, potential_partners):
    return match(suitor, potential_partners)


@matching.all_matches
def all_matches(suitors, partners, symmetric=False):
    return matches(suitors, partners)

@matching.best_match
def best_match(suitors, partners, symmetric=False):
    return all_matches(suitors, partners, symmetric)
