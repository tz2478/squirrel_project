import csv

from django.core.management.base import BaseCommand

from squirrel.models import Squirrel

class Command(BaseCommand):
    help = 'Get seeds into pot'

    def add_arguments(self, parser):
        parser.add_argument('seeds_file', help='file containing squirrel data')

    def handle(self, *args, **options):
        file_ = options['seeds_file']

        with open(file_) as fp:
            reader = csv.DictReader(fp)
        
        #data = list(reader)
        #print(len(data))
            for item in reader:
                obj = Squirrel()
           #     obj.X = item['X']
           #     obj.Y = item['Y']
                
          #      obl.raw_sql('Insert into Squirrel']

                obj.save()
                #pass

        msg = f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))

