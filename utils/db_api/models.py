from sqlalchemy.orm import relationship

from datetime import datetime
from distutils.sysconfig import get_makefile_filename
from sqlalchemy import (
    Column, BigInteger, 
    String, Integer, 
    DateTime, Text, ForeignKey
    )

from utils.db_api.base import Base


class User(Base):
    __tablename__ = "user"

    user_id = Column(BigInteger, primary_key=True, unique=True, autoincrement=False)
    username = Column(String(50))
    first_name = Column(String(50))
    last_name = Column(String(50))


class School(Base):
    __tablename__ = "school"

    id = Column(Integer, primary_key=True)
    nomlar = Column(Text)
    malumot = Column(Text)
    rahbariyat = Column(String(150))
    yonalish = Column(String(150))
    qabul = Column(String(150))
    savollar = Column(Text)
    boglanish = Column(String(150))


class College(Base):
    __tablename__ = "college"

    id = Column(Integer, primary_key=True)
    nomlar = Column(Text)
    malumot = Column(Text)
    rahbariyat = Column(String(150))
    yonalish = Column(String(150))
    qabul = Column(String(150))
    savollar = Column(Text)
    boglanish = Column(String(150))


class Texnikum(Base):
    __tablename__ = "texnikum"

    id = Column(Integer, primary_key=True)
    nomlar = Column(Text)
    malumot = Column(Text)
    rahbariyat = Column(String(150))
    yonalish = Column(String(150))
    qabul = Column(String(150))
    savollar = Column(Text)
    boglanish = Column(String(150))


class Lyceum(Base):
    __tablename__ = "lyceum"

    id = Column(Integer, primary_key=True)
    nomlar = Column(Text)
    malumot = Column(Text)
    rahbariyat = Column(String(150))
    yonalish = Column(String(150))
    qabul = Column(String(150))
    savollar = Column(Text)
    boglanish = Column(String(150))
