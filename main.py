# 1. Sukurtų duomenų bazę
# 2. Sukurtų lentelę paskaitos su stulpeliais pavadinimas, destytojas ir trukme
# 3. Sukurkite atskirą skriptą, kuris sugeneruotų įrašus atsitiktinę tvarka. reikia, kad sukurtų 1000 įraššū. Tokių kaip ('Vadyba', 'Domantas', 40), ('Python', 'Donatas', 80) ir ('Java', 'Tomas', 80). studijų trukmė gali būto tarp 200-1000 valandų, suapvalinus iki 100.
# 5. Atspausdintų tik tas paskaitas, kurių trukmė didesnė už 250
# 6. Atnaujintų paskaitos „Python“ pavadinimą į „Python programavimas“
# Ištrintų paskaitą, kurios dėstytojas – „Tomas“
# 7. Atspausdintų visas paskaitas (visą lentelę)

# import sqlite3

# conn = sqlite3.connect("paskaitos.db")
# c = conn.cursor()

# query = """
# CREATE TABLE paskaitos (
#     pavadinimas text,
#     destytojas text,
#     trukme integer
# );
# """

# c.execute(query)
# conn.commit()
# conn.close()


# import sqlite3

# conn = sqlite3.connect("paskaitos.db")
# c = conn.cursor()

# with conn:
#     c.execute("INSERT INTO paskaitos VALUES ('Vadyba', 'Domantas', 40)")

#     c.execute("INSERT INTO paskaitos VALUES ('Python', 'Donatas', 80)")

#     c.execute("INSERT INTO paskaitos VALUES ('Java', 'Tomas', 80)")


# import random
# import sqlite3


# def generate_records():
#     pavadinimas = ["Vadyba", "Python", "Java"]
#     destytojas = [
#         "Domantas",
#         "Donatas",
#         "Tomas",
#         "Povilas",
#         "Andrius",
#         "Jonas",
#         "Saulius",
#         "Vytautas",
#         "Vaclov",
#         "Albert",
#         "Vilius",
#         "Renatas",
#     ]

#     records = []
#     for _ in range(1000):
#         pavadinimas = random.choice(pavadinimas)
#         destytojas = random.choice(destytojas)
#         trukme = round(random.uniform(200, 1000), -2)
#         records.append((pavadinimas, destytojas, trukme))

#     return records


# generated_records = generate_records()

# conn = sqlite3.connect("paskaitos.db")
# c = conn.cursor()

# with conn:
#     c.executemany("INSERT INTO paskaitos VALUES (?, ?, ?)", generated_records)

# conn.close()


# import sqlite3

# conn = sqlite3.connect("paskaitos.db")
# c = conn.cursor()

# with conn:
#     c.execute("SELECT * FROM paskaitos WHERE trukme BETWEEN 500 AND 1000")
#     print(c.fetchall())

# conn.close()







# import sqlite3

# conn = sqlite3.connect("paskaitos.db")
# c = conn.cursor()

# with conn:
#     c.execute(
#         "UPDATE paskaitos SET pavadinimas='Python programavimas' WHERE pavadinimas='Python'"
#     )







