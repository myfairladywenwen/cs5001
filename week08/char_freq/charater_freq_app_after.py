import sys
from character_freqs import CharFreqs


def main(filename):
    cf = CharFreqs()

    try:
        f = open(filename)
    except FileNotFoundError:
        print("Can't find", filename)
        return
    for line in f:
        cf.count_line(line)

    print("\nCharacter counts dictionary:")
    print(cf.char_counts)

    print("\nAnd as a sorted list:")
    print(cf.sorted_counts)

    print("\nChars frequency:")
    print(cf.char_freqs)
    print("\nSorted frequency:")
    print(cf.sorted_freq)


main(sys.argv[1])
