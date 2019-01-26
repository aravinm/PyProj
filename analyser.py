from reader import get_interests
from collections import Counter
import re

# todo import nltk word stemming?

"""
extracts meaningful words from the list of books then then count the frequency
"""


def sanitised(sentence):
    # return list of word in sentence after converting to lower case
    sentence = sentence.lower()
    sentence = re.sub('[^a-z ]', '', sentence)
    # remove not alphabetic characters
    sentence = sentence.strip().split()
    sentence = word_stems_of(sentence)
    return sentence


def word_stems_of(words):
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


def remove_stop_words_from(words):
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
    stop_words_removed = [word for word in words if word not in stop_words]
    return stop_words_removed


def shared_interest_of(user1, user2, interests_d):
    shared_interests = [interest for interest in interests_d[user1] if interest in interests_d[user2]]
    return shared_interests


def shared_interests_score(user1, user2, interests_d, return_data=False):
    # todo define metric for normalizing score
    if return_data:
        score = 0
        data = []
        for interest in shared_interest_of(user1, user2, interests_d):
            data.append((interest, interests_d[user1][interest], interests_d[user2][interest]))
            score += interests_d[user1][interest]+interests_d[user2][interest]
        data.sort(reverse=True, key=lambda s:s[2]+s[1])
        return score, data

    else:
        score = 0
        for interest in shared_interest_of(user1, user2, interests_d):
            score += interests_d[user1][interest]+interests_d[user2][interest]
        return score


def best_match(user, user_interest_d, n=3):
    matches = Counter()
    potential_partners = user_interest_d.keys()
    potential_partners.remove(user)
    for potential_partner in potential_partners:
        matches[user] = shared_interests_score(user, potential_partner, user_interest_d)
        matches[potential_partner] = shared_interests_score(user, potential_partner, user_interest_d)
    return matches.most_common(n)

def main():
    path="./data/"
    user_interests = get_interests("./data/profiles/")
    user_interest_count={}
    best_matches = {}
    for user in user_interests:
        interests = Counter()
        for title in user_interests[user]:
            title = sanitised(title)
            title = remove_stop_words_from(title)
            interests += Counter(title)
            user_interest_count[user] = interests
    for user in user_interest_count:
        best_matches[user] = best_match(user, user_interest_count)
        print "best matches for {0} are {1[0][0]}(score:{1[0][1]}), {1[1][0]}(score:{1[1][1]}), {1[2][0]}(score:{1[2][1]})" .format(user,best_matches[user])


if __name__ == '__main__':
    main()