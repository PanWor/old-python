# Kalkulator temperatur (Celsjusze, Kelwiny, Fahrenhaita)

print(f'Witaj w kalkulatorze temperatur')
print(f'Napisz:')
print(f'[CK] - jeśli chcesz obliczyć z Celsjuszy na Kelwiny')
print(f'[KC] - jeśli chcesz obliczyć z Kelwinów na Celsjusze')
print(f'[CF] - jeśli chcesz obliczyć z Celsjuszy na Fahrenhaita')
print(f'[FC] - jeśli chcesz obliczyć z Fahrenhaita na Celsjusze')
print(f'[FK] - jeśli chcesz obliczyć z Fahrenhaita na Kelwiny')
print(f'[KF] - jeśli chcesz obliczyć z Kelwinów na Fahrenhaita')
print(f'______________________________________________________')

wybór = input()

if wybór == 'CK':
    print(f'Wybrano kalkulator Celsjuszy na Kelwiny')
    print(f'Wpisz Celsjusze (bez przecinka):')
    print(f'________________________________')
    CK = int(input())
    wynik1 = CK + 273
    print(f'{CK} Celsjuszy to ok. {wynik1} Kelwinów')
elif wybór == 'KC':
    print(f'________________________________________')
    print(f'Wybrano kalkulator Kelwinów na Celsjuszy')
    print(f'Wpisz Kelwiny (bez przecinka):')
    KC = int(input())
    wynik2 = KC - 273
    print(f'{KC} Kelwinów to ok. {wynik2} Celsjuszy')
elif wybór == 'CF':
    print(f'___________________________________________________')
    print(f'Wybrano kalkulator Celsjuszy na stopnie Fahrenhaita')
    print(f'Wpisz Celsjusze (bez przecinka):')
    CF = int(input())
    Fahrenhait1 = CF * 9
    Fahrenhait2 = Fahrenhait1 / 5
    Fahrenhait3 = Fahrenhait2 + 32
    print(f'{CF} Celsjuszy to ok. {Fahrenhait3} stopni Fahrenhaita')
elif wybór == 'FC':
    print(f'__________________________________________________')
    print(f'Wybrano kalkulator stopni Fahrenhaita na Celsjusza')
    print(f'Wpisz stopnie Fahrenhaita (bez przecinka):')
    FC = int(input())
    Celsjusze1 = FC - 32
    Celsjusze2 = Celsjusze1 * 5
    Celsjusze3 = Celsjusze2 / 9
    print(f'{FC} stopni Fahrenhaita to ok. {Celsjusze3} Celsjuszy')
elif wybór == 'FK':
    print(f'Niestety kalkulator stopni Fahrenhaita na Kelwiny nie jest jeszcze gotowy :(')
elif wybór == 'KF':
    print(f'__________________________________________________')
    print(f'Wybrano kalkulator Kelwinów na stopnie Fahrenhaita')
    print(f'Wpisz Kelwiny (bez przecinka):')
    KF = int(input())
    Fahrenhait4 = KF - 273
    Fahrenhait5 = Fahrenhait4 * 1.8
    Fahrenhait6 = Fahrenhait5 + 32
    print(f'{KF} Kelwinów to ok. {Fahrenhait6} stopni Fahrenhaita')
else:
    print(f'Podano zły wybór...')

print(f'Wpisz byle co, żeby zamknąć aplikację...')
byleco = input()