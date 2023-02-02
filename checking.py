from transliterate import to_cyrillic, to_latin


def translit(message):
    msg = message
    to_cyrillic(msg)
    return to_cyrillic(msg)
print(translit('salom'))
