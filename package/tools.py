from sqlalchemy import func, create_engine
from sqlalchemy.orm import sessionmaker
from package.models import Base, Person
from json import load
from datetime import datetime as dt


def get_session():
    """
    This function creates connection with database.

    :return: Session with database object
    """
    engine = create_engine('sqlite:///database.db')
    DBSession = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    return DBSession()


def fill_up_base():
    """
    This function will fill up database with example data.
    """
    example_file = "package/persons.json"
    conn = get_session()
    persons_dict = None
    persons_list = []

    with open(example_file, encoding="utf8") as persons_json:
        persons_dict = load(persons_json)

    for result in persons_dict['results']:
        persons_list.append(person_data_formating(result))

    conn.bulk_save_objects(persons_list)
    conn.commit()
    conn.close()


def person_data_formating(data):
    """
    Function prepares data to transfer into database.
    Skips information about pictures.
    Transform dates into date timeobjects
    Adds days till birthday and password strength score - both based on input data.

    :param data: example data (dict) structure
  {
    "gender":"female",
    "name":{"title":"Miss","first":"Louane","last":"Vidal"},
    "location":{
      "street":{
        "number":2479,
        "name":"Place du 8 Février 1962"},
      "city":"Avignon",
      "state":"Vendée",
      "country":"France",
      "postcode":78276,
      "coordinates":{
        "latitude":"2.0565",
        "longitude":"95.2422"},
      "timezone":{
        "offset":"+1:00",
        "description":"Brussels, Copenhagen, Madrid, Paris"}},
    "email":"louane.vidal@example.com",
    "login": {
      "uuid":"9f07341f-c7e6-45b7-bab0-af6de5a4582d",
      "username":"angryostrich988",
      "password":"r2d2",
      "salt":"B5ywSDUM",
      "md5":"afce5fbe8f32bcec1a918f75617ab654",
      "sha1":"1a5b1afa1d9913cf491af64ce78946d18fea6b04",
      "sha256":"0124895aa1e6e5fb0596fad4c413602e0922e8a8c2dc758bbdb3fa070ad25a07"},
    "dob":{
      "date":"1966-06-26T11:50:25.558Z",
      "age":54},
    "registered":{
      "date":"2016-08-11T06:51:52.086Z",
      "age":4},
    "phone":"02-62-35-18-98",
    "cell":"06-07-80-83-11",
    "id":{
      "name":"INSEE",
      "value":"2NNaN01776236 16"},
    "picture":{
      "large":"https://randomuser.me/api/portraits/women/88.jpg",
      "medium":"https://randomuser.me/api/portraits/med/women/88.jpg",
      "thumbnail":"https://randomuser.me/api/portraits/thumb/women/88.jpg"},
    "nat":"FR"},
    :type data: dict

    :return: Person object based on SQLAlchemy model.
    :rtype: object

    NOTE:
    Function may be easily transform to return dicts.
    All variables fits Person object attribute names.

    Person(gender, title, first_name, last_name,
           id_name, id_value, nat, dob, age, dtb,
           register_date, register_age, uuid,
           username, password, pass_strength,
           salt, md5, sha1, sha256, email, phone,
           cellphone, street_name, street_number,
           city, postcode, state, country, latitude,
           longitude, timezone_offset, timezone_desc)

    """
    gender = data['gender']
    title = data['name']['title']
    first_name = data['name']['first']
    last_name = data['name']['last']
    id_name = data['id']['name']
    id_value = data['id']['value']
    nat = data['nat']
    dob = str_to_date(data['dob']['date'])  # day of birth
    age = data['dob']['age']
    dtb = days_till_bd(dob)  # days till birth
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


def str_to_date(input_string, message='Nieprawidłowy format daty'):
    """
    Transform different strings into datetime objects.

    :param input_string: Takes string formatted in one of four possible scenarios:
        UTC format ended with timezone information including specific 'Z' letter situation.
        Year, month and day in %Y-%M-%D format (2020-08-05)
        Year and month in %Y-%M format (2020-08)
        Year in %Y format (2020)
    :type input_string: str

    :param message: Message value defines info which prompts when ValueError raised.
    :type message: str

    :return: date
    :rtype: datetime

    :raise ValueError: Function try different scenarios and raises ValueError when can't deal with data.

    NOTE:
        Python standard libraries can't deal properly with letter ended UTC format.
        It ins't a problem while timezone is stored separate place.
        In our case 'Z' letter stands for Zulu time which means no time zone shift.
        Skipping last letter makes function naive so I've decided to change 'Z' letter in this specific scenario.
        Strongly recommend external library.
    """
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

    raise ValueError(message)


