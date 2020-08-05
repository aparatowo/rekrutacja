from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Person(Base):
    """
    SQLAlchemy object and database model.
    Two magic methods were modified: __repr__ and __str__.
    This way we can show more readable format of data when needed.
    """
    __tablename__ = 'persons'

    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    gender = Column(String(), nullable=False)
    title = Column(String(), nullable=False)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    id_name = Column(String())
    id_value = Column(String())
    nat = Column(String())
    dob = Column(DateTime(timezone=True))  # day of birth
    age = Column(Integer(), nullable=False)
    dtb = Column(Integer(), nullable=False)  # days to birthday
    register_date = Column(String())
    register_age = Column(Integer())
    uuid = Column(String())
    username = Column(String())
    password = Column(String())
    pass_strength = Column(Integer())
    salt = Column(String())
    md5 = Column(String())
    sha1 = Column(String())
    sha256 = Column(String())
    email = Column(String())
    phone = Column(Integer())
    cellphone = Column(Integer())
    street_name = Column(String())
    street_number = Column(String())
    city = Column(String())
    postcode = Column(String())
    state = Column(String())
    country = Column(String())
    latitude = Column(String())
    longitude = Column(String())
    timezone_offset = Column(String())
    timezone_desc = Column(String())

    def __str__(self):
        return f'{self.title} {self.first_name} {self.last_name}, {self.gender} from {self.city} in {self.country}'

    def __repr__(self):
        return f'{self.first_name} {self.last_name} from {self.country}'
