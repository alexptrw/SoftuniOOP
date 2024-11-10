from project.customer import Customer
from project.dvd import DVD
from project.movie_world import MovieWorld


movie_world = MovieWorld("Test")
d = DVD("A", 1, 1254, "February", 10)
c = Customer("Pesho", 20, 4)
movie_world.add_customer(c)
movie_world.add_dvd(d)
result = movie_world.rent_dvd(4, 1)
print(c.rented_dvds[0])