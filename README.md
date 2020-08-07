##Zadanie rekrutacyjne BACKEND
Autor rozwiązania: Rafał Nitychoruk

###Wymagania
Program wymaga do działania bibliotek standardowych dla Pythona 3.7 oraz SQLAlchemy i Requests.<br>
Dokładna specyfikacja niezbędnych bibliotek i ich zaleźności znajduje się w pliku requirements.txt


###Uruchamianie
Aby uruchomić program należy z przejść do folderu nadrzędnego nad programem i podać w terminalu jego nazwę wraz z komendą.

Aby poznać dostępne polecenia linii komend możesz także użyć atrybutu -h <br>
   >python play.py -h

#####Początek pracy - pierwsze uruchomienie
Na początku pracy z programem neleży wypełnić bazę danymi.
służy do tego argument -f
   >python play.py -f



###Dostępne argumenty i atrybuty

* '-h, --help' <br>
Pokazuje dostępne komendy wraz z opcjami.
    >python play.py -h
 
* '-f, --fill' <br>
Inicjalizuje bazę oraz wypełnia ją przykładowymi danymi. <br>
Przykładowe dane znajdują się w źródle programu, jednak można użyć źródła z sieci (randomuser.me).
Funkcja wymaga podania atrybutu 'sample' by użyć źródła domyślnego (1000 gotowych rekordów)<br>
Funkcja wymaga podania atrybutu w zakresie 1-5000 by użyć źródła API (rekordy unikalne)<br>
    >python play.py -f sample

    >python play.py -f 3500

* '-d, --dob' <br>
Zwraca użytkowników urodzonych w podanym zakresie dat. <br>
Wymaga dwóch atrybutów daty w formacie UTC, YYYY-MM-DD, YYYY-MM lub YYYY" <br>
Uwaga: czas w formacie UTC powinien być podany w zapisie '+HH:MM' lub zakończony Z (Zulu).
    >python play.py -d 1986-06-21T01:04:42.172Z 1990

    >python play.py -d 1977 1986-06-21T01:04:42+13:00

* '-a, --average-age' <br>
Zwraca średnią wieku dla płci lub całości populacji w bazie. <br>
Wymaga atrybutu z puli ['female', 'male', 'balance'].
    >python play.py -a balance

* '-g, --average-gender' <br>
Zwraca średnią dla jednej lub wszystkich płci w populacji zapisanej w bazie. <br>
Wymaga atrybutu z puli ['female', 'male', 'balance'].
    >python play.py -g balance

* '-c, --common-city' <br>
Zwraca najpopularniejsze miasta spośród danych w bazie. Funkcja zwraca wybraną liczbę miast. <br>
Wymaga atrybutu typu int. Wartość minimalna to jedno miasto.
    >python play.py -c 3
    
* '-p, --common-pass' <br>
Zwraca najpopularniejsze hasła spośród danych w bazie. Funkcja zwraca wybraną liczbę haseł.
Wymaga atrybutu typu int. Wartość minimalna to jedno hasło.
    >python play.py -p 6
    
* '-s, --strong-pass' <br>
Funkcja zwraca najmocniejsze hasło spośród danych w bazie. <br>
Jeśli haseł o takiej samej sile będzie więcej, funkcja wylistuje je.
    >python play.py -s    

