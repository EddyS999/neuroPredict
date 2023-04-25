# Generated by Django 4.1.3 on 2023-04-25 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('sexe', models.IntegerField(max_length=1)),
                ('age', models.IntegerField(max_length=3)),
                ('poids', models.FloatField(max_length=3)),
                ('taille', models.FloatField(max_length=3)),
                ('salivation', models.IntegerField(max_length=1)),
                ('cutting', models.IntegerField(max_length=1)),
                ('turning_in_bed', models.IntegerField(max_length=1)),
                ('alsfrs', models.IntegerField(max_length=2)),
                ('symptom_duration', models.FloatField(max_length=4)),
                ('pulse', models.FloatField(max_length=4)),
                ('systolic_blood_pressure', models.FloatField(max_length=4)),
                ('prediction', models.IntegerField()),
                ('vivant', models.FloatField(max_length=100)),
                ('mort', models.FloatField(max_length=100)),
            ],
        ),
    ]