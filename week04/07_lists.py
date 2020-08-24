band = ["Paul", "Pete", "John", "George", "Mickey"]  # literal list

print(band)
print(band[1])
band[1] = "Ringo"
print(band)

instruments = ["Bass", "Drums", "Vocals", "Giutar"]
instruments2 = ["B", "D", "V", "G"]

lineup = zip(range(10), "hellothere", band, instruments, instruments2)
print(lineup)  # py cannot print zip objects
print(list(zip(range(10), "hellothere", band, instruments, instruments2)))
print(list(lineup))

print(range(10))
print(list(range(10)))
print(list("hello, there"))

line_up = zip(band, instruments)
numbered_line_up = zip(range(10), line_up)
print(list(numbered_line_up))


for band_member in list(lineup):
    print ("band_member: ", band_member)
# not work 因为是 genrator，用完就没了

line_up = list(zip(band, instruments))
# numbered_line_up = list(zip(range(10), line_up))
for band_member in line_up:
    print ("band_member: ", band_member)


fruits = ["apple", "banana", "cranberry", "durian", "etrog", "fig",
            "guava", "honeydew"]
print(fruits[-1])
print(fruits[0:5])

first_letters = [fruit[0] for fruit in fruits]
print(first_letters)


string = "Hi there, I'm a string"
numbered_characters = [numbered_char for numbered_char
                        in zip(range(len(string)), string)]
print(numbered_characters)

even_numbered_chars = [((n_c[0])*2, n_c[1]) for
                        n_c in zip(range(len(string)), string)]
print(even_numbered_chars)


list_of_lists =[['a','b','c','d'], [1,2,3,4,5,"one","two"], ["apple","banana","cranberry"]]
print(len(list_of_lists))
print(list_of_lists[2])
print(list_of_lists[2][2])
print(list_of_lists[2][2][2])

print(band)
band.insert(2, "Jeff")
print(band)