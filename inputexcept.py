Menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
    try:
        Total = 0
        while True:
            text = input('Item: ').lower().title()
            if Menu.get(text):
                Total = Total + Menu[text]
                print(f"Total: ${Total}")
                
    except EOFError:
        pass
    print("\n")
main()