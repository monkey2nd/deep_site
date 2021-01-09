from django.db import models
from django import forms
from django.conf import Settings
from django.utils import timezone
# Create your models here.

class Check_photo(models.Model):
    picture = models.ImageField(upload_to = 'images/')
    title = forms.ChoiceField(
        choices=(
            ('cat','猫'),
            ('dog','犬'),
            ('vihicle','乗り物')
        )
    )
    published_date = models.DateTimeField(blank = True,null = True)
    def vote(self):
        self.published_date = timezone.now()
        self.save()
    
    def __str__(self):
        return self.title