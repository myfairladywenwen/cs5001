from prime_generator import PrimeGenerator
import time


def main():
    num = int(input("enter an integer and you will get all the prime numbers" +
                    "from 2 to that integer: "))
    start = time.perf_counter()
    list_of_primes = PrimeGenerator(num).primes_to_max()
    end = time.perf_counter()
    time_cost = end - start
    print(list_of_primes)
    print("time cost is", time_cost)


main()
