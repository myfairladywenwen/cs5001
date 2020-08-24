letters = input('enter 4 letters:')
count = 0
for i in letters:
    for j in letters:
        if j!=i:
            for k in letters:
                if k!= j and k!= i:
                    for l in letters:
                        if l!= k and l!= j and l!= i:
                            print(i+j+k+l)
                            count +=1
print('in all there are',count, 'permutations from',letters)