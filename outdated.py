months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# The anno_domini comes in two formats: (1) Complete Month name-Space-Number-Comma-Space-Four digit Number and (2) Number-Slash-Number-Slash-four digit number

# The second number is between 1 and 31, No restrictions for the third number, the first number goes between 1 and 12

# I was able to split with multiple delimiters a string and then check for both formats if they are OK... Finally I created a list that does rearrange in the format [YYYY, M, D].

#It is alright because I was able limit the string entry to the formats allowed to be entered.  I just need to add a couple of things: check if len(result) is three and if it ain't ask for the user to enter another date
def main():
    anno_Domini = input("Date: ")
    date_list = (validator_rearranger(splitter(anno_Domini)))
    print(date_list)

#https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/

def splitter(anno_Domini):
    delimiters = [",", " ", "/"]
    
    for delimiter in delimiters:
        anno_Domini = " ".join(anno_Domini.split(delimiter))
    
    result = anno_Domini.split()
    return result
    
    #print(result)
    #print(result[0] in months)

def validator_rearranger(result):

    if len(result) == 3:

        try:
            if result[0] in months:
                result[0] = str(months.index(result[0]) + 1)
            elif type(int(result[0])) is int:
                pass
            else:
                pass
                main()

        except ValueError:
            pass
            main()
        try:
            if int(result[0]) > 12 or int(result[0]) < 1:
                pass
                main()
            elif int(result[1]) > 31 or int(result[1]) < 1:
                pass
                main()
            else:
                rearranged = [result[2], result[0], result[1]]
                return rearranged
        except ValueError:
            pass
            main()
    else:
        pass
        main()
    


main()
