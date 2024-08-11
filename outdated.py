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

# The anno_domini comes in two formats: (1) Complete Month name-Space-Number-Comma-Space-Four digit Number and (2) Nomber-Slash-Number-Slash-four digit number

# The second number is between 1 and 31, No restrictions for the third number, the first number goes between 1 and 12

# Approach 1: Work on the format that doesn't have any strings and split the MM/DD/YYYY format to convert it into YYY-MM-DD format.  Make it work fine from the very get go...  Convert the format Month Day, Year into the format with slashes and take it from there.
anno_Domini = input("Date: ")

#https://www.geeksforgeeks.org/python-split-multiple-characters-from-string/

delimiters = [",", " ", "/"]
 
for delimiter in delimiters:
    anno_Domini = " ".join(anno_Domini.split(delimiter))
 
result = anno_Domini.split()
 
print(result)
print(result[0] in months)

try:
    if result[0] in months:
        result[0] = str(months.index(result[0]) + 1)
    elif type(int(result[0])) is int:
        pass

except ValueError:
    print("Call main function again")

if int(result[0]) > 12 or int(result[0]) < 1:
    print("Call main function again")
elif int(result[1]) > 31 or int(result[1]) < 1:
    print("Call main function again")
else:
    rearranged = [result[2], result[0], result[1]]
    print(rearranged)
