from ngram_frequencies import NgramFrequencies


word_list = ['a', 'b', 'b', 'c', 'c', 'c']
ng1 = NgramFrequencies(word_list, 1)
ng2 = NgramFrequencies(word_list, 2)
ng3 = NgramFrequencies(word_list, 3)


def test_add_item():
    ng1.add_item()
    ng2.add_item()
    ng3.add_item()
    assert ng1.total_count == 6
    assert ng1.gram_count == {'a': 1, 'b': 2, 'c': 3}
    assert ng2.total_count == 5
    assert ng2.gram_count == {'a_b': 1, 'b_b': 1, 'b_c': 1, 'c_c': 2}
    assert ng3.total_count == 4
    assert ng3.gram_count == {'a_b_b': 1, 'b_b_c': 1, 'b_c_c': 1, 'c_c_c': 1}


def test_top_n_counts():
    assert ng1.top_n_counts(2) == [('c', 3), ('b', 2)]


def test_word_freqs():
    assert ng1.word_freqs == {'a': 0.167, 'b': 0.333, 'c': 0.5}


def test_top_n_freqs():
    assert ng1.top_n_freqs(2) == [('c', 0.5), ('b', 0.333)]


def test_frequency():
    assert ng1.frequency('a') == 0.167
