from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@com.com',
            first_name='Admin',
            last_name='Com',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            is_verify=True,
        )

        user.set_password('123456qwerty')
        user.save()
