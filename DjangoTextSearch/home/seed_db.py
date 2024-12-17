from home.models import *
from faker import Faker
import random
fake = Faker('en_IN')




def dbSeeder(records = 10)->None:
    college_names = ['IIT', 'MIT', 'NIT', 'VIT', 'SRM', 'RMV', 'IIIT', 'BITS', 'LIT', 'KIT']
    for name in college_names:
        address = fake.address()
        College.objects.create(
            college_name=name,
            college_address=address
        )
def dbSeeder2(records=10) -> None:
    colleges = list(College.objects.all())  # Convert queryset to a list for indexing
    
    for _ in range(records):
        college = random.choice(colleges)  # Randomly select a college
        gender_choice = random.choice(['Male', 'Female'])
        name = fake.name()
        mobile_number = fake.msisdn()[:10]  # Limit to 10 digits or as per your model's max_length
        email = fake.email()
        age = random.randint(18, 25)
        student_bio = fake.text()

        Student.objects.create(
            college=college,
            name=name,
            mobile_number=mobile_number,
            email=email,
            gender=gender_choice,
            age=age,
            student_bio=student_bio,
        )