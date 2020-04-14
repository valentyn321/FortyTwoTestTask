from django.db import models


class Developer(models.Model):
    name = models.CharField(max_length=128, blank=False)
    last_name = models.CharField(max_length=128, blank=False)
    date_of_birth = models.DateField(blank=False, default='2000-01-01')
    bio = models.TextField()
    email = models.EmailField(blank=False)
    jabber = models.EmailField(blank=False)
    skype = models.CharField(max_length=256, default='skypelogin')
    other = models.TextField()
