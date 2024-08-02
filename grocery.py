list_raw = []

try:
    while True:
        item = input()
        list_raw.append(item)
except EOFError:
    pass

caps_list = []

for item in list_raw:
    item = item.upper()
    caps_list.append(item)

grocery_dict = {i:caps_list.count(i) for i in caps_list}

items_list = sorted(list(grocery_dict.keys()))

#print("\n")

for i in range(len(items_list)):
    print(grocery_dict.get(items_list[i]),items_list[i])