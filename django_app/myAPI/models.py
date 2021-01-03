from django.db import models

class choice(models.Model):
    CHOICES=(('1','pixels1'),('2','pixels2'))

#choices=models.CharFields(default=0)
