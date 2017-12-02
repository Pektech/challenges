from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY) as f:
        return f.read().splitlines()


def calc_word_value(letters):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(char.upper(), 0)for char in letters)



def max_word_value(words = load_words()):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    old_score = 0
    for line in words:
        score = calc_word_value(line)
        if score > old_score:
            max_word = line
            old_score = score
    return max_word


if __name__ == "__main__":
    pass # run unittests to validate
