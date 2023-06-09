# Generated by Django 4.1.3 on 2023-05-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='breathing',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='patient',
            name='climbing',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='patient',
            name='dressing',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='patient',
            name='handwriting',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='patient',
            name='speech',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='patient',
            name='swallowing',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AddField(
            model_name='patient',
            name='walking',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='alsfrs',
            field=models.IntegerField(max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cutting',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='salivation',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='patient',
            name='turning_in_bed',
            field=models.IntegerField(default=0, max_length=1),
        ),
    ]
