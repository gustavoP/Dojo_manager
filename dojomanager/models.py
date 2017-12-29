from django.db import models
from django.utils import timezone


class Studant(models.Model):
    name = models.TextField()
    slug_name = models.CharField(max_length=100)
    birth_date = models.DateTimeField(default=timezone.now)
    join_date = models.DateTimeField(default=timezone.now)
    contact_main_phone = models.TextField(max_length=100)
    contact_alternative = models.TextField(max_length=100)
    #classes=models.varias foreignkey([list os classes])
    #    author = models.ForeignKey('auth.User')

    def change_phone(self,phone_contact):
        self.contact_alternatove = phone_contact
        self.save()

    def __str__(self):
        return self.name
