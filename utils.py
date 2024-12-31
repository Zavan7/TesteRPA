import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))
