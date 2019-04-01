from fuzzyset import FuzzySet
import nltk
from nltk.corpus import stopwords


def concept_match(concept_list, text, sim_thresh=0.8):
    f_s = FuzzySet(concept_list)
    token_text = nltk.word_tokenize(text)
    # stop_w = set(stopwords.words("de"))
    # token_text = [item for item in token_text if item not in stop_w]
    recognized_concepts = []
    i = 0

    while i < len(token_text):
        # check for composites of largest size first then smaller up to single words
        for l in reversed(range(3)):
            token_slice = token_text[i:i + 1 + l]
            word_composition = " ".join(token_slice)
            sim, matched_word = f_s.get(word_composition, [(0.0, "")])[0]
            if sim >= sim_thresh:
                score = len(matched_word.split(" "))
                recognized_concepts.append((matched_word, score))
                i += 1 + l
                break
        else:
            i += 1
    return recognized_concepts

