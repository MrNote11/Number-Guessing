from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from game.models import Profile

class Command(BaseCommand):
    help = 'Create missing profiles for existing users'

    def handle(self, *args, **kwargs):
        users_without_profiles = User.objects.filter(profile__isnull=True)
        
        if not users_without_profiles.exists():
            self.stdout.write(self.style.SUCCESS('All users already have profiles.'))
            return
        
        for user in users_without_profiles:
            if not hasattr(user, 'profile'):  # Double check user has no profile
                Profile.objects.create(user=user)
                self.stdout.write(self.style.SUCCESS(f'Created profile for user: {user.username}'))
