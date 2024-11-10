from project.customer import Customer
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str) -> None:
        self.name = name
        self.customers: list[Customer] = []
        self.dvd: list[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer) -> None:
        capacity = MovieWorld.customer_capacity()
        if len(self.customers) < capacity:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        capacity = MovieWorld.dvd_capacity()
        if len(self.dvd) < capacity:
            if len(self.dvd) < capacity:
                self.dvd.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = [c.__dict__ for c in self.customers if c.__dict__['id'] == customer_id][0]
        dvd = [d.__dict__ for d in self.dvd if d.__dict__['id'] == dvd_id][0]
        # return customer
        if dvd['name'] in customer['rented_dvd']:
            return f"{customer['name']} has already rented {dvd['name']}"
        if dvd['is_Rented']:
            return "DVD is already rented"
        if customer['age'] < dvd['age_restriction']:
            return f"{customer['name']} should be at least {dvd['age_restriction']} to rent this movie"

        dvd['is_Rented'] = True
        customer['rented_dvd'].append(dvd['name'])
        return f"{customer['name']} has successfully rented {dvd['name']}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [c.__dict__ for c in self.customers if c.__dict__['id'] == customer_id][0]
        dvd = [d.__dict__ for d in self.dvd if d.__dict__['id'] == dvd_id][0]

        if dvd['name'] in customer['rented_dvd']:
            customer['rented_dvd'].remove(dvd['name'])
            return f"{customer['name']} has successfully returned"
        return f"{customer['name']} does not have that DVD"

    def __repr__(self):
        result = ''
        for cus in self.customers:
            result += repr(cus) + '\n'
        for dvd in self.dvd:
            result += repr(dvd) + '\n'
        return result.strip()


from project.customer import Customer
from project.dvd import DVD
from project.movie_world import MovieWorld

import unittest


class TestsMovieWorld(unittest.TestCase):
    def test_customer_init(self):
        c = Customer("Pesho", 22, 1)
        self.assertEqual(c.name, "Pesho")
        self.assertEqual(c.age, 22)
        self.assertEqual(c.id, 1)

    def test_customer_repr(self):
        c = Customer("Pesho", 22, 1)
        self.assertEqual(repr(c), "1: Pesho of age 22 has 0 rented DVD's ()")

    def test_dvd_init(self):
        dvd = DVD("B", 1, 2020, "January", 10)
        self.assertEqual(dvd.name, "B")
        self.assertEqual(dvd.id, 1)
        self.assertEqual(dvd.creation_month, "January")
        self.assertEqual(dvd.creation_year, 2020)
        self.assertEqual(dvd.age_restriction, 10)
        self.assertEqual(dvd.is_rented, False)

    def test_dvd_class_method(self):
        dvd = DVD.from_date(1, "A", "16.10.1997", 18)
        self.assertEqual(dvd.name, "A")
        self.assertEqual(dvd.id, 1)
        self.assertEqual(dvd.creation_month, "October")
        self.assertEqual(dvd.creation_year, 1997)
        self.assertEqual(dvd.age_restriction, 18)
        self.assertEqual(dvd.is_rented, False)

    def test_dvd_repr(self):
        dvd = DVD.from_date(1, "A", "16.10.1997", 18)
        self.assertEqual(repr(dvd), "1: A (October 1997) has age restriction 18. Status: not rented")

    def test_movie_init(self):
        movie = MovieWorld("Test")
        self.assertEqual(movie.name, "Test")
        self.assertEqual(movie.customers, [])
        self.assertEqual(movie.dvds, [])

    def tests_movie_world_dvd_capacity(self):
        self.assertEqual(MovieWorld.dvd_capacity(), 15)

    def tests_movie_world_customer_capacity(self):
        self.assertEqual(MovieWorld.customer_capacity(), 10)

    def test_movie_world_add_customer_success(self):
        movie_world = MovieWorld("Test")
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        self.assertEqual(movie_world.customers, [c])

    def test_movie_world_add_customer_overflow(self):
        movie_world = MovieWorld("Test")
        for _ in range(11):
            movie_world.add_customer(Customer("Pesho", 20, 4))
        self.assertEqual(len(movie_world.customers), 10)

    def test_movie_world_add_dvd_success(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        movie_world.add_dvd(d)
        self.assertEqual(movie_world.dvds, [d])

    def test_movie_world_add_dvd_overflow(self):
        movie_world = MovieWorld("Test")
        for _ in range(16):
            movie_world.add_dvd(DVD("A", 1, 1254, "February", 10))
        self.assertEqual(len(movie_world.dvds), 15)

    def test_movie_world_rent_dvd_already_rented(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        c2 = Customer("Gosho", 26, 2)
        movie_world.add_customer(c)
        movie_world.add_customer(c2)
        movie_world.add_dvd(d)
        movie_world.rent_dvd(4, 1)
        result = movie_world.rent_dvd(2, 1)
        self.assertEqual(result, "DVD is already rented")

    def test_movie_world_rent_dvd_already_rented_by_user(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        movie_world.rent_dvd(4, 1)
        result = movie_world.rent_dvd(4, 1)
        self.assertEqual(result, "Pesho has already rented A")

    def test_movie_world_rent_dvd_no_permision(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 18)
        c = Customer("Pesho", 16, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        result = movie_world.rent_dvd(4, 1)
        self.assertEqual(result, "Pesho should be at least 18 to rent this movie")

    def test_movie_world_rent_dvd_success(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        result = movie_world.rent_dvd(4, 1)
        self.assertEqual(result, "Pesho has successfully rented A")
        self.assertEqual(d.is_rented, True)
        self.assertEqual(c.rented_dvds[0], d)

    def test_movie_world_return_dvd_success(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        movie_world.rent_dvd(4, 1)
        result = movie_world.return_dvd(4, 1)
        self.assertEqual(result, "Pesho has successfully returned A")
        self.assertEqual(c.rented_dvds, [])
        self.assertEqual(d.is_rented, False)

    def test_movie_world_return_dvd_unsuccessful(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        result = movie_world.return_dvd(4, 1)
        self.assertEqual(result, "Pesho does not have that DVD")

    def test_movie_world_repr(self):
        movie_world = MovieWorld("Test")
        d = DVD("A", 1, 1254, "February", 10)
        c = Customer("Pesho", 20, 4)
        movie_world.add_customer(c)
        movie_world.add_dvd(d)
        movie_world.rent_dvd(4, 1)
        actual = repr(movie_world).strip('\n')
        expected = "4: Pesho of age 20 has 1 rented DVD's (A)\n1: A (February 1254) has age restriction 10. Status: rented"
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()