lst = []

try:
    while True:
        item = input()
        lst.append(item)
except EOFError:
    pass
    print(lst)