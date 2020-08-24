from text_cleaner import TextCleaner
import sys


filename = sys.argv[2]
tc = TextCleaner(filename)


def test_deal_special_dot():
    assert tc.deal_special_dot("abcdmr.") == "abcdmr"
    assert tc.deal_special_dot("abcddr.abcd") == "abcddrabcd"


def test_deal_commna():
    assert tc.deal_comma("abc,de") == "abc COMMAde"


def test_deal_apostro():
    assert tc.deal_apostro("burton's") == "burtonAPOSs"


def test_split_sentence():
    assert tc.split_sentence("I am a girl. You are a boy.") == [
        "I am a girl", " You are a boy", ""]


def test_deal_punc():
    assert tc.deal_punc("A necro- philiac entertainment-for") == [
        "A", "necro-", "philiac", "entertainment-for"]


def test_deal_whole_text():
    sentence_list = ["IAPOSm a girl.", "dr. white is-not!"]
    assert tc.deal_whole_text(sentence_list) == [
        "I'm", "a", "girl", "dr", "white", "isnot"
    ]