def days_till_bd(date):
    """
    Function counts days till future birthday based on given day of birth.
    It deals with leap year dob problem by counting days till the last day of february.

    :param date: Day of birth in UTC format.
    :type date: str

    :return: Days till closest future birthday
    :rtype: int
    """
    now = dt.now()
    dob = str_to_date(date)

    try:
        this_year_bd = dt(now.year, dob.month, dob.day)
        next_year_bd = dt(now.year + 1, dob.month, dob.day)
    except ValueError:
        this_year_bd = dt(now.year, dob.month, dob.day - 1)
        next_year_bd = dt(now.year + 1, dob.month, dob.day - 1)

    delta = [(this_year_bd - now), (next_year_bd - now)]
    delta = max(delta)
    return delta.days


def popular_city(answers=1):
    """
    Picks most popular cities from database.

    :param answers: Defines how many cities will be returned as an answers.
    :type answers: int

    :return: List of tuples, where first value is city (str) and second one is count (int).
    :rtype: list
    """
    conn = get_session()
    query_result = [city for city, in conn.query(Person.city).all()]
    conn.close()

    result_set = set(query_result)
    cities_counted = [(city, query_result.count(city)) for city in result_set]
    most_popular = sorted(cities_counted, key=lambda c: c[1], reverse=True)[0:abs(answers)]
    return most_popular


def popular_passwords(answers=1):
    """
    Picks most popular passwords from database.

    :param answers: Defines how many passwords will be returned as an answers.
    :type answers: int

    :return: List of tuples, where first value is password (str) and second one is count (int).
    :rtype: list
    """
    conn = get_session()
    query_result = [password for password, in conn.query(Person.password).all()]
    conn.close()

    result_set = set(query_result)
    counted_passwords = [(password, query_result.count(password)) for password in result_set]
    most_popular = sorted(counted_passwords, key=lambda c: c[1], reverse=True)[0:abs(answers)]
    return most_popular


def strongest_password():
    """
    Function checks the strongest password score in database.

    :return: List of tuples where first value is password (str) and the second is strength score (int)
    :rtype: list

    NOTE:
        Function first query base for highest password score stored,
        then query it specifically for the strongest passwords.
        This way we do not need query and process all the records from growing database.
        Still, function can be modified do that.
    """
    conn = get_session()
    max_pass_score, = conn.query(func.max(Person.pass_strength)).one()
    best_passwords = conn.query(Person.password, Person.pass_strength) \
        .filter(Person.pass_strength == max_pass_score).all()
    conn.close()
    return best_passwords


def dob_range(first_date, second_date):
    """
    Function query person data based on given date range.

    :param first_date: Must fit "str_to_date()" function requirements.
    :type first_date: str
    :param second_date:
    :type second_date: str

    :return: List of Person objects based on SQLAlchemy model
    :rtype: list

    NOTE:
     "str_to_date()" function requirements:
        Function takes string input formatted in one of four possible scenarios:
        UTC format ended with timezone information including specific 'Z' letter situation.
        Year, month and day in %Y-%M-%D format (2020-08-05)
        Year and month in %Y-%M format (2020-08)
        Year in %Y format (2020)
    """
    first_date = str_to_date(first_date)
    second_date = str_to_date(second_date)
    conn = get_session()
    query_result = conn.query(Person).filter(Person.dob >= first_date).filter(Person.dob <= second_date).all()
    return query_result


def average_age():
    """
    Function query age and gender tuples from database and count average age.

    :return: Average age for entire databased population, for males and for females.
        It gives back list of (int) values.
    :rtype: list

    NOTE:
        While this solution is sufficient enough for smaller databases,
        it can be easily adapted to narrow data while querying bigger databases.
    """
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
    """
    Function counts an average male and female percentage based on data stored in database.

    :return: Tuple of floats.
    :rtype: tuple
    """
    query_result = None
    conn = get_session()
    query_result = [gender for gender, in conn.query(Person.gender).all()]
    male_percentage = float(query_result.count('male')) / len(query_result) * 100
    female_percentage = float(query_result.count('female')) / len(query_result) * 100
    return male_percentage, female_percentage


def pass_strength_score(password):
    """
    Function scores the password strength.

    :param password: Regular string with letters, special characters and digits.
    :type password: str

    :return: Password score value
    :rtype: int

    NOTE:
        There is way more 'pythonic' solution based on any() build in function,
        but I found out that if-elif construct in for loop is still more efficient.
        The code is split into two main parts. First part is mentioned above.
        Second part allows to adjust scoring points values.
    """
    score = 0
    lowercase = None
    uppercase = None
    digits = None
    special = None

    for symbol in password:
        if symbol.islower():
            lowercase = True
            pass
        elif symbol.isupper():
            uppercase = True
            pass
        elif symbol.isdigit():
            digits = True
            pass
        elif not symbol.isalnum():
            special = True
            pass

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
    """
    Function helps clear phone numbers from any non-digit characters.
    :param data: Phone number with non-digit characters
    :type data: str

    :return: Cleared phone number
    :rtype: int
    """
    cleared_data = []
    data_string = ""
    for symbol in data:
        if symbol.isdigit():
            cleared_data.append(symbol)
    data_string = data_string.join(cleared_data)
    return int(data_string)
