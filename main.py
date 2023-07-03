from faker import Faker

def generate_fake_person():
    fake = Faker()
    person = {
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'job': fake.job(),
        'birthdate': fake.date_of_birth().strftime('%Y-%m-%d')
    }
    return person

# Example usage:
person = generate_fake_person()

print("Fake Person Information:")
print("Name:", person['name'])
print("Address:", person['address'])
print("Email:", person['email'])
print("Phone Number:", person['phone_number'])
print("Job:", person['job'])
print("Birthdate:", person['birthdate'])
