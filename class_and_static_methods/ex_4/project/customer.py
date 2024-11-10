from project.cls_id_mixin import ClsIdMixin


class Customer(ClsIdMixin):

    def __init__(self, name: str, address: str, email: str):
        # print(f"Creating new Customer, current counter: {Customer._id_counter}")
        self.name = name
        self.address = address
        self.email = email
        self.id = self.get_next_id()
        self.increment_id()

    def __repr__(self):
        return f"Customer <{self.id}> " \
               f"{self.name}; Address: {self.address};" \
               f" Email: {self.email}"

