from faker import Faker
import random
class User:
    fake_ru = Faker('ru_Ru')
    fake_en = Faker('en_US')
    name = fake_ru.first_name()
    last_name = fake_ru.last_name()
    email = fake_en.email()
    address = random.choice(['Москва', 'Московская область']) + ', ' + 'ул. ' + fake_ru.street_name()
    phone = random.randint(10000000000, 99999999999)
    delivery_date_rand = str(random.randint(1, 30)) + '.' + str(random.randint(6, 12)) + '.' + '2023'
    comment = str(fake_ru.text())


