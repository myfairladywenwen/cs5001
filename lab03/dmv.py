from random import randint
def main():
    EXPIRE_YEAR = 2021
    print("Welcome to the DMV (estimated wait time is 3 hours)")
    fullname = input("Please enter your first, middle, and last name:"+'\n')
    # generate the last_name and the first_and_middle_name
    name_break = fullname.rfind(' ')
    last_name = fullname[name_break+1:]
    first_and_middle_name = fullname[:name_break]

    #get date_of_birth and update to year to the expire year
    date_of_birth = input("Enter date of birth (MM/DD/YY): "+'\n')
    date_to_modify = date_of_birth[6:]
    expire_date = date_of_birth.replace(date_to_modify, str(EXPIRE_YEAR))

    #generate 7 digit random license num 
    license_num =''
    for count in range(0,7):
        num = str(randint(0,9))
        license_num += num
    print("-------------------------------------")
    print("Washington Driver License")
    print("DL " + license_num)
    print("LN " + last_name)
    print("FN " + first_and_middle_name)
    print("DOB " + date_of_birth)
    print("EXP " + expire_date)
    print("-------------------------------------")
main()
# another way to generate the last_name and the first_and_middle_name
# for idx in range (len(fullname)-1, -1, -1):
#     # from the last letter, that is index[len-1],traverse backward,
#     # to the first letter,that is index[0]
#     if fullname[idx] == ' ':
#         # since we are travesing backward,
#         # the first '' we encounter will be the break of last name
#         # in this way, we avoid the edge case of having 2 middle names
#         last_name = fullname[idx+1:]
#         break
# first_and_middle_name = fullname[: idx]

