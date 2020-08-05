##Zadanie rekrutacyjne BACKEND
Autor rozwiązania: Rafał Nitychoruk

###Wymagania
Program wymaga do działania bibliotek standardowych dla Pythona 3.7 oraz SQLAlchemy.

###Uruchamianie
Aby uruchomić program należy z przejść do folderu nadrzędnego nad programem i podać w terminalu jego nazwę wraz z komendą.

Przykładowa komenda:
>python play.py -h

Aby poznać dostępne polecenia linii komend możesz także użyć komendy
>"python play.py -h".

###Początek pracy
Na początku pracy z programem neleży wypełnić bazę danymi.
służy do tego komenda -f


###Dostępne argumenty

Pokazuje dostępne komendy wraz z opcjami.
>-h, --help

Inicjalizuje bazę oraz wypełnia ją przykładowymi danymi.
>-f', --fill

Zwraca użytkowników urodzonych w podanym zakresie dat.
Wymaga dwóch atrybutów daty w formacie UTC, YYYY-MM-DD, YYYY-MM lub YYYY"
>-d, --dob

Zwraca średnią wieku dla płci lub całości populacji w bazie.
Wymaga atrybutu z puli ['female', 'male', 'balance'].
>-a, --average-age
    
Zwraca średnią dla jednej lub wszystkich płci w populacji zapisanej w bazie.
Wymaga atrybutu z puli ['female', 'male', 'balance'].
>-g, --average-gender

Zwraca najpopularniejsze miasta spośród danych w bazie. Funkcja zwraca wybraną liczbę miast.
Wymaga atrybutu typu int. Wartość minimalna to jedno miasto.
>-c, --common-city
    
Zwraca najpopularniejsze hasła spośród danych w bazie. Funkcja zwraca wybraną liczbę haseł.
Wymaga atrybutu typu int. Wartość minimalna to jedno hasło.
>-p, --common-pass
    
Funkcja zwraca najmocniejsze hasło spośród danych w bazie.
>-s, --strong-pass
    

