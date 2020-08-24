def insuff():
    print("Insufficient infomation to list possibilities.")


def test_achingBones():
    if input("Do you have aching bones or aching joints? ") == 'y':
        print("possibilities include viral infection.")
    elif input("Do you have a rash? ") == 'y':
        insuff()
    elif input("Do you have a sore throat? ") == 'y':
        print("possibilities include throat infection.")
    elif input("Do you have a back pain just above the waist with" +
               " chills and fever? ") == 'y':
        print("possibilities include kidney infection.")
    elif input("Do you have pain urinating or" +
               " are urinating more often? ") == 'y':
        print("possibilities include urinary tract infection.")
    elif input("Have you spent the day in the sun or" +
               " in hot conditions? ") == 'y':
        print("Possibilities sunstroke or heat exhaustion.")
    else:
        insuff()


def diagnose():
    print("This is a fever diagnosis system." +
          "  For all the questions, please enter 'y' to represent 'yes'" +
          " and 'no' to represent 'no'.")

    if input("Are you coughing? ") == "y":  # coughing
        if input("Are you short of breath" +
                 " or wheezing or coughing up phlegm? ") == 'y':
            print("possibilities include pneumonia or infection of airways.")
        elif input("Do you have a headache? ") == 'y':
                print("possibilities include viral infection.")
        else:  # cough +not headache
            test_achingBones()
    else:  # not coughing
        if input("Do you have a headache? ") == 'y':  # not cough but headache
            if input("Are you experiencing any of the folowing: " +
                     "pain when bending your head forward," +
                     " nausea or vomitting," +
                     " brighting light hurting your eyes," +
                     " drowsiness or confusion? ") == 'y':
                print("Possibilities include menigitis.")
            elif input("Are you vomitting or had diarrhea? ") == 'y':
                print("Possibilities include digestive infection.")
            else:
                test_achingBones()
        else:  # not cough not headache
            test_achingBones()


def main():
    diagnose()


main()
