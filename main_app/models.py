from django.db import models
from django.urls import reverse


# Create your models here.


SEASONS = (
    ('SUM','Summer'),
    ('SPG','Spring'),
    ('FLL','Fall'),
    ('WIN','Winter')
)
SEASONZ = (
    ('SUM','Summer'),
    ('SPG','Spring'),
    ('FLL','Fall'),
    ('WIN','Winter'),
    ('NAN','None'),
)
TYPE = (
    ('Tree','Tree'),
    ('Shrub','Shrub'),
    ('Vine','Vine'),
    ('Perin','Perineal'),
    ('Palm','Palm'),
    ('Annuals','Annuals'),
)
class Plant(models.Model):  # Note that parens are optional if not inheriting from another class
    name = models.CharField(max_length=100)
    scientific_name = models.CharField(max_length=100)
    type = models.CharField(
        max_length=15,
        choices=TYPE,
        default= TYPE[0][0],)
    bloom_season = models.CharField(
        max_length=3,
        choices=SEASONS,
        default= SEASONS[0][0],)
    trim_season = models.CharField(
        max_length=3,
        choices=SEASONZ,
        default= SEASONZ[0][0],)
    description = models.CharField(max_length=100)
    height = models.CharField(max_length=100)
    spread = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'plant_id': self.id})

