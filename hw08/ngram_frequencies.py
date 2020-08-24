class NgramFrequencies:
    def __init__(self, word_list, n):
        self.n = n
        self.word_list = word_list
        self.gram_count = {}
        self.total_count = 0

    def add_item(self):
        """put the n-gram into the dictionay, and count the total.
        None -> None"""
        for i in range(len(self.word_list) - self.n + 1):
            data = ''
            for j in range(i, i+self.n):
                data += (self.word_list[j] + "_")
            data_new = data[:-1]  # delete the final"_"
            self.total_count += 1
            if data_new in self.gram_count:
                self.gram_count[data_new] += 1
            else:
                self.gram_count[data_new] = 1

    def top_n_counts(self, n):
        sorted_counts_list = sorted(self.gram_count.items(),
                                    key=lambda x: x[1],
                                    reverse=True
                                    )
        return sorted_counts_list[:n]

    @property
    def word_freqs(self):
        return {key: round(self.gram_count[key]/self.total_count, 3)
                for key in self.gram_count.keys()}

    def top_n_freqs(self, n):
        sorted_freqs_list = sorted(self.word_freqs.items(),
                                   key=lambda x: x[1],
                                   reverse=True
                                   )
        return sorted_freqs_list[:n]

    def frequency(self, word):
        return round(self.gram_count[word] / self.total_count, 3)
