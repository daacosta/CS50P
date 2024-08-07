def main():
    current_time = input("What time is it? ")
    X = convert(current_time)
    if X >= 7 and X <= 8:
        print("breakfast time")
    elif X >= 12 and X <= 13:
        print("lunch time")
    elif X >= 18 and X <= 19:
        print("dinner time")
    else:
        pass

def convert(time):
    hours, minutes = time.split(":")
    float_time = int(hours) + int(minutes)/60
    return float_time


if __name__ == "__main__":
    main()

#print(convert("7:30"))