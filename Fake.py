from faker import Faker

fake = Faker()

print("Name:", fake.name())
print("Email:", fake.email())
phone_number = fake.phone_number()
print("Phone_number:",fake.phone_number())