# Generated by Django 2.1.7 on 2020-05-19 01:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Concepto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calle', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=50)),
                ('colonia', models.CharField(max_length=50)),
                ('municipio', models.CharField(max_length=50)),
                ('estado', models.CharField(max_length=50)),
                ('codigo_postal', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Partida',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('propietario', models.CharField(max_length=50)),
                ('direccion', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='HogaresYObrasMexicanas.Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='Unidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('costo', models.FloatField()),
                ('concepto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HogaresYObrasMexicanas.Concepto')),
            ],
        ),
        migrations.AddField(
            model_name='partida',
            name='proyecto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HogaresYObrasMexicanas.Proyecto'),
        ),
        migrations.AddField(
            model_name='concepto',
            name='partida',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='HogaresYObrasMexicanas.Partida'),
        ),
    ]
