# Generated by Django 2.1.7 on 2019-02-18 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('socios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=500)),
                ('fecha_inic', models.DateField()),
                ('limite_ayu', models.IntegerField()),
                ('link', models.URLField(max_length=500, null=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('ayudantes', models.ManyToManyField(related_name='eventos', to='socios.Socio')),
            ],
        ),
    ]
