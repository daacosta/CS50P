import string

Alphabetlist = [chr(i) for  i in range(97, 123)]
Alphabet_lower = "".join(Alphabetlist)
Alphabet_upper = Alphabet_lower.upper()
Alphabet_complete = Alphabet_lower + Alphabet_upper
Alphabet = set(Alphabet_complete)
Numbers = str(set([x for x in range(0, 10)]))
Punctuation = string.punctuation
Punctuation_set = set([ x for x in Punctuation])

plate = input("Plate: ")

def plate_length(s):
    d = True
    if len(s) < 2:
        d = False
    elif len(s) > 6:
        d = False
    else:
        d = True
    return d

def first_two_characters(s):
    d = True
    if plate_length(s):
        if s[0] in Alphabet and s[1] in Alphabet:
            d = True
        else:
            d = False
    else:
        d = False
    return d
    
def no_punctuation_symbols(s):
    d = True
    if plate_length(s) and first_two_characters(s):
        if any(x in Punctuation_set for x in s):
            d = False
        else:
            d = True
    else:
        d = False
    return d
    
def count_digits(s):
    if no_punctuation_symbols(s):
        alpha = 0
        for i in s:
            if (i in Alphabet):
                alpha+=1
        digits = len(s)-alpha
        return digits
    else:
        return -1
        
def first_digit_not_zero(s):
    if count_digits(s) != -1:
        first_digit_position = len(s) - count_digits(s)
        if s[first_digit_position] == "0":
            d = False
        else:
            d = True
    else:
        d = False
    return d

#I need to verify that all digits are together starting from the very last index (-1).
#So, I need to use the number of digits to have the indexes of i from -1 to -digits-1
#changing by -1 every time... This is cool...

def digits_in_last_places_continuous(s):
    if first_digit_not_zero(s):
        for i in range(-1, -count_digits(s)-1, -1):
            if s[i] in Numbers:
                d = True
            else:
                d = False
                break
            d = False
    else:
        d = False
    return d
    
print("Plate length between 2 and 6 characters?", plate_length(plate))
print("First two characters are letters?", first_two_characters(plate))
print("No punctuation symbols?", no_punctuation_symbols(plate))
print("How many digits are in the plate?", count_digits(plate))
print("String's length is:", len(plate))
print("The first digit is not a zero?", first_digit_not_zero(plate))
print("All digits correctly placed?", digits_in_last_places_continuous(plate))