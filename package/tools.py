from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker
from package.models import *
from json import load
from datetime import datetime as dt


def get_session(echo=False):
    engine = create_engine('sqlite:///database.db', echo=echo)
    DBSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    return DBSession()


def fill_up_base():
    conn = get_session()
    persons_dict = None
    persons_list = []

    with open("package/persons.json", encoding="utf8") as persons_json:
        persons_dict = load(persons_json)

    for result in persons_dict['results']:
        persons_list.append(person_data_formating(result))

    conn.bulk_save_objects(persons_list)
    conn.commit()
    conn.close()


def person_data_formating(data):
    gender = data['gender']
    title = data['name']['title']
    first_name = data['name']['first']
    last_name = data['name']['last']
    id_name = data['id']['name']
    id_value = data['id']['value']
    nat = data['nat']
    dob = str_to_date(data['dob']['date'])
    age = data['dob']['age']
    dtb = days_till_bd(dob)
    register_date = str_to_date(data['registered']['date'])
    register_age = data['registered']['age']
    uuid = data['login']['uuid']
    username = data['login']['username']
    password = data['login']['password']
    pass_strength = pass_strength_score(password)
    salt = data['login']['salt']
    md5 = data['login']['md5']
    sha1 = data['login']['sha1']
    sha256 = data['login']['sha256']
    email = data['email']
    phone = clear_phone_number(data['phone'])
    cellphone = clear_phone_number(data['cell'])
    street_name = data['location']['street']['name']
    street_number = data['location']['street']['number']
    city = data['location']['city']
    postcode = data['location']['postcode']
    state = data['location']['state']
    country = data['location']['country']
    latitude = data['location']['coordinates']['latitude']
    longitude = data['location']['coordinates']['longitude']
    timezone_offset = data['location']['timezone']['offset']
    timezone_desc = data['location']['timezone']['description']

    return Person(gender=gender, title=title, first_name=first_name, last_name=last_name,
                  id_name=id_name, id_value=id_value, nat=nat, dob=dob, age=age, dtb=dtb,
                  register_date=register_date, register_age=register_age, uuid=uuid,
                  username=username, password=password, pass_strength=pass_strength,
                  salt=salt, md5=md5, sha1=sha1, sha256=sha256, email=email, phone=phone,
                  cellphone=cellphone, street_name=street_name, street_number=street_number,
                  city=city, postcode=postcode, state=state, country=country, latitude=latitude,
                  longitude=longitude, timezone_offset=timezone_offset, timezone_desc=timezone_desc)


def str_to_date(input_string):
    date = str(input_string).replace('Z', '+00:00')
    try:
        date = dt.fromisoformat(date)
        return date
    except (ValueError, TypeError):
        pass

    try:
        date = dt.strptime(date, '%Y-%M-%D')
        return date
    except (ValueError, TypeError):
        pass

    try:
        date = dt.strptime(date, '%Y-%M')
        return date
    except (ValueError, TypeError):
        pass

    try:
        date = dt.strptime(date, '%Y')
        return date
    except (ValueError, TypeError):
        pass

    raise ValueError('Nieprawidłowy format daty')


def days_till_bd(date):
    now = dt.now()
    dob = str_to_date(date)
    try:
        this_year_bd = dt(now.year, dob.month, dob.day)
        next_year_bd = dt(now.year + 1, dob.month, dob.day)
    except ValueError:
        this_year_bd = dt(now.year, dob.month, dob.day - 1)
        next_year_bd = dt(now.year + 1, dob.month, dob.day - 1)
        # metoda ominięcia problemu roku przestępnego
        # zakładam, że osoby urodzone 29 lutego jednak nie świętują urodzin co 4 lata lecz z końcem lutego.

    delta = [(this_year_bd - now), (next_year_bd - now)]
    delta = max(delta)
    return delta.days


def popular_city(int=1):
    most_popular = []
    conn = get_session()

    query_result = [city for city, in conn.query(Person.city).all()]
    result_set = set(query_result)

    cities_counted = [(city, query_result.count(city)) for city in result_set]
    most_popular = sorted(cities_counted, key=lambda c: c[1], reverse=True)[0:abs(int)]
    conn.close()
    return most_popular


def popular_passwords(int=1):
    conn = get_session()

    query_result = [password for password, in conn.query(Person.password).all()]
    result_set = set(query_result)

    counted_passwords = [(password, query_result.count(password)) for password in result_set]
    most_popular = sorted(counted_passwords, key=lambda c: c[1], reverse=True)[0:abs(int)]
    conn.close()
    return most_popular


def strongest_password():
    conn = get_session()
    max_pass_score, = conn.query(func.max(Person.pass_strength)).one()
    best_passwords = conn.query(Person.password, Person.pass_strength) \
        .filter(Person.pass_strength == max_pass_score).all()
    return best_passwords


def dob_range(first_date, second_date):
    first_date = str_to_date(first_date)
    second_date = str_to_date(second_date)
    conn = get_session()
    query_result = conn.query(Person).filter(Person.dob >= first_date).filter(Person.dob <= second_date).all()
    return query_result


def average_age():
    query_result = None
    conn = get_session()

    query_result = conn.query(Person.age, Person.gender).all()
    general_result = [age for age, gender in query_result]
    male_result = [age for age, gender in query_result if gender == 'male']
    female_result = [age for age, gender in query_result if gender == 'female']

    averages = [float(sum(gender_age_result)) / len(gender_age_result)
                for gender_age_result in [general_result, male_result, female_result]]

    return averages


def average_gender():
    query_result = None
    conn = get_session()
    query_result = [gender for gender, in conn.query(Person.gender).all()]
    male_percentage = float(query_result.count('male')) / len(query_result) * 100
    female_percentage = float(query_result.count('female')) / len(query_result) * 100
    return male_percentage, female_percentage


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


def clear_phone_number(data):
    cleared_data = []
    new_string = ""
    for symbol in data:
        if symbol.isdigit():
            cleared_data.append(symbol)
    data_string = new_string.join(cleared_data)
    return data_string


def input_validation(number_given):
    number_given = number_given
    try:
        proper_integer = int(number_given)
    except (ValueError, TypeError):
        proper_integer = 1
    return abs(proper_integer)
