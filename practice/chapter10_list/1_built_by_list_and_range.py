from math import sqrt
def is_prime(value):
    if value == 2:
        return True
    if value < 2 or value % 2 == 0:
        return False
    trial_factor = 3
    root = sqrt(value)
    while trial_factor <= root:
        if value % trial_factor == 0:
            return False
        trial_factor += 2  #next potentail value, skip evens
    return True


def prime_seq(begin, end):
    for item in range(begin, end+1):
        if is_prime(item) == True:
            yield item


def main():
    primes = list(prime_seq(20, 50))
    print(primes)

if __name__=='__main__':
    main()
        