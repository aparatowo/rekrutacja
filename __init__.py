from tools import fill_up_base, average_age, input_validation, \
    average_gender, popular_city, popular_passwords, strongest_password, \
    dob_range
from commandline_interface import argparse_commands

args = argparse_commands()

if __name__ == '__main__':

    if args.average_age:
        get_average = average_age()

        if args.average_age == 'male':
            print(f'Średni wiek mężczyzny w bazie to {get_average[1]} lat.')
        elif args.average_age == 'female':
            print(f'Średni wiek kobiety w bazie to {get_average[2]} lat.')
        elif args.average_age == 'balance':
            print(f'Średni wiek użytkownika w bazie to {get_average[0]} lat.')

    elif args.average_gender:
        get_average = average_gender()
        if args.average_gender == 'male':
            print(f'Mężczyźni to średnio {get_average[0]}% populacji zapisanej w bazie.')
        elif args.average_gender == 'female':
            print(f'Kobiety to średnio {get_average[1]}% populacji zapisanej w bazie')
        elif args.average_gender == 'balance':
            print(f'Kobiety stanowią {get_average[1]}% populacji zapisanej w bazie danych.' \
                  f'Mężczyźni stanowią {get_average[0]}% populacji.')

    elif args.common_city:
        validated_input = input_validation(args.common_city)
        get_popular_city = popular_city(validated_input)

        if validated_input == 1:
            city = get_popular_city[0]
            print(f'Najpopularniejsze miasto to {city[0]} - pojawia się w bazie {city[1]}x.')
        elif validated_input > 1:
            print('Lista najpopularniejszych miast z częstotliwością występowania:')
            print(' ' + 42 * '-')  # linia oddzielająca

            for count, item in enumerate(get_popular_city, 1):
                print(f'|{count:4}. {item[0]:30} | {item[1]}x |')  # numer porządkowy + nazwa miasta + licznik
                print(' ' + 42 * '-')  # linia oddzielająca

    elif args.common_pass:
        validated_input = input_validation(args.common_pass)
        get_popular_pass = popular_passwords(validated_input)

        if validated_input == 1:
            city = get_popular_pass[0]
            print(f'Najpopularniejsze hasło to {city[0]} - pojawia się w bazie {city[1]}x.')
        elif validated_input > 1:
            print('Lista najpopularniejszych haseł z częstotliwością występowania:')
            print(' ' + 42 * '-')  # linia oddzielająca

            for count, item in enumerate(get_popular_pass, 1):
                print(f'|{count:4}. {item[0]:30} | {item[1]}x |')  # numer porządkowy + hasło + licznik
                print(' ' + 42 * '-')  # linia oddzielająca


    elif args.strong_pass:
        password = strongest_password()
        print(f'Najmocniejszym hasłem w bazie jest {password[0]}, które osiągnęło wynik {password[1]}.')

    elif args.fill:
        fill_up_base()
        print()

test = dob_range('1980-05-26T02:46:09.953Z', '1990-05-26T02:46:09.953Z')
print(len(test))
print(test)

