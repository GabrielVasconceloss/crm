from django.db import models


class Camp(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, verbose_name="Description")

    def __str__(self):
        return "{} ({})".format(self.title, self.description)