import csv

from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

class Command(BaseCommand):
    help = 'export data in csv format'

    def add_arguments(self, parser):
        parser.add_argument('file_', help = 'path of the file containing squirrel')

    def handle(self, *args, **options):
        file_ = options['file_']

        output = {}
        obj = Squirrel.objects.all()

        with open(file_, "w") as fp:
            for inst in obj:
                output['X'] = inst.X
                output['Y'] = inst.Y
                output['Unique Squirrel ID'] = inst.Unique_Squirrel_ID 
                output['Shift'] = inst.Shift
                output['Date'] = inst.Date
                output['Age'] = inst.Age
                output['Primary Fur Color'] = inst.Primary_Fur_Color
                output['Location'] = inst.Location
                output['Specific Location'] = inst.Specific_Location
                output['Running'] = inst.Running
                output['Chasing'] = inst.Chasing
                output['Climbing'] = inst.Climbing
                output['Eating'] = inst.Eating
                output['Foraging'] = inst.Foraging
                output['Other Activities'] = inst.Other_Activities
                output['Kuks'] = inst.Kuks
                output['Quaas'] = inst.Quaas
                output['Moans'] = inst.Moans
                output['Tail flags'] = inst.Tail_flags
                output['Tail twitches'] = inst.Tail_twitches
                output['Approaches'] = inst.Approaches
                output['Indifferent'] = inst.Indifferent
                output['Runs from'] = inst.Runs_from

                write_squirrel = csv.DictWriter(fp, delimiter = ',', fieldnames = output.keys())

                write_squirrel.writeheader()
                write_squirrel.writerow(output)


