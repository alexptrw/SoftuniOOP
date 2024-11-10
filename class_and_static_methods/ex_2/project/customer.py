class Customer:
    def __init__(self, name: str, age: int, id: int) -> None:
        self.name = name
        self.age = age
        self.id = id
        self.rented_dvds = []

    def __repr__(self):
        rented_dvd_names = ', '.join(dvd.name for dvd in self.rented_dvds)
        return f"{self.id}: {self.name} of age {self.age} has " \
               f"{len(self.rented_dvds)} rented DVD's " \
               f"({rented_dvd_names})"
