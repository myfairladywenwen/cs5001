import re


class TextCleaner:
    def __init__(self, filename):
        try:
            self.f = open(filename, 'r')
        except FileNotFoundError:
            print("Can't open", filename, ".")
            return

    def do_the_cleaning(self):
        '''read the text and return the text as a list of word, with special
        punctuations dealt.
        None -> List'''
        string0 = self.f.read()
        string1 = self.deal_special_dot(string0).lower()
        string2 = self.deal_comma(string1)
        string3 = self.deal_apostro(string2)
        sentence_list = self.split_sentence(string3)
        new_list = self.deal_whole_text(sentence_list)
        return new_list

    def deal_special_dot(self, astring):
        new_string = astring.replace("mr.", "mr")
        new_string = new_string.replace("dr.", "dr")
        return new_string

    def deal_comma(self, astring):
        return astring.replace(",", " COMMA")
        # add a " " for further split

    def deal_apostro(self, astring):
        return astring.replace("'", "APOS")

    def split_sentence(self, astring):
        return astring.split('.')

    def deal_punc(self, astring):
        return re.findall(r'([\w-]+)', astring)
        # match all the words, if the word has a - in it ,trade it as one word

    def deal_whole_text(self, sentence_list):
        whole_text_word_list = []
        for sentence in sentence_list:
            whole_text_word_list += self.deal_punc(sentence)
        # put APOS back as "'"
        for idx in range(len(whole_text_word_list)):
            new_string = whole_text_word_list[idx].replace("APOS", "'")
            whole_text_word_list[idx] = new_string
        # delete '-' within word
        for idx in range(len(whole_text_word_list)):
            new_string = whole_text_word_list[idx].replace("-", "")
            whole_text_word_list[idx] = new_string
        return whole_text_word_list
