Session = sessionmaker(bind=engine)
session = Session()


vaikas = Vaikas(vardas="Vaikas", pavarde="Vaikaitis")
vaikas2 = Vaikas(vardas="Vaikas 2", pavarde="Vaikaitis 2")
tevas = Tevas(vardas="Tevas", pavarde="Vaikaitis")
tevas.vaikai.append(vaikas)
tevas.vaikai.append(vaikas2)
session.add(tevas)
session.commit()