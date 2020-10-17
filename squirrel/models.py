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
    
    Hectare = models.CharField(
        max_length=100,
        help_text=_('Hectare'),
)

    Shift = models.CharField(
        max_length=100,
        help_text=_('Shift'),
)

    Date = models.CharField(
        max_length=100,
        help_text=_('Date'),
)
    Hectare_Squirrel_Number = models.CharField(
        max_length=100,
        help_text=_('Hectare Squirrel Number'),
)
    Age = models.CharField(
        max_length=100,
        help_text=_('Age'),
        blank=True,
)
    Primary_Fur_Color = models.CharField(
        max_length=100,
        help_text=_('Primary Fur Color'),
        blank=True,
)
    Highlight_Fur_Color = models.CharField(
        max_length=100,
        help_text=_('Highlight Fur Color'),
        blank=True,
)
    Combination_of_Primary_and_Highlight_Color = models.CharField(
        max_length=100,
        help_text=_('Combination of Primary and Highlight Color'),
)

    Color_notes = models.CharField(
        max_length=100,
        help_text=_('Color notes'),
        blank=True,
)

    Location = models.CharField(
        max_length=100,
        help_text=_('Location'),
        blank=True,
)

    Above_Ground_Sighter_Measurement = models.CharField(
        max_length=100,
        help_text=_('Above Ground Sighter Measurement'),
        blank=True,
)

    Specific_Location = models.CharField(
        max_length=100,
        help_text=_('Specific Location'),
        blank=True,
)
    
    Running = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is running'),
)

    Chasing = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is chasing'),
)

    Climbing = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is climbing'),
)

    Eating = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is eating'),
)

    Foraging = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is foraging'),
)

    Other_Activities = models.CharField(
        max_length=100,
        help_text=_('Other Activities'),
        blank=True,
)

    Kuks = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is kuks'),
)

    Quaas = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is quaas'),
)

    Moans = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is moans'),
)

    Tail_flags = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is tail flags'),
)

    Tail_twitches = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is tail twitches'),
)

    Approaches = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is approaches'),
)

    Indifferent = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is indiferent'),
)

    Runs_from = models.CharField(
        max_length=100,
        help_text=_('Whether or not squirrel is runs from'),
)

    Other_interactions = models.CharField(
        max_length=100,
        help_text=_('Other interactions'),
        blank=True,
)

    Lat_Long = models.CharField(
        max_length=100,
        help_text=_('Lat/Long'),
)

    def __str__(self):
        return self.name

# Create your models here.
