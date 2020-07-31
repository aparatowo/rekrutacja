from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__= 'users'

    id = Column(Integer(), primary_key=True, unique=True, autoincrement=True)
    gender = Column(String(50), nullable=False)
    title = Column(String(50), nullable=False)
    first_name = Column(String(256), nullable=False)
    last_name = Column(String(256), nullable=False)
    true_id_name = Column(String(50))
    true_id_value = Column(String(50))
    nat = Column(String(50))
    dob = Column(String(50), nullable=False) #day of birth
    age = Column(Integer(), nullable=False)
    dtb = Column(String(50), nullable=False) #days to birthday
    register_date = Column(String(50), nullable=False)
    registered_at_age = Column(Integer())

    _confidential = relationship("Confidential")
    contact_details = relationship("ContactDetails")
    location = relationship("Location")


class Confidential(Base):
    __tablename__ = 'confidencial'
    id = Column(Integer(), primary_key=True, unique=True)
    user_ID = Column(Integer(), ForeignKey('users.id'))
    id_name = Column(String())
    id_value = Column(String())
    uuid = Column(String())
    username = Column(String())
    password = Column(String())
    pass_strength = Column(Integer())
    salt = Column(String())
    md5 = Column(String())
    sha1 = Column(String())
    sha256 = Column(String())


class ContactDetails(Base):
    __tablename__ = 'contact_details'
    id = Column(Integer(), primary_key=True, unique=True)
    user_ID = Column(Integer(), ForeignKey('users.id'))
    email = Column(String(), nullable=False)
    phone = Column(Integer())
    cellphone = Column(Integer())


class Location(Base):
    __tablename__ = 'location'
    id = Column(Integer(), primary_key=True, unique=True)
    user_ID = Column(Integer(), ForeignKey('users.id'))
    street_name = Column(String())
    home_number = Column(String())
    city = Column(String())
    postcode = Column(String())
    state = Column(String())
    country = Column(String())
    latitude = Column(String())
    longitude = Column(String())
    timezone_offset = Column(String())
    timezone_desc = Column(String())

