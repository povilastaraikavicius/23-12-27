from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from task11 import Projektas
from datetime import datetime


def new_input(f_name, l_name, birtt_date, responsibilities, salary, start_work):
    engine = create_engine("sqlite:///darbuotojai.db")
    Session = sessionmaker(bind=engine)
    session = Session()

    darbuotojai = Projektas(
        f_name=f_name,
        l_name=l_name,
        birtt_date=birtt_date,
        responsibilities=responsibilities,
        salary=salary,
        start_work=start_work,
    )

    session.add(darbuotojai)
    session.commit()


f_name = input("Enter first name: ")
l_name = input("Enter last name: ")
dob_str = input("Enter date of birth (YYYY-MM-DD): ")
birtt_date = datetime.strptime(dob_str, "%Y-%m-%d")
responsibilities = input("Enter responsibilities: ")
salary = float(input("Enter salary: "))
start_work = datetime.utcnow().date()

new_input(
    f_name=f_name,
    l_name=l_name,
    birtt_date=birtt_date,
    responsibilities=responsibilities,
    salary=salary,
    start_work=start_work,
)
