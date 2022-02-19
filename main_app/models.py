from django.db import models

# Create your models here.

# Add the Cat class & list and view function below the imports
class Plant:  # Note that parens are optional if not inheriting from another class
    def __init__(self, name, scientific_name, family, bloom_season, trim_season, height, spread, description):
        self.name = name
        self.scientific_name = scientific_name
        self.family = family
        self.bloom_season = bloom_season
        self.trim_season = trim_season
        self.description = description
        self.height = height
        self.spread = spread

plants = [
    Plant('Japanese Maple', 'Acer Palmatum', 'Sapinaceae', 'Sping', None, '15 - 25ft', '10 - 15ft', 'Looks goooood'),
    Plant('Maple', 'Acer Palmatum', 'Sapinaceae', 'Sping', None, '15 - 25ft', '10 - 15ft', 'Looks goooood'),
    Plant('Japanese', 'Acer Palmatum', 'Sapinaceae', 'Sping', None, '15 - 25ft', '10 - 15ft', 'Looks goooood'),
]