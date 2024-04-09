import django
import os
from polls.models import Question
from faker import Faker
import random

# Tạo một đối tượng Faker
faker = Faker()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', './DjangoProject/settings.py')
django.setup()

# Tạo dữ liệu giả cho model Question
for _ in range(10):
    question = Question(
        question_text=faker.sentence(),
        option_one=faker.word(),
        option_two=faker.word(),
        option_three=faker.word()
    )
    question.save()
