# Generated by Django 4.2.7 on 2023-12-15 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0006_alter_opportunity_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='status',
            name='description',
            field=models.CharField(blank=True, max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='status',
            name='text_color',
            field=models.CharField(blank=True, default='#000000', help_text='Enter a hex color code for the text', max_length=7),
        ),
        migrations.AlterField(
            model_name='status',
            name='title_color',
            field=models.CharField(blank=True, default='#fff', help_text='Enter a hex color code for the title', max_length=7),
        ),
    ]