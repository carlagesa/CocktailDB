from django.core.management.base import BaseCommand
from django_q.tasks import schedule
from drinks.tasks import fetch_cocktails

class Command(BaseCommand):
    help = 'Schedule the fetch_cocktails task'

    def handle(self, *args, **kwargs):
        schedule(
            'drinks.tasks.fetch_cocktails',
            schedule_type='H',  # hourly
            repeats=-1  # repeat forever
        )
        self.stdout.write(self.style.SUCCESS('Scheduled fetch_cocktails task'))
