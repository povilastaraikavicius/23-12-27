from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from LAlchemy import Projektas

engine = create_engine("sqlite:///projektai.db")
Session = sessionmaker(bind=engine)
session = Session()

# 1budas


# projektas1 = session.query(Projektas).get(1)
# projektas1.price = 22000
# session.commit()


# 2budas


projektas2 = session.query(Projektas).filter_by(name="2 projektas").one()
projektas2.name = "2 projektas tikrai"
session.commit()


