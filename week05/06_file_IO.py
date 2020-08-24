import sys


def main(files):
    try:
        out = open("result.txt", "w")
    except:
        print("I cannot open result.txt for writing")
    
    for filename in files:
        try:
            f = open(filename, "r")
        except:
            print("cannot open", filename)
            return

        # f.readline() 这样title这行就被读过了，下面title readline（）实质读的是author了

        title = f.readline().strip()
        # author = str.join(' ', f.readline().strip().split(' ')[1:])
        author = ' '.join(f.readline().strip().split(' ')[1:])
        line_count = 0
        for _ in f:
            line_count +=1
        
        out.write("Processed poem:\n")
        out.write("Title: " + title + "\n")
        out.write("Author: " + author +"\n")
        out.write("Lines: " + str(line_count) +"\n")


main(sys.argv[1:])