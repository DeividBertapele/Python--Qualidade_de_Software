from faker import Faker

faker = Faker('pt_BR')

d = {
    'name': faker.name(),
    'city': faker.city(),
    'country': faker.country(),
    
}

#explorar instancia de faker

print(d)