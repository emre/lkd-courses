# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AdministrativeNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(verbose_name=b'Not')),
                ('adder', models.ForeignKey(related_name='adder', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='notted_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'administrative_notes',
                'verbose_name': 'Y\xf6netimsel not',
                'verbose_name_plural': 'Y\xf6netimsel notlar',
            },
        ),
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
            ],
            options={
                'db_table': 'courses',
                'verbose_name': 'Kurs',
                'verbose_name_plural': 'Kurslar',
            },
        ),
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
                ('type', models.IntegerField(choices=[(b'1', b'platin'), (b'2', b'alt\xc4\xb1n'), (b'4', b'g\xc3\xbcm\xc3\xbc\xc5\x9f'), (b'5', b'bronz')])),
                ('event', models.ForeignKey(to='courses.Event')),
            ],
            options={
                'db_table': 'event_sponsors',
                'verbose_name': 'Etkinlik sponsoru',
                'verbose_name_plural': 'Etkinlik sponsorlar\u0131',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fullname', models.CharField(max_length=255, verbose_name=b'ad soyad')),
                ('avatar', models.ImageField(null=True, upload_to=b'instructor_avatars', blank=True)),
            ],
            options={
                'db_table': 'instructors',
                'verbose_name': 'E\u011fitmen',
                'verbose_name_plural': 'E\u011fitmenler',
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
            name='UserChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('priority', models.IntegerField(verbose_name=b'\xc3\x96ncelik')),
                ('course', models.ForeignKey(to='courses.Course')),
                ('event', models.ForeignKey(to='courses.Event')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_choices',
                'verbose_name': 'kullan\u0131c\u0131 kurs se\xe7imi',
                'verbose_name_plural': 'kullan\u0131c\u0131 kurs se\xe7imleri',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.TextField(null=True, verbose_name=b'Adres', blank=True)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name=b'Telefon numaras\xc4\xb1', blank=True)),
                ('company', models.CharField(help_text=b'Kamu \xc3\xa7al\xc4\xb1\xc5\x9fanlar\xc4\xb1 ba\xc4\x9fl\xc4\xb1 olduklar\xc4\xb1 m\xc3\xbcd\xc3\xbcrl\xc3\xbc\xc4\x9f\xc3\xbc yazabilir.', max_length=255, null=True, verbose_name=b'\xc3\x87al\xc4\xb1\xc5\x9ft\xc4\xb1\xc4\x9f\xc4\xb1 \xc5\x9firket', blank=True)),
                ('public_officer', models.NullBooleanField(default=False, verbose_name=b'Kamu \xc3\xa7al\xc4\xb1\xc5\x9fan\xc4\xb1')),
                ('role', models.CharField(max_length=255, null=True, verbose_name=b'Ba\xc4\x9fl\xc4\xb1 olunan departman/b\xc3\xb6l\xc3\xbcm', blank=True)),
                ('birthdate', models.DateField(null=True, verbose_name=b'Do\xc4\x9fum tarihi', blank=True)),
                ('lkd_id', models.CharField(max_length=32, null=True, verbose_name=b'LKD \xc3\xbcye numaras\xc4\xb1', blank=True)),
                ('inetd_id', models.CharField(max_length=32, null=True, verbose_name=b'INETD \xc3\xbcye numaras\xc4\xb1', blank=True)),
                ('github_username', models.CharField(max_length=64, null=True, verbose_name=b'Github kullan\xc4\xb1c\xc4\xb1 ad\xc4\xb1', blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profiles',
                'verbose_name': 'Kullan\u0131c\u0131 profili',
                'verbose_name_plural': 'Kullan\u0131c\u0131 profilleri',
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
            field=models.ForeignKey(to='courses.Sponsor'),
        ),
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.ForeignKey(to='courses.Venue'),
        ),
        migrations.AddField(
            model_name='course',
            name='event',
            field=models.ForeignKey(to='courses.Event'),
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
            field=models.ForeignKey(to='courses.Event'),
        ),
        migrations.AddField(
            model_name='application',
            name='user',
            field=models.ForeignKey(related_name='application_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
