import string

Alphabetlist = [chr(i) for  i in range(97, 123)]
Alphabet_lower = "".join(Alphabetlist)
Alphabet_upper = Alphabet_lower.upper()
Alphabet_complete = Alphabet_lower + Alphabet_upper

Alphabet = set(Alphabet_complete)

print(Alphabet)

Numbers = set([x for x in range(0, 10)])

print(Numbers)

Punctuation = string.punctuation
Punctuation_set = set([ x for x in Punctuation])

print(Punctuation_set)


string = input("Plate: ")

d = True

if len(string) < 2 or len(string) > 6:
    d = False
elif string[0] not in Alphabet:
    d = False
elif string[1] not in Alphabet:
    d = False
elif string[2] == "0":
    d = False
elif string[2] in Alphabet and string[3] == "0":
    d = False
elif string[2] in Alphabet and string[3] in Alphabet and string[4] == "0":
    d = False
elif string[2] in Alphabet and string[3] in Alphabet and string[4] in Alphabet and string[5] == "0":
    d = False
elif any(x in Punctuation_set for x in string):
    d = False

print(d)