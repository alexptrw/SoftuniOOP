from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo

from project.caretaker import Caretaker
from project.cheetah import Cheetah
from project.keeper import Keeper
from project.lion import Lion
from project.tiger import Tiger
from project.vet import Vet
from project.zoo import Zoo


zoo = Zoo("Zootopia", 3000, 5, 8)

# Animals creation
animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]

# Animal prices
prices = [200, 190, 204, 156, 211, 140]

# Workers creation
workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]

# Adding all animals
for i in range(len(animals)):
    animal = animals[i]
    price = prices[i]
    (zoo.add_animal(animal, price))

# Adding all workers
for worker in workers:
    zoo.hire_worker(worker)

result = []
lions = []
tigers = []
cheetahs = []
for animal in zoo.animals:
    print(animal)
    if animal.__class__.__name__ == 'Lion':
        lions.append(animal)
    elif animal.__class__.__name__ == 'Tiger':
        tigers.append(animal)
    elif animal.__class__.__name__ == 'Cheetah':
        cheetahs.append(animal)

result.append(f"You have {len(zoo.animals)} animals")
result.append(f'{len(lions)} Lions')
result.extend(lions)
result.append(f'{len(tigers)} Lions')
result.append(tigers)

for row in result:
    print(row)



