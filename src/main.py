from connection import session
from pathlib import Path

def create_person():
  from datetime import datetime
  from models import Person
  from extract import ExtractorExcel
  
  # person = Person(address='Antananarivo', birthdate=datetime(1990, 1, 1))
  # session.add(person)
  # session.commit()
  excel_path = Path(__file__).resolve().parent / "excel" / "data.xlsx"
  extractor = ExtractorExcel(str(excel_path))
  extractor.save()
  
def voir_transaction():
  from models import Person
  
  persons = session.query(Person).all()
  for person in persons:
    print(f'ID: {person.id}, Address: {person.address}, Birthdate: {person.birthdate}')
    
voir_transaction()
create_person()