class PrimeGenerator:
    def __init__(self, num):
        self.num = num

    def primes_to_max(self):
        '''get the prime numbers from 2 to a given number.
        None -> List'''

        comp_set = set()
        prime_list = []
        for x in range(2, self.num+1):
            if x not in comp_set:
                prime_list.append(x)
            for y in range(2*x, self.num + 1, x):
                comp_set.add(y)
        return prime_list
