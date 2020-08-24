from ngram_frequencies import NgramFrequencies
from text_cleaner import TextCleaner
import sys

UNI_COUNT = 1
BI_COUNT = 2
TRI_COUNT = 3


def main(filename):
    tc = TextCleaner(filename)
    word_list = tc.do_the_cleaning()
    ng_uni = NgramFrequencies(word_list, UNI_COUNT)
    ng_bi = NgramFrequencies(word_list, BI_COUNT)
    ng_tri = NgramFrequencies(word_list, TRI_COUNT)
    ng_uni.add_item()
    ng_bi.add_item()
    ng_tri.add_item()

    print('Top 10 unigrams:')
    print_output_ngram(ng_uni.top_n_freqs(10))
    print('Top 10 bigrams:')
    print_output_ngram(ng_bi.top_n_freqs(10))
    print('Top 10 trigrams:')
    print_output_ngram(ng_tri.top_n_freqs(10))


def print_output_ngram(collection):
    for item in collection:
        print(item)


main(sys.argv[1])
