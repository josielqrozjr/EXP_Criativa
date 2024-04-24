from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import database_exists, create_database
from flask_sqlalchemy import create_engine
from flask_sqlalchemy import Session


db= SQLAlchemy()

bd_name = "TesteRA3"
password = "2n#*uB?w!r_O"

instance = f"mysql+pymysql://root:{password}@localhost:3306/{bd_name}"

if not database_exists(url=instance):
    create_database(url=instance)

engine = create_engine(url=instance, echo=True)
connection = Session(bind=engine, autocommit=False, autoflush=True)