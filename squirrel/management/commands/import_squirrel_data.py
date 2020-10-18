import csv

import datetime

from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

class Command(BaseCommand):
    help = 'import data from squirrel census file'

    def add_arguments(self, parser):
        parser.add_argument('file_', help='file containing squirrel data')

    def handle(self, *args, **options):
        file_ = options['squirrel_file']

        with open(file_) as fp:
            reader = csv.DictReader(fp)
            data = list(reader)

            for obs in data:
                inst = Squirrel(
                        X = obs['X'],
                        Y = obs['Y'],
                        Unique_Squirrel_ID = obs['Unique Squirrel ID'],
                        Shift = obs['Shift'],
                        Date = obs['Date'],
                        Age = obs['Age'],
                        Primary_fur_color = obs['Primary_fur_color'],
                        Location = obs['Location'],
                        Specific_Location = obs['Specific_Location'],
                        Running = obs['Running'],
                        Chasing = obs['Chasing'],
                        Climbing = obs['Climbing'],
                        Eating = obs['Eating'],
                        Foraging = obs['Foraging'],
                        Other_Activities = obs['Other_Activities'],
                        Kuks = obs['Kuks'],
                        Quaas = obs['Quaas'],
                        Moans = obs['Moans'],
                        Tail_flags = obs['Tail_flags'],
                        Tail_twitches = obs['Tail_twitches'],
                        Approaches = obs['Approaches'],
                        Indifferent = obs['Indifferent'],
                        Runs_from = obs['Runs_from'],
                        )
                inst.save()
            msg = f'You are importing from {file_}'
            self.stdout.write(self.style.SUCCESS(msg))
        
        #data = list(reader)
        #print(len(data))
            #for item in reader:
                #obj = Squirrel()
           #     obj.X = item['X']
           #     obj.Y = item['Y']
                
          #      obl.raw_sql('Insert into Squirrel']

                #obj.save()
                #pass

