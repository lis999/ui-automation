import random

from data.data import Person
from faker import Faker

fake = Faker()
Faker.seed()


def generated_person():
    yield Person(
        full_name=fake.first_name() + " " + fake.last_name(),
        firstname=fake.first_name(),
        lastname=fake.last_name(),
        age=random.randint(10, 80),
        salary=random.randint(60000, 110000),
        department=fake.job(),
        email=fake.email(),
        current_address=fake.address(),
        permanent_address=fake.address(),
    )
