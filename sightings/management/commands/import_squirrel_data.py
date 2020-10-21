import csv

from django.core.management.base import BaseCommand

from sightings.models import Squirrel

class Command(BaseCommand):
    help = 'import data from squirrel census file'

    def add_arguments(self, parser):
        parser.add_argument('file_', help='file containing squirrel data')

    def handle(self, *args, **options):
        Squirrel.objects.all().delete()
        file_ = options['file_']
        with open(file_) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)
            
            def toBoolean(string):
                if str(string).lower() == 'true':
                    return True
                elif str(string).lower() == 'false':
                    return False

            for obs in data:
                inst = Squirrel(
                        X = obs['X'],
                        Y = obs['Y'],
                        Unique_Squirrel_ID = obs['Unique Squirrel ID'],
                        Shift = obs['Shift'],
                        Date = obs['Date'],
                        Age = obs['Age'],
                        Primary_Fur_Color = obs['Primary Fur Color'],
                        Location = obs['Location'],
                        Specific_Location = obs['Specific Location'],
                        Running = toBoolean(obs['Running']),
                        Chasing = toBoolean(obs['Chasing']),
                        Climbing = toBoolean(obs['Climbing']),
                        Eating = toBoolean(obs['Eating']),
                        Foraging = toBoolean(obs['Foraging']),
                        Other_Activities = obs['Other Activities'],
                        Kuks = toBoolean(obs['Kuks']),
                        Quaas = toBoolean(obs['Quaas']),
                        Moans = toBoolean(obs['Moans']),
                        Tail_flags = toBoolean(obs['Tail flags']),
                        Tail_twitches = toBoolean(obs['Tail twitches']),
                        Approaches = toBoolean(obs['Approaches']),
                        Indifferent = toBoolean(obs['Indifferent']),
                        Runs_from = toBoolean(obs['Runs from']),
                        )
                inst.save()
            msg = f'You are importing from {file_}'
            self.stdout.write(self.style.SUCCESS(msg))

