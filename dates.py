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

def main():
    valid_input = False
    while not valid_input:
        date = input("Date: ")
        if splitters_validator(date) and whole_validator(date):
            date_list = splitter(date)
            print(f"{rearrange_join(date)[0]}-{rearrange_join(date)[1].zfill(2)}-{rearrange_join(date)[2].zfill(2)}")
            valid_input = True

    # print(list_length_validator(date_list))
    # print(month_validator(date_list))
    # print(day_validator(date_list))
    # print(year_validator(date_list))
    # print(whole_validator(date))

def splitters_validator(X):
    if [month for month in months if(month in X)] and X.count(",") == 1:
        return True
    elif not [month for month in months if(month in X)] and X.count("/") == 2:
        return True
    elif [month for month in months if(month in X)] and X.count("/") != 0:
        return False
    else:
        return False

def splitter(X):
    if splitters_validator(X):
        delimiters = [",", " ", "/"]
        
        for delimiter in delimiters:
            X_stringer = " ".join(X.split(delimiter))
        
        X_list = X_stringer.split()
        X_list[1] = X_list[1].replace(',', '')

        return X_list
    else:
        return False

def list_length_validator(X_list):
    try:
        return len(X_list) == 3
    except TypeError:
        return False

def month_validator(X_list):
    try:
        d = True
        if list_length_validator:
            if X_list[0] in months:
                d = True
            elif int(X_list[0]) in range(1,13):
                d = True
            else:
                d = False
        else:
            d = False
    except (ValueError, TypeError):
        d = False
    return d

def day_validator(X_list):
    try:
        X_list[1] = X_list[1].replace(',', '')
        return int(X_list[1]) <= 12 and int(X_list[1]) >= 1
    except (ValueError, IndexError, TypeError):
        return False

def year_validator(X_list):
    try:
        return isinstance(int(X_list[2]), int)
    except (ValueError, IndexError, TypeError):
        return False
    
def whole_validator(X):
    return splitters_validator(X) and (splitter(X) != False) and list_length_validator(splitter(X)) and month_validator(splitter(X)) and day_validator(splitter(X)) and year_validator(splitter(X))

def rearrange_join(X):
    if whole_validator:
        rearranged_list = [splitter(X)[2], splitter(X)[0], splitter(X)[1]]
    if rearranged_list[1] in months:
        rearranged_list[1] = str(months.index(rearranged_list[1]) + 1)
    else:
        pass

    return rearranged_list

main()