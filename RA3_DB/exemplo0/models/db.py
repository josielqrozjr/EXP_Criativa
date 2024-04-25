from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()

bd_name = "DB_IOT_RA3"
password = "2n#*uB?w!r_O"

instance = f"mysql+pymysql://root:{password}@localhost:3306/{bd_name}"
