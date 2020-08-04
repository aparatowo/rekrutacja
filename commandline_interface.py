# TODO
# procent kobiet
# procent mężczyzn
# procenty obu wartości
# średnia wieku kobiet
# średnia wieku mężczyzn
# średnia wieku ogólna
# X najbardziej popularnych miast - miasto, liczba wystąpień, X to zmienna
# X najbardziej popularnych haseł - hasło, liczba wystąpień, X to zmienna
# użytkownicy urodzeni między X i Y
# najbezpieczniejsze hasło
# .

import argparse


def argparse_commands():
    parser = argparse.ArgumentParser(description='Prosty program do zarządzania danymi.')
    parser.add_argument('-f', '--fill', action='store_true',
                        help='Funkcja inicjalizuje bazę oraz wypełnia ją przykładowymi danymi.')
    parser.add_argument('-a', '--average-age',
                        choices=['female', 'male', 'balance'],
                        help='Funkcja zwraca średnią wieku dla płci lub całości populacji w bazie.')
    parser.add_argument('-g', '--average-gender',
                        choices=['female', 'male', 'balance'],
                        help='Funkcja zwraca średnią dla jednej lub wszystkich płci w populacji zapisanej w bazie.')
    parser.add_argument('-c', '--common-city', type=int,
                        help='Funkcja zwraca najpopularniejsze miasta spośród danych w bazie. ' \
                             'Funkcja zwraca wybraną liczbę miast. Wartość minimalna to jedno miasto.')
    parser.add_argument('-p', '--common-pass', type=int,
                        help='Funkcja zwraca najpopularniejsze hasła spośród danych w bazie. ' \
                             'Funkcja zwraca wybraną liczbę haseł. Wartość domyślna to jedno hasło.')

    parser.add_argument('-s', '--strong_pass', action='store_true',
                        help='Funkcja zwraca najmocniejsze hasło spośród danych w bazie.')

    return parser.parse_args()
