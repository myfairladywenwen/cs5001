from word_ladder import WordLadder


def test_make_ladder():
    english_words = load_words()
    wl = WordLadder('dog', 'puppy', english_words)
    word_ladder = wl.make_ladder()
    assert repr(word_ladder) == "dog" + "\t" + "cog" + "\t" + "cop" + "\t"\
                                + "copy" + "\t" + "coppy" + "\t"\
                                + "poppy" + "\t" + "puppy" + "\t"

    wl = WordLadder('sad', 'happy', english_words)
    word_ladder = wl.make_ladder()
    assert repr(word_ladder) == "sad" + "\t" + "gad" + "\t"\
                                + "gap" + "\t" + "gapy" + "\t"\
                                + "gappy" + "\t" + "happy" + "\t"

    wl = WordLadder('red', 'yellow', english_words)
    word_ladder = wl.make_ladder()
    assert repr(word_ladder) == "red" + "\t" + "bed" + "\t"\
                                + "bel" + "\t" + "bell" + "\t"\
                                + "bello" + "\t" + "bellow" + "\t"\
                                + "yellow" + "\t"

    wl = WordLadder('command', 'line', english_words)
    word_ladder = wl.make_ladder()
    assert repr(word_ladder) == "command" + "\t" + "commend" + "\t"\
                                + "compend" + "\t" + "comped" + "\t"\
                                + "coped" + "\t" + "loped" + "\t"\
                                + "lope" + "\t" + "lone" + "\t"\
                                + "line" + "\t"


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
