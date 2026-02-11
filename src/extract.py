import pandas as pd
from connection import session
from models import Person

class ExtractorExcel:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.data = None

    def extract(self) -> pd.DataFrame:
        self.data = pd.read_excel(self.file_path)
      
    def save(self):
        self.extract()
        for index, row in self.data.iterrows():
            # print(f"Row {index}: {row.to_dict()}")
            person = Person(nom=row['nom'], adresse=row['adresse'], date_naissance=row['date_naissance'])
            session.add(person)
            session.commit()