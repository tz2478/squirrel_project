from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    X = models.CharField(
	max_length=100,
	help_text=_('X'),
)

    Y = models.CharField(
        max_length=100,
        help_text=_('Y'),
)

    Unique_Squirrel_ID = models.CharField(
        max_length=100,
	help_text=_('Unique Squirrel ID'),
)
    
    AM = 'AM'
    PM = 'PM'
    Shift_choice = [
            (AM, 'AM'),
            (PM, 'PM'),
    ]

    Shift = models.CharField(
        max_length=100,
        choices = Shift_choice,
        help_text=_('Shift'),
        default=AM,
)

    Date = models.CharField(
        max_length=100, 
        help_text=_('Date'),
)

    Juvenile='Juvenile'
    Adult='Adult'
    Other='Other'
    Age_choice = [
            (Juvenile,'Juvenile'),
            (Adult,'Adult'),
            (Other,'Other'),
    ]

    Age = models.CharField(
        max_length=100,
        help_text=_('Age'),
        choices = Age_choice,
        default = Juvenile,
        blank=True,
)
    
    Black='Black'
    Cinnamon='Cinnamon'
    Gray='Gray'
    Other='Other'
    Color_choice = [
            (Black,'Black'),
            (Cinnamon,'Cinnamon'),
            (Gray,'Gray'),
            (Other,'Other'),
    ]

    Primary_Fur_Color = models.CharField(
        max_length=100,
        help_text=_('Primary Fur Color'),
        choices = Color_choice,
        default = Other,
        blank=True,
)

    Above_Ground='Above_Ground'
    Ground_Plane='Ground_Plane'
    Other='Other'
    Location_choice = [
            (Above_Ground,'Above_Ground'),
            (Ground_Plane,'Ground_Plane'),
            (Other,'Other'),
    ]

    Location = models.CharField(
        max_length=100,
        help_text=_('Location'),
        choices = Location_choice,
        default = Other,
        blank=True,
)

    Specific_Location = models.CharField(
        max_length=100,
        help_text=_('Specific Location'),
        blank=True,
)
    
    Running = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is running'),
)

    Chasing = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is chasing'),
)

    Climbing = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is climbing'),
)

    Eating = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is eating'),
)

    Foraging = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is foraging'),
)

    Other_Activities = models.CharField(
        max_length=100,
        help_text=_('Other Activities'),
        blank=True,
)

    Kuks = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is kuks'),
)

    Quaas = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is quaas'),
)

    Moans = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is moans'),
)

    Tail_flags = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is tail flags'),
)

    Tail_twitches = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is tail twitches'),
)

    Approaches = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is approaches'),
)

    Indifferent = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is indiferent'),
)

    Runs_from = models.BooleanField(
        default = False,
        help_text=_('Whether or not squirrel is runs from'),
)

    def __str__(self):
        return self.Unique_Squirrel_ID

# Create your models here.
