from uzwords import words
from difflib import get_close_matches

def checkWords(word,words=words):
    word=word.lower()
    matches =set(get_close_matches(word,words))
    available =False

    if word in matches:
        available=True
        matches=word
    return {'avalible':available,'matches':matches}

if __name__=='__main__':
    print(checkWords('апа'))
