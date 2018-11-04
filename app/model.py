# import sqlalchemy
from sqlalchemy import (Column,
                        Integer,
                        String,
                        ForeignKey,
                        DateTime,
                        Float,
                        Boolean,
                        create_engine)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql import func
# from passlib.apps import postgres_context as pwd_context
from passlib.apps import custom_app_context as pwd_context

base = declarative_base()


class Admin(base):
    __tablename__ = 'admin'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(20), nullable=False, unique=True)
    password = Column(String(200))

    """convert password to hashed password"""
    def hash_password(self, password):
        self.password = pwd_context.encrypt(password)

    """verify entered password against hashed password """
    def verify_password(self, password):
        return pwd_context.verify(password, self.password)


class Basic(base):
    """Basic class contains basic site info """
    __tablename__ = 'basic'
    id = Column(Integer, primary_key=True)
    mission = Column(String, nullable=False)
    vision = Column(String, nullable=False)
    values = Column(String, nullable=False)
    certification_name = Column(String, nullable=False)
    certification_url = Column(String, nullable=False)


class Contact_info(base):
    """contact_info class contains the company contacts Info"""
    __tablename__ = 'contact_info'
    id = Column(Integer, primary_key=True)
    address = Column(String(150), nullable=False)
    email = Column(String(150), nullable=False)
    phone = Column(String(20), nullable=False)
    fax = Column(String(20), nullable=False)
    mobile = Column(String(20), nullable=False)


class Career(base):
    """Career class contains careers posted """
    __tablename__ = 'career'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    date = Column(DateTime(timezone=True), server_default=func.now())


class Project(base):
    """Project class contains projects constructed by the company"""
    __tablename__ = 'projects'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    role = Column(String(64), nullable=False)
    location = Column(String(64), nullable=False)
    area = Column(String(64), nullable=False)
    status = Column(String(64), nullable=False)
    project_images = relationship("Project_images", cascade="all,delete", backref="Project")


class Project_images(base):
    __tablename__ = 'project_images'
    id = Column(Integer, primary_key=True)
    project_id = Column(Integer, ForeignKey('projects.id'))
    img_url = Column(String, nullable=False)



class Client(base):
    """clients of the company"""
    __tablename__ = 'clients'
    id = Column(Integer, primary_key=True)
    logo = Column(String, nullable=False)
    url = Column(String, nullable=False)


class Letters(base):
    __tablename__ = 'letters'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)


class About(base):
    __tablename__ = 'about'
    id = Column(Integer, primary_key=True)
    history = Column(String, nullable=False)
    iso_description = Column(String, nullable=False)
    iso_name = Column(String, nullable=False)
    iso_url = Column(String, nullable=False)
    ohsas_description = Column(String, nullable=False)
    ohsas_name = Column(String, nullable=False)
    ohsas_url = Column(String, nullable=False)
    code_of_conduct_name = Column(String, nullable=False)
    code_of_conduct_url = Column(String, nullable=False)
    brochure_name = Column(String, nullable=False)
    brochure_url = Column(String, nullable=False)


engine = create_engine('sqlite:///database.db')
base.metadata.create_all(engine)
