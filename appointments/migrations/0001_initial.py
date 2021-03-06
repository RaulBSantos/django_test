# Generated by Django 2.2.4 on 2019-08-22 22:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('honorific', models.SmallIntegerField(choices=[(1, 'Mr'), (2, 'Mme')], default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('hour', models.TimeField()),
                ('duration', models.DurationField(default=15)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appointments.Patient')),
            ],
        ),
    ]
