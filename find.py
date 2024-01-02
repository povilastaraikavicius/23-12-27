from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from LAlchemy import Projektas

engine = create_engine("sqlite:///projektai.db")
Session = sessionmaker(bind=engine)
session = Session()


search = session.query(Projektas).filter(Projektas.name.ilike("2%"))
search2 = session.query(Projektas).filter(Projektas.price > 1000)
search3 = session.query(Projektas).filter(
    Projektas.price > 1000, Projektas.name.ilike("2%")
)

print([i for i in search])
print([i for i in search2])
print([i for i in search3])
