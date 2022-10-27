from django.core.management.base import BaseCommand, CommandError
from core.services.hackernews_engine import HackerNewsEngine

class Command(BaseCommand):
    help = 'Syncs with hacker news api, to fetch items'

    def handle(self, *args, **options):
        try:
            engine = HackerNewsEngine()
            engine.run()
        except Exception:
            self.stdout.write(self.style.ERROR('Failed to sync.'))
            return

        self.stdout.write(self.style.SUCCESS('Successfully synced'))
        return