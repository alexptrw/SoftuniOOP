class Zoo:
    def __init__(self, name, budget, animal_capacity, worker_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = worker_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if price > self.__budget and (len(self.animals) + 1) <= self.__animal_capacity:
            return "Not enough budget"
        if price <= self.__budget and (len(self.animals) + 1) > self.__animal_capacity:
            return "Not enough space for animal"
        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if len(self.workers) + 1 > self.__workers_capacity:
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        # if worker_name in self.workers:
        #     self.workers.remove(worker_name)
        worker = next((w for w in self.workers if w.name == worker_name), None)
        # for worker in self.workers:
        #     if worker.name == worker_name:
        #         self.workers.remove(worker)
        if worker:
            self.workers.remove(worker)
            return f"There is no {worker_name} in the zoo"
        return f"{worker_name} fired successfully"

    def pay_workers(self):
        sum_salaries = sum([w.salary for w in self.workers])
        if sum_salaries <= self.__budget:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_care = sum([a.money_for_care for a in self.animals])
        if sum_care <= self.__budget:
            self.__budget -= sum_care
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        lions = []
        tigers = []
        cheetahs = []
        for animal in self.animals:
            if animal.__class__.__name__ == 'Lion':
                lions.append(animal)
            elif animal.__class__.__name__ == 'Tiger':
                tigers.append(animal)
            elif animal.__class__.__name__ == 'Cheetah':
                cheetahs.append(animal)
        result += f'----- {len(lions)} Lions:\n'
        result += "\n".join([lion.__repr__() for lion in lions]) + '\n'
        result += f'----- {len(tigers)} Tigers:\n'
        result += "\n".join([tiger.__repr__() for tiger in tigers]) + '\n'
        result += f'----- {len(cheetahs)} Cheetahs:\n'
        result += "\n".join([cheetah.__repr__() for cheetah in cheetahs]) + '\n'

        return result.strip()

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        keepers = []
        caretakers = []
        vets = []
        for worker in self.workers:
            if worker.__class__.__name__ == 'Keeper':
                keepers.append(worker)
            elif worker.__class__.__name__ == 'Caretaker':
                caretakers.append(worker)
            elif worker.__class__.__name__ == 'Vet':
                vets.append(worker)
        result += f'----- {len(keepers)} Keepers:\n'
        result += "\n".join([keeper.__repr__() for keeper in keepers]) + '\n'
        result += f'----- {len(caretakers)} Caretakers:\n'
        result += "\n".join([caretaker.__repr__() for caretaker in caretakers]) + '\n'
        result += f'----- {len(vets)} Vets:\n'
        result += "\n".join([vet.__repr__() for vet in vets]) + '\n'

        return result.strip()
