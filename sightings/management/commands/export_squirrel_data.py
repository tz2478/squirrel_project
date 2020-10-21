import csv

from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

class Command(BaseCommand):
    help = 'export data in csv format'

    def add_arguments(self, parser):
        parser.add_argument('file_', help = 'path of the file containing squirrel')

    def handle(self, *args, **options):
        file_ = options['file_']
        obj = Squirrel.objects.all()
        with open(file_, "w") as fp:
            writer = csv.DictWriter(fp, delimiter = ',', fieldnames = ['X','Y','Unique Squirrel ID','Shift','Date','Age','Primary Fur Color','Location','Specific Location','Running','Chasing','Climbing','Eating','Foraging','Other Activities','Kuks','Quaas','Moans','Tail flags','Tail twitches','Approaches','Indifferent','Runs from'])
            writer.writeheader()

            for inst in obj:
                writer.writerow({
                    'X':inst.X,
                    'Y':inst.Y,
                    'Unique Squirrel ID':inst.Unique_Squirrel_ID,
                    'Shift':inst.Shift,
                    'Date':inst.Date,
                    'Age':inst.Age,
                    'Primary Fur Color':inst.Primary_Fur_Color,
                    'Location':inst.Location,
                    'Specific Location':inst.Specific_Location,
                    'Running':inst.Running,
                    'Chasing':inst.Chasing,
                    'Climbing':inst.Climbing,
                    'Eating':inst.Eating,
                    'Foraging':inst.Foraging,
                    'Other Activities':inst.Other_Activities,
                    'Kuks':inst.Kuks,
                    'Quaas':inst.Quaas,
                    'Moans':inst.Moans,
                    'Tail flags':inst.Tail_flags,
                    'Tail twitches':inst.Tail_twitches,
                    'Approaches':inst.Approaches,
                    'Indifferent':inst.Indifferent,
                    'Runs from':inst.Runs_from,
                    })


