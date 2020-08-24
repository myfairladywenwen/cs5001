from character_freqs import CharFreqs


def test_constructor():
    char_freqs = CharFreqs()
    assert char_freqs.total_count == 0
    assert char_freqs.char_counts == {}


def test_count_line():
    char_freqs = CharFreqs()
    char_freqs.count_line("ab;A")
    assert char_freqs.char_counts['a'] == 2
    assert char_freqs.char_counts['b'] == 1
    assert ';' not in char_freqs.char_counts.keys()


def test_sorted_counts_property():
    char_freqs = CharFreqs()
    char_freqs.count_line("aba")
    assert char_freqs.sorted_counts[0][0] == 'a'
    assert char_freqs.sorted_counts[0][1] == 2
    assert len(char_freqs.sorted_counts) == 2


def test_char_freqs():
    char_freqs = CharFreqs()
    char_freqs.count_line("aba")
    assert char_freqs.char_freqs['a'] == round(2/3, 2)
