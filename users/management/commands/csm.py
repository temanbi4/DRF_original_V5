from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Кастомная команда для создания модератора"""

    def handle(self, *args, **kwargs):
        user = User.objects.create(email='moderator@moderator.moderator',
                                   first_name='moderator',
                                   last_name='moderator',
                                   is_staff=True,
                                   is_superuser=True)

        user.set_password('moderator')
        user.save()