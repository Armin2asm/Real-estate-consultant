from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):

    PROPERTY_TYPES = [  ('residential', 'Residential'), ('commercial', 'Commercial'),   ('villa', 'Villa'),  ('land', 'Land'), ('office', 'Office'),   ('shop', 'Shop')  ]

    TRANSACTION_TYPES = [    ('sale', 'Sale'),   ('rent', 'Rent'),  ('mortgage', 'Mortgage'),('mortgage_rent', 'Mortgage & Rent')    ]

    owner = models.ForeignKey(     User,   on_delete=models.CASCADE,    related_name="properties",   null=True,blank=True   )

    title = models.CharField(max_length=200)

    property_type = models.CharField(    choices=PROPERTY_TYPES )

    transaction_type = models.CharField(   max_length=20,     choices=TRANSACTION_TYPES  )

    owner_name = models.CharField(max_length=100)

    owner_phone = models.CharField(max_length=20)

    city = models.CharField(max_length=100)

    address = models.TextField()

    area = models.PositiveIntegerField(help_text="Square meters")

    bedrooms = models.PositiveIntegerField(default=0)

    bathrooms = models.PositiveIntegerField(default=1)

    floor = models.PositiveIntegerField(null=True, blank=True)

    year_built = models.PositiveIntegerField(null=True, blank=True)

    parking = models.BooleanField(default=False)

    elevator = models.BooleanField(default=False)

    storage_room = models.BooleanField(default=False)

    sale_price = models.BigIntegerField(null=True, blank=True)

    mortgage_price = models.BigIntegerField(null=True, blank=True)

    rent_price = models.BigIntegerField(null=True, blank=True)

    description = models.TextField(blank=True)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):

    property = models.ForeignKey(    Property,     on_delete=models.CASCADE,    related_name='images'  )

    image = models.ImageField(upload_to='properties/')

    def __str__(self):
        return self.property.title