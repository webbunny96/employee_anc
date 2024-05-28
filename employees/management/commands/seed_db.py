from django.core.management.base import BaseCommand
from django_seed import Seed
from employees.models import Employee
import random

class Command(BaseCommand):
    help = "Seed db with employee date"

    def handle(self, *args, **kwargs):
        seeder = Seed.seeder()
        seeder.add_entity(Employee, 50000, {
            'full_name': lambda x: seeder.faker.name(),
            'position': lambda x: random.choice(['Regional manager', 'District manager', 'Marketing', 'Pharmacist', 'Accountant', 'Dispenser' ]),
            'hire_date': lambda x: seeder.faker.date_this_decade(),
            'email': lambda x: seeder.faker.email(),
            'manager': None
        })
        inserted_pks = seeder.execute()
        employees = list(Employee.objects.all())
        for employee in employees:
            if random.choice([True, False]):
                employee.manager = random.choice(employees)
                employee.save()
        self.stdout.write(self.style.SUCCESS('DB seeded successfully!'))