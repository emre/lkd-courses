# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Etkinlik ad\xc4\xb1')),
                ('slug', models.SlugField()),
                ('cover_image', models.ImageField(upload_to=b'event_cover_images')),
                ('start_date', models.DateField(verbose_name=b'Ba\xc5\x9flang\xc4\xb1\xc3\xa7 tarihi')),
                ('end_date', models.DateField(verbose_name=b'Biti\xc5\x9f tarihi')),
                ('allowed_course_count', models.IntegerField(default=2, help_text=b'Biri asil, di\xc4\x9ferleri yedek olmak \xc3\xbczere toplam.', verbose_name=b'Tek bir ki\xc5\x9finin ba\xc5\x9fvuru yapabilece\xc4\x9fi kurs say\xc4\xb1s\xc4\xb1')),
                ('faq', models.TextField(verbose_name=b'S\xc4\xb1k\xc3\xa7a sorulan sorular')),
            ],
            options={
                'db_table': 'events',
                'verbose_name': 'Etkinlik',
                'verbose_name_plural': 'Etkinlikler',
            },
        ),
        migrations.CreateModel(
            name='EventSponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.IntegerField(choices=[(1, b'platin'), (2, b'alt\xc4\xb1n'), (3, b'g\xc3\xbcm\xc3\xbc\xc5\x9f'), (4, b'bronz')])),
                ('event', models.ForeignKey(to='events.Event')),
            ],
            options={
                'db_table': 'event_sponsors',
                'verbose_name': 'Etkinlik sponsoru',
                'verbose_name_plural': 'Etkinlik sponsorlar\u0131',
            },
        ),
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Sponsor ismi')),
                ('url', models.CharField(max_length=255, verbose_name=b'Sponsor adres')),
            ],
            options={
                'db_table': 'sponsors',
                'verbose_name': 'Sponsor',
                'verbose_name_plural': 'Sponsorlar',
            },
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Etkinli\xc4\x9fin yap\xc4\xb1laca\xc4\x9f\xc4\xb1 alan\xc4\xb1n ad\xc4\xb1')),
                ('address', models.TextField(verbose_name=b'Alan\xc4\xb1n adresi')),
                ('directions', models.TextField(verbose_name=b'Alana ula\xc5\x9f\xc4\xb1m i\xc3\xa7in y\xc3\xb6nlendirmeler')),
                ('accommodation', models.TextField(verbose_name=b'Konaklama ile ilgili bilgiler.')),
                ('latitude', models.DecimalField(help_text=b'Harita g\xc3\xb6sterimi i\xc3\xa7in gerekli.', max_digits=6, decimal_places=3)),
                ('longitude', models.DecimalField(help_text=b'Harita g\xc3\xb6sterimi i\xc3\xa7in gerekli.', max_digits=6, decimal_places=3)),
            ],
            options={
                'db_table': 'venues',
                'verbose_name': 'Etkinlik alan\u0131',
                'verbose_name_plural': 'Etkinlik alanlar\u0131',
            },
        ),
        migrations.AddField(
            model_name='eventsponsor',
            name='sponsor',
            field=models.ForeignKey(to='events.Sponsor'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(to='events.Venue'),
        ),
    ]
