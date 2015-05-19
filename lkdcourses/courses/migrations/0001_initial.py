# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('application_date', models.DateTimeField(verbose_name=b'Ba\xc5\x9fvuru tarihi')),
                ('approved', models.BooleanField(default=False, verbose_name=b'Onay durumu')),
                ('approve_date', models.DateTimeField(null=True, verbose_name=b'Onaylanma tarihi', blank=True)),
                ('permit_file', models.FileField(null=True, upload_to=b'permit_files', blank=True)),
                ('need_accommodation', models.BooleanField(default=0, verbose_name=b'Konaklama ihtiyac\xc4\xb1')),
                ('notes', models.TextField(null=True, verbose_name=b'Notlar', blank=True)),
                ('approved_by', models.ForeignKey(verbose_name=b'Onaylayan', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'applications',
                'verbose_name': 'Ba\u015fvuru',
                'verbose_name_plural': 'Ba\u015fvurular',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Kurs ismi')),
                ('description', models.TextField(null=True, verbose_name=b'Kurs a\xc3\xa7\xc4\xb1klamas\xc4\xb1', blank=True)),
                ('slug', models.SlugField()),
                ('start_date', models.DateField(verbose_name=b'Ba\xc5\x9flang\xc4\xb1\xc3\xa7 tarihi')),
                ('end_date', models.DateField(verbose_name=b'Biti\xc5\x9f tarihi')),
                ('participation_rules', models.TextField(help_text=b'Bir bo\xc5\x9fluk b\xc4\xb1rakarak maddeler halinde yaz\xc4\xb1n\xc4\xb1z.', verbose_name=b'Kat\xc4\xb1l\xc4\xb1m ko\xc5\x9fullar\xc4\xb1')),
                ('covered_topics', models.TextField(help_text=b'Bir bo\xc5\x9fluk b\xc4\xb1rakarak maddeler halinde yaz\xc4\xb1n\xc4\xb1z.', verbose_name=b'Konular')),
                ('deadline_date', models.DateField(verbose_name=b'Son ba\xc5\x9fvuru ekleme/d\xc3\xbczenleme tarihi')),
                ('quota', models.IntegerField(null=True, verbose_name=b'Kat\xc4\xb1l\xc4\xb1mc\xc4\xb1 kotas\xc4\xb1', blank=True)),
                ('event', models.ForeignKey(to='events.Event')),
            ],
            options={
                'db_table': 'courses',
                'verbose_name': 'Kurs',
                'verbose_name_plural': 'Kurslar',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=255, verbose_name=b'ad soyad')),
                ('avatar', models.ImageField(null=True, upload_to=b'instructor_avatars', blank=True)),
                ('about_text', models.TextField(null=True, verbose_name=b'E\xc4\x9fitmen hakk\xc4\xb1nda', blank=True)),
            ],
            options={
                'db_table': 'instructors',
                'verbose_name': 'E\u011fitmen',
                'verbose_name_plural': 'E\u011fitmenler',
            },
        ),
        migrations.CreateModel(
            name='UserChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField(verbose_name=b'\xc3\x96ncelik')),
                ('course', models.ForeignKey(to='courses.Course')),
                ('event', models.ForeignKey(to='events.Event')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_choices',
                'verbose_name': 'kullan\u0131c\u0131 kurs se\xe7imi',
                'verbose_name_plural': 'kullan\u0131c\u0131 kurs se\xe7imleri',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='instructors',
            field=models.ManyToManyField(to='courses.Instructor'),
        ),
        migrations.AddField(
            model_name='application',
            name='choices',
            field=models.ManyToManyField(to='courses.UserChoice'),
        ),
        migrations.AddField(
            model_name='application',
            name='event',
            field=models.ForeignKey(to='events.Event'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(related_name='application_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
