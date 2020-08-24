import sys


def main(endpoint):
    print(tri(endpoint, 0, 0))

def tri(endpoint, startpoint, pre_trinumber):
    if startpoint == endpoint:
        return pre_trinumber
    else:
        startpoint += 1
        pre_trinumber = pre_trinumber + startpoint
        print(pre_trinumber)
        return tri(endpoint, startpoint, pre_trinumber)
# tail recursion: very last thing the func does 
# is recursively call itself
main(int(sys.argv[1]))