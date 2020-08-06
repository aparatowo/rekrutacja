import argparse
from .tools import fill_up_base, average_age, dob_range, \
    average_gender, popular_city, popular_passwords, strongest_password


def argparse_commands():
    """
    Function stores argparse attributes and arguments.
    It runs without any other arguments than those called in terminal.

    >python play.py -h

    """
    parser = argparse.ArgumentParser(description='Prosty program do zarządzania danymi.')
    parser.add_argument('-f', '--fill', action='store_true',
                        help='Funkcja inicjalizuje bazę oraz wypełnia ją przykładowymi danymi.')
    parser.add_argument('-d', '--dob', nargs=2,
                        help='Funkcja zwraca użytkowników urodzinych w podanym zakresie dat. Optymalny format daty to "YYYY-MM-DD YYYY-MM-DD"')
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

    parser.add_argument('-s', '--strong-pass', action='store_true',
                        help='Funkcja zwraca najmocniejsze hasło spośród danych w bazie.')

    args = parser.parse_args()

    # This section refers to -d argument and lists persons with dob between two dates given.
    if args.dob:
        first_date = args.dob[0]
        second_date = args.dob[1]
        people_range = dob_range(first_date, second_date)
        print(f'Ludzie urodzeni w zakresie dat od {first_date} do {second_date}:')
        print(' ' + 70 * '-')  # simple separator line

        for count, item in enumerate(people_range, 1):
            print(f'{count:4}. {item}')  # order number + city + counter
            print(' ' + 70 * '-')  # simple separator line

    # This section refers to -a argument. Allows user to see database population average age by gender.
    elif args.average_age:
        get_average = average_age()
        if args.average_age == 'male':
            print(f'Średni wiek mężczyzny w bazie to {get_average[1]} lat.')
        elif args.average_age == 'female':
            print(f'Średni wiek kobiety w bazie to {get_average[2]} lat.')
        elif args.average_age == 'balance':
            print(f'Średni wiek użytkownika w bazie to {get_average[0]} lat.')

    # This section refers to -g argument. Allows user to see database population percentage by gender.
    elif args.average_gender:
        get_percentage = average_gender()
        if args.average_gender == 'male':
            print(f'Mężczyźni to średnio {get_percentage[0]}% populacji zapisanej w bazie.')
        elif args.average_gender == 'female':
            print(f'Kobiety to średnio {get_percentage[1]}% populacji zapisanej w bazie')
        elif args.average_gender == 'balance':
            print(f'Kobiety stanowią {get_percentage[1]}% populacji zapisanej w bazie danych.' \
                  f'Mężczyźni stanowią {get_percentage[0]}% populacji.')

    # This section refers to -c argument. It lists most popular cities.
    elif args.common_city:
        user_input = args.common_city
        get_popular_city = popular_city(user_input)

        if user_input == 1:
            city = get_popular_city[0]
            print(f'Najpopularniejsze miasto to {city[0]} - pojawia się w bazie {city[1]}x.')
        elif user_input > 1:
            print('Lista najpopularniejszych miast z częstotliwością występowania:')
            print(' ' + 42 * '-')  # simple separator line

            for count, city in enumerate(get_popular_city, 1):
                print(f'|{count:4}. {city[0]:30} | {city[1]}x |')  # order number + city + counter
                print(' ' + 42 * '-')  # simple separator line

    # This section refers to -p argument. It lists most popular passwords.
    elif args.common_pass:
        user_input = args.common_pass
        get_popular_pass = popular_passwords(user_input)

        if user_input == 1:
            password = get_popular_pass[0]
            print(f'Najpopularniejsze hasło to {password[0]} - pojawia się w bazie {password[1]}x.')
        elif user_input > 1:
            print('Lista najpopularniejszych haseł z częstotliwością występowania:')
            print(' ' + 42 * '-')  # simple separator line

            for count, password in enumerate(get_popular_pass, 1):
                print(f'|{count:4}. {password[0]:30} | {password[1]}x |')  # order number + password + counter
                print(' ' + 42 * '-')  # simple separator line

    # This section refers to -s attribute. It lists best stored passwords.
    elif args.strong_pass:
        password = strongest_password()
        if len(password) == 1:
            print(f'Najmocniejszym hasłem w bazie jest {password[0][0]}, które osiągnęło wynik {password[0][1]}.')
        else:
            print(f'Najmocniejszymi hasłami w bazie są:')
            print(' ' + 42 * '-')  # simple separator line

            for count, password in enumerate(password, 1):
                print(f'|{count:4}. {password[0]:30} | {password[1]}x |')  # order number + password + counter
                print(' ' + 42 * '-')  # simple separator line

    # This section refers to -h argument. It fills up database with sample data.
    elif args.fill:
        fill_up_base()
        print()

    # Simple helper section.
    else:
        print('Wpisz "python play.py -h" aby zobaczyć pomoc.')
        print('Type "python play.py -h" to get help.')
