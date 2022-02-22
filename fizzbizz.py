#  Eine kleine Beispielaufgabe:

def main():
    for i in range(100):
        print(fizzbizz(i))


def fizzbizz(number: int):

    # Schreibe hier eine funktion, die eine Zahl als annimmt und als return Wert
    #  Fizz ausgibt, wenn die Zahl durch 3 teilbar ist.
    #  Bizz ausgibt, wenn die Zahl durch 5 teilbar ist.
    #  FizzBizz ausgibt, wenn die Zahl durch 3 und 5 Teilbar ist.
    #  Wenn nichts davon zutrifft gib die Zahl zu zurück

    if number % 3 == 0:
        if number % 5 == 0:
            return "FizzBizz"
        else:
            return "Fizz"
    if number % 5 == 0:
        return "Bizz"
    else:
        return number


if __name__ == "__main__":
    main()
