import re


class DataAnalysis:
    def __init__(self, file):
        try:
            self.f = open(file, "r")
        except FileNotFoundError:
            print("Can't find", file)
            return
        self.total_count = 0
        self.lang_count = {}
        self.domain_id_count = {}

    def read_data(self, file_name):
        column_list = self.f.readline().strip().split(',')
        lang_idx = column_list.index('language')
        domain_id_idx = column_list.index('email')
        for line in self.f:
            column_list = line.strip().split(',')
            language = column_list[lang_idx]
            self.add_lang(language)
            domain_id_list = re.findall(r'\.([\w]*)$',
                                        column_list[domain_id_idx])
            self.add_domain_id(domain_id_list[0])

    def add_lang(self, lang):
        self.total_count += 1
        if lang in self.lang_count:
            self.lang_count[lang] += 1
        else:
            self.lang_count[lang] = 1

    def add_domain_id(self, domain_id):
        if len(domain_id) == 2:
            if domain_id in self.domain_id_count:
                self.domain_id_count[domain_id] += 1
            else:
                self.domain_id_count[domain_id] = 1

    @property
    def lang_freqs(self):
        return {key: self.lang_count[key]/self.total_count
                for key in self.lang_count.keys()}

    def top_n_lang_freqs(self, n):
        sorted_lang_freqs = sorted(
            self.lang_freqs.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return sorted_lang_freqs[:n]

    @property
    def domain_id_freqs(self):
        return {key: self.domain_id_count[key]/self.total_count
                for key in self.domain_id_count.keys()}

    def top_n_country_tlds_freqs(self, n):
        sorted_domain_id_freqs_list = sorted(
            self.domain_id_freqs.items(),
            key=lambda x: x[1],
            reverse=True
        )
        return sorted_domain_id_freqs_list[:n]
