from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Person(Base):
    __tablename__ = 'persons'

    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    gender = Column(String(50), nullable=False)
    title = Column(String(50), nullable=False)
    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    id_name = Column(String(50))
    id_value = Column(String(50))
    nat = Column(String(50))
    dob = Column(String(50), nullable=False) #day of birth
    age = Column(Integer(), nullable=False)
    dtb = Column(String(50), nullable=False) #days to birthday
    register_date = Column(String(50), nullable=False)
    register_age = Column(Integer())
    uuid = Column(String(256))
    username = Column(String())
    password = Column(String())
    pass_strength = Column(Integer())
    salt = Column(String())
    md5 = Column(String())
    sha1 = Column(String())
    sha256 = Column(String())
    email = Column(String(), nullable=False)
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

