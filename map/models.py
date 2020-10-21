from django.db import models
from django.utils.translation import gettext as _


class Map(models.Model):
    X = models.CharField(
	max_length=100,
	help_text=_('X'),
)

    Y = models.CharField(
        max_length=100,
        help_text=_('Y'),
)
# Create your models here.
