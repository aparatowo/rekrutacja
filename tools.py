from sqlalchemy import event, create_engine
from sqlalchemy.orm import sessionmaker
from models import *
from json import load
from datetime import datetime as dt


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
    persons_list = []

    with open("persons.json", encoding="utf8") as persons_json:
        persons_dict = load(persons_json)

    for result in persons_dict['results']:
        normalised_result(result)
        result.append(Person())

def normalised_person_data(data):
    gender = data['gender']
    title = data['name']['title']
    first_name = data['name']['first']
    last_name = data['name']['last']
    id_name = data['id']['name']
    id_value = data['id']['value']
    nat = data['nat']
    dob = data['dob']['date']
    age = data['dob']['age']
    dtb = days_till_bd(dob)
    uuid = data['login']['uuid']
    username = data['login']['username']
    password = data['login']['password']
    pass_strength = pass_strength_score(password)
    salt = data['login']['salt']
    md5 = data['login']['md5']
    sha1 = data['login']['sha1']
    sha256 = data['login']['sha256']
    email = data['email']
    phone = data['phone']
    cellphone = data['cell']
    street_name = data['location']['street']['name']
    home_number = data['location']['street']['number']
    city = data['location']['city']
    postcode = data['location']['postcode']
    state = data['location']['state']
    country = data['location']['country']
    latitude = data['location']['coordinates']['latitude']
    longitude = data['location']['coordinates']['longitude']
    timezone_offset = data['location']['timezone']['offset']
    timezone_desc = data['location']['timezone']['description']

def str_to_date(date, skip_char=1):
    return dt.fromisoformat(date[0:-skip_char])

def days_till_bd(date):
    now = dt.now()
    dob = str_to_date(date)
    this_year_bd = dt(now.year, dob.month, dob.day)
    next_year_bd = dt(now.year+1, dob.month, dob.day)
    delta = [(this_year_bd - now), (next_year_bd - now)]
    delta = max(delta)
    return delta.days



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
