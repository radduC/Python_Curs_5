def capitalize_string(string):
    return '. '.join(sentence.strip().capitalize() for sentence in string.split('.'))


def count_letters(string):
    return {letter: string.count(letter) for letter in string}


if __name__ == "__main__":
    print(capitalize_string('foaie verde. si-o lalea. ce faina-i butelca mea.'))
    print(count_letters('foaie verde. si-o lalea. ce faina-i butelca mea.'))
