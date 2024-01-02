from sqlalchemy import Column, Integer, String, Float, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///one2many_test.db")
Base = declarative_base()


class Tevas(Base):
    __tablename__ = "tevas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    vaikai = relationship("Vaikas", back_populates="tevas")


class Vaikas(Base):
    __tablename__ = "vaikas"
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavardė", String)
    mokymo_istaiga = Column("Mokymo įskaita", String)
    tevas_id = Column(Integer, ForeignKey("tevas.id"))
    tevas = relationship("Tevas", back_populates="vaikai")


Base.metadata.create_all(engine)


Session = sessionmaker(bind=engine)
session = Session()


vaikas = Vaikas(vardas="Vaikas", pavarde="Vaikaitis")
vaikas2 = Vaikas(vardas="Vaikas 2", pavarde="Vaikaitis 2")
tevas = Tevas(vardas="Tevas", pavarde="Vaikaitis")
tevas.vaikai.append(vaikas)
tevas.vaikai.append(vaikas2)
session.add(tevas)
session.commit()
