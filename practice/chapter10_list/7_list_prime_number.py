MAX = 10
#initianlize a list of False*500
lst = [False] * 500
lst[0] = lst[1] = True

for i in range(2, MAX+1):  # check each number
    if not lst[i]:  # if it is a prime
        print(i, end ='')
    for j in range (2*i, MAX+1, i):  # mark out all the multiples of i
        lst[j] = True
print()


def primes_to_max1(self):
        original_list = [x for x in range(2, self.num + 1)]
        comp_set = set()
        prime_list = []
        for x in original_list:
            if x not in comp_set:
                prime_list += [x]
            # original_list.remove(x)

            for y in range(x, self.num+1, x):
                # if y in original_list:
                comp_set.add(y)
                # print(comp_set)
                    # original_list.remove(y)
        return prime_list


def primes_to_max2(self):
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
