
from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data.'

    def handle(self, *args, **kwargs):
        # Очистити існуючі дані
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Додаємо користувачів
        user1 = User.objects.create(email='alice@example.com', name='Alice', password='alicepass')
        user2 = User.objects.create(email='bob@example.com', name='Bob', password='bobpass')
        user3 = User.objects.create(email='carol@example.com', name='Carol', password='carolpass')

        # Додаємо команди
        team1 = Team.objects.create(name='OctoRunners')
        team2 = Team.objects.create(name='FitSquad')
        team1.members.add(user1, user2)
        team2.members.add(user3)

        # Додаємо активності
        Activity.objects.create(user=user1, activity_type='run', duration=30, points=10, date=timezone.now())
        Activity.objects.create(user=user2, activity_type='walk', duration=60, points=8, date=timezone.now())
        Activity.objects.create(user=user3, activity_type='strength', duration=45, points=12, date=timezone.now())

        # Додаємо лідерборд
        Leaderboard.objects.create(team=team1, total_points=18)
        Leaderboard.objects.create(team=team2, total_points=12)

        # Додаємо тренування
        Workout.objects.create(name='Morning Run', description='Run 3km in the morning', suggested_for='all')
        Workout.objects.create(name='Pushups', description='Do 20 pushups', suggested_for='beginners')
        Workout.objects.create(name='Plank', description='Hold plank for 1 minute', suggested_for='all')

        self.stdout.write(self.style.SUCCESS('Test data successfully populated in octofit_db.'))
