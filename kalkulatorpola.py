print(f'Kalkulator pola')
print('Napisz:')
print('[1] - jeśli chcesz obliczyć pole kwadratu')
print('[2] - jeśli chcesz obliczyć pole prostokąta')
print('[3] - jeśli chcesz obliczyć pole rombu')
print('[4] - jeśli chcesz obliczyć pole równoległoboku')
print('[5] - jeśli chcesz obliczyć pole trójkąta')
print('[6] - jeśli chcesz obliczyć pole trapezu')
print('[7] - jeśli chcesz obliczyć pole koła')
print('—————————————————————————————')

wybór = int(input())

print('—————————————————————————————')
if wybór == 1:
    print('Wybrano kalkulator pola kwadratu')
    print('Wpisz jeden bok kwadratu (w cm):')
    bokkwadrat = float(input())
    polekwadrat = bokkwadrat * bokkwadrat
    print('——————————————')
    print(f'Pole tego kwadratu wynosi {polekwadrat} cm²')
    koniec = input()
elif wybór == 2:
    print('Wybrano kalkulator pola prostokąta')
    print('Wpisz pierwszy bok prostokąta (w cm):')
    bokprostokat1 = float(input())
    print('——————————————')
    print('Wpisz drugi bok prostokąta (w cm):')
    bokprostokat2 = float(input())
    print('——————————————')
    poleprostokat = bokprostokat1 * bokprostokat2
    print(f'Pole tego prostokąta wynosi {poleprostokat} cm²')
    koniec = input()
elif wybór == 3:
    print('Wybrano kalkulator pola rombu')
    print('!!! Pole rombu można obliczyć na dwa sposoby, wybierz jaki !!!')
    print('Napisz:')
    print('[1] - jeśli chcesz obliczyć pole na podstawie boku i wysokości')
    print('[2] - jeśli chcesz obliczyć pole na podstawie dwóch przekątnych')
    print('——————————————')
    wybór2 = int(input())
    print('——————————————')
    if wybór2 == 1:
        print('Wybrano obliczenie pola na podstawie boku i wysokości')
        bokromb = float(input('Wpisz bok rombu (w cm): '))
        print('——————————————')
        wysokoscromb = float(input('Wpisz wysokość rombu (w cm): '))
        poleromb1 = bokromb * wysokoscromb
        print('——————————————')
        print(f'Pole tego rombu wynosi {poleromb1} cm²')
        koniec = input()
    elif wybór2 == 2:
        print('Wybrano obliczenie pola na podstawie przekątnych')
        przekromb1 = float(input('Wpisz pierwszą przekątną rombu (w cm): '))
        print('——————————————')
        przekromb2 = float(input('Wpisz drugą przekątną rombu (w cm): '))
        poleromb2 = przekromb1 * przekromb2
        poleromb3 = poleromb2 / 2
        print('——————————————')
        print(f'Pole tego rombu wynosi {poleromb3} cm²')
        koniec = input()
    else:
        print('Podany zły wybór')
        koniec = input()
elif wybór == 4:
    print('Wybrano kalkulator pola równoległoboku')
    bokrownoleglobok = float(input('Wpisz bok równoległoboku (w cm): '))
    print('——————————————')
    wysokoscrownoleglobok = float(input('Wpisz wysokość równoległoboku (w cm): '))
    polerownoleglobok = bokrownoleglobok * wysokoscrownoleglobok
    print('——————————————')
    print(f'Pole tego równoległoboku wynosi {polerownoleglobok} cm²')
    koniec = input()
elif wybór == 5:
    print('Wybrano kalkulator pola trójkata')
    boktrojkat = float(input('Wpisz bok trójkąta (w cm): '))
    print('——————————————')
    wysokosctrojkat = float(input('Wpisz wysokość trójkąta (w cm): '))
    poletrojkat1 = boktrojkat * wysokosctrojkat
    poletrojkat2 = poletrojkat2 / 2
    print('——————————————')
    print(f'Pole tego trójkąta wynosi {poletrojkat2} cm²')
    koniec = input()
elif wybór == 6:
    print('Wybrano kalkulator pola trapezu')
    boktrapez1 = float(input('Wpisz pierwszy bok trapezu (w cm): '))
    print('——————————————')
    boktrapez2 = float(input('Wpisz drugi bok trapezu (w cm): '))
    print('——————————————')
    wysokosctrapez = float(input('Wpisz drugi wysokość trapezu (w cm): '))
    poletrapez1 = boktrapez1 + boktrapez2
    poletrapez2 = poletrapez1 * wysokosctrapez
    poletrapez3 = poletrapez2 / 2
    print('——————————————')
    print(f'Pole tego trapezu wynosi {poletrapez3} cm²')
    koniec = input()
elif wybór == 7:
    print('Wybrano kalkulator pola koła')
    promienkolo = float(input('Wpisz promień koła (w cm): '))
    polekolo1 = promienkolo * promienkolo
    polekolo2 = 3.14159265359 * polekolo1
    print('——————————————')
    print(f'Pole tego koła wynosi ok. {polekolo2} cm²')
    koniec = input()
else:
    print('Podano zły wybór')
    koniec = input()