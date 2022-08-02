import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','footprints.settings')

import django

django.setup()

from todolist_app.models import *
from faker import Faker
from random import randint

fake = Faker()

def populate(n):

    for i in range(n):
        try:
            fake_task = fake.first_name()
            fake_status = fake.boolean()

            fake_tasks = TodoList.objects.get_or_create(task =fake_task, done = fake_status)

        except: 
            print("Failed")
        else:
            print("Done!")

    

populate(30)