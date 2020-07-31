from sqlalchemy import event, create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from json import load


# from string import ascii_lowercase, ascii_uppercase, digits, punctuation

# DB and connectione setting
def _fk_pragma_on_connect(dbapi_con):
    dbapi_con.execute('pragma foreign_keys=ON')


def get_session(echo=False):
    engine = create_engine('sqlite:///database.db', echo=echo)
    DBSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    event.listen(engine, 'connect', _fk_pragma_on_connect)

    return DBSession()

#TODO
# dodanie osób do bazy
def fill_up_base():
    conn = get_session()
    persons_dict = None

    with open("persons.json", encoding="utf8") as persons_json:
        persons_dict = load(persons_json)

    for result in persons_dict['results']:
        result




#TODO
# użytkownicy urodzeni w zakresie dat

#TODO
# średnia wieku

#TODO
# popularne miasta

#TODO
# popularne hasła

#TODO
# najsilniejsze hasło

def pass_strength_score(password):
    score = 0
    lowercase = None
    uppercase = None
    digits = None
    special = None

    for symbol in password:
        if symbol.islower():
            lowercase = True
        if symbol.isupper():
            uppercase = True
        if symbol.isdigit():
            digits = True
        if not symbol.isalnum():
            special = True

    if lowercase:
        score += 1
    if uppercase:
        score += 2
    if digits:
        score += 1
    if len(password) >= 8:
        score += 5
    if special:
        score += 3

    return score

#TODO
# dni do urodzin


#TODO
# dodatkowe: request z api
