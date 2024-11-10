from datetime import datetime


class DVD:
    def __init__(self, name: str, id: int, creation_year: int, creation_month: str, age_restriction: int) ->None:
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id: int, name: str, date: str, age_restriction: int):
        day, month, year = map(int, date.split('.'))
        date = datetime(year, month, day)
        month = date.strftime("%B")
        return cls(name, id, year, month, age_restriction)

    def __repr__(self) -> str:
        status = 'not rented'
        if self.is_rented:
            status = 'rented'
        return f"{self.id}: {self.name} ({self.creation_month} " \
               f"{self.creation_year}) has age restriction " \
               f"{self.age_restriction}. Status: {status}"

