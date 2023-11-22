from faker import Faker

fake = Faker('ko-KR')
print(fake.name())
print(fake.address())
print(fake.text())
print(fake.catch_phrase())
