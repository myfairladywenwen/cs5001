from word_ladder import WordLadder


def test_make_ladder():
    english_words = load_words()
    wl = WordLadder('cat', 'hat', english_words[len('cat')])
    word_ladder = wl.make_ladder()
    assert repr(word_ladder) == "cat" + "\t" + "hat" + "\t"

    wl = WordLadder('love', 'hate', english_words[len('love')])
    word_ladder = wl.make_ladder()
    assert repr(word_ladder) == "love" + "\t" + "hove" + "\t"\
                                + "have" + "\t" + "hate" + "\t"

    wl = WordLadder('earth', 'ocean', english_words[len('earth')])
    word_ladder = wl.make_ladder()
    assert repr(word_ladder) == "earth" + "\t" + "barth" + "\t"\
                                + "barih" + "\t" + "baris" + "\t"\
                                + "batis" + "\t" + "bitis" + "\t"\
                                + "aitis" + "\t" + "antis" + "\t"\
                                + "antas" + "\t" + "antal" + "\t"\
                                + "ontal" + "\t" + "octal" + "\t"\
                                + "octan" + "\t" + "ocean" + "\t"


def test_generate_alphe_list():
    english_words = load_words()
    wl = WordLadder('cat', 'hat', english_words[len('cat')])
    assert wl.generate_alphe_list() == ['a', 'b', 'c', 'd', 'e', 'f',
                                        'g', 'h', 'i', 'j', 'k', 'l',
                                        'm', 'n', 'o', 'p', 'q', 'r',
                                        's', 't', 'u', 'v', 'w', 'x',
                                        'y', 'z']


def load_words():
    """Load words from complete wordlist file"""
    valid_words = {}
    with open('words_alpha.txt') as word_file:
        for w in word_file.read().split():
            if len(w) in valid_words.keys():
                valid_words[len(w)].add(w)
            else:
                valid_words[len(w)] = {w}
    return valid_words
