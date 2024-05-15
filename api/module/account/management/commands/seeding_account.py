
from django.core.management.base import BaseCommand
from module.account.models import User
from django.db import transaction




class Command(BaseCommand):
    help = "seeding_account"

    @transaction.atomic
    def handle(self, *args, **options):
        print("Starting seeding account...")
        user = User.objects.create_user(username="root", email="root@localhost", first_name="hoang", last_name="luong", password="1181080029")
        user.is_staff = True
        user.is_superuser = True
        user.save()
        print("Seeded account successfully !")
        print("--------------------------------")
        print("Starting seeding account d3 repository...")


        
    
