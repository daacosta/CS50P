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

# month = input("Month: ")
# index = months.index(month)
# print(index + 1)

# The anno_domini comes in two formats: (1) Complete Month name-Space-Number-Comma-Space-Four digit Number and (2) Nomber-Slash-Number-Slash-four digit number

# The second number is between 1 and 31, No restrictions for the third number, the first number goes between 1 and 12

# Approach 1: Work on the format that doesn't have any strings and split the MM/DD/YYYY format to convert it into YYY-MM-DD format.  Make it work fine from the very get go...  Convert the format Month Day, Year into the format with slashes and take it from there.

anno_Domini = "September 8, 1636".split(",")
print(anno_Domini)
month_day = anno_Domini[0].split(" ")
month_day.append(anno_Domini[1].strip())

List_anno_Domini = []
List_anno_Domini.append(str(months.index(month_day[0])+1))
List_anno_Domini.append(month_day[1])
List_anno_Domini.append(month_day[2])

Formatted_as_numbers_only = "/".join(List_anno_Domini)

print(Formatted_as_numbers_only)

print(List_anno_Domini)
print(month_day)

