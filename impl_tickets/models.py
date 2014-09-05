from django.db import models
from datetime import datetime
from django.utils import timezone
from south.models import models

class ItemStatus(models.Model):
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.status

class Items(models.Model):
    submitted_by = models.TextField(max_length=2000)
    description = models.TextField(max_length=2000)
    status_customer = models.TextField(max_length=2000)
    status_solvo = models.TextField(max_length=2000)
    date_found = models.DateTimeField('Item registration date', default=timezone.now)
    date_to_fix = models.DateField('Planned fix date', null='true')
    fixed=models.BooleanField(default=False)
    date_fixed = models.DateTimeField('Fix applied date', null='true')
    confirmed = models.BooleanField(default=False)
    date_fix_confirmed = models.DateTimeField('Fix confirmation date', null='true')
    responsible = models.TextField(max_length=2000, null='true')

    def __str__(self):
        return self.description


