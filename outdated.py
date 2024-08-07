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

month = input("Month: ")
index = months.index(month)
print(index + 1)

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

