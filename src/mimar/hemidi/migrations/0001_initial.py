# Generated by Django 3.0.4 on 2020-03-25 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='info_tp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_prof', models.CharField(max_length=100)),
                ('imail_prof', models.CharField(max_length=100)),
                ('nome_modul', models.CharField(max_length=100)),
                ('type_shm', models.CharField(choices=[('green', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], default='green', max_length=6)),
                ('title_tp', models.CharField(max_length=100)),
                ('description_tp', models.CharField(max_length=500)),
                ('fiche_tp', models.FileField(upload_to='uploads/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
