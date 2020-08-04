Zadanie rekrutacyjne BACKEND
Autor rozwiązania: Rafał Nitychoruk

#Wymagania
Program wymaga do działania bibliotek standardowych oraz SQLAlchemy.

#Uruchamianie
Aby uruchomić program należy z przejść do folderu nadrzędnego nad programem i podać w terminalu jego nazwę wraz z komendą.

Przykładowa komenda:
>python play.py -h

Aby poznać dostępne polecenia linii komend możesz także użyć komendy "python play.py -h".
Używając starszej wersji pythona należy użyć komendy "python3 play.py -h".

#Początek pracy
Na początku pracy z programem neleży wypełnić bazę danymi.
służy do tego komenda -f

#Dostępne komendy
-h, --help
    Pokazuje dostępne komendy wraz z opcjami
-f', --fill
    Inicjalizuje bazę oraz wypełnia ją przykładowymi danymi.')
-d, --dob
    Zwraca użytkowników urodzonych w podanym zakresie dat.
    Wymaga dwóch atrybutów daty w formacie UTC, YYYY-MM-DD, YYYY-MM lub YYYY"
-a, --average-age
    Zwraca średnią wieku dla płci lub całości populacji w bazie.
    Wymaga atrybutu z puli ['female', 'male', 'balance'].
-g, --average-gender
    Zwraca średnią dla jednej lub wszystkich płci w populacji zapisanej w bazie.
    Wymaga atrybutu z puli ['female', 'male', 'balance'].
-c, --common-city
    Zwraca najpopularniejsze miasta spośród danych w bazie. Funkcja zwraca wybraną liczbę miast.
    Wymaga atrybutu typu int. Wartość minimalna to jedno miasto.
-p, --common-pass
    Zwraca najpopularniejsze hasła spośród danych w bazie. Funkcja zwraca wybraną liczbę haseł.
    Wymaga atrybutu typu int. Wartość minimalna to jedno hasło.
-s, --strong-pass
    Funkcja zwraca najmocniejsze hasło spośród danych w bazie.

