# Generated by Django 2.1rc1 on 2019-01-03 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ontology', '0002_remove_document_owl'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='ai',
        ),
        migrations.RemoveField(
            model_name='document',
            name='los',
        ),
    ]