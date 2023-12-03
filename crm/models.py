from django.db import models


class Camp(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, verbose_name="Description")

    def __str__(self):
        return "{} ({})".format(self.title, self.description)

class status(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, verbose_name="Description")
    title_color = models.CharField(max_length=7, default='#fff', help_text='Enter a hex color code for the title')
    text_color = models.CharField(max_length=7, default='#000000', help_text='Enter a hex color code for the text')

    def __str__(self):
        return "{} ({})".format(self.title, self.description)