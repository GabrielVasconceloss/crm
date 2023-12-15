from django.db import models


class Camp(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, verbose_name="Description")

    def __str__(self):
        return "{} ({})".format(self.title, self.description)


class Status(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500, verbose_name="Description", blank=True)
    title_color = models.CharField(max_length=7, default='#000000', help_text='Enter a hex color code for the title', blank=True)
    text_color = models.CharField(max_length=7, default='#000000', help_text='Enter a hex color code for the text', blank=True)

    def __str__(self):
        return "{}".format(self.title)


class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return "{} ({})".format(self.first_name, self.last_name)


class Contact(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)

    def __str__(self):
        return "{}".format(self.contact_name)


class Opportunity(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    opportunity_name = models.CharField(max_length=255)
    opportunity_description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return "{} ({})".format(self.opportunity_name, self.opportunity_description)


class Activity(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    activity_date = models.DateField()
    notes = models.TextField()

    def __str__(self):
        return "{}".format(self.activity_type)


class ContactOpportunityRelationship(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    opportunity = models.ForeignKey(Opportunity, on_delete=models.CASCADE)
    role = models.CharField(max_length=50)