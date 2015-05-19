# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.auth.models
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, max_length=30, validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username. This value may contain only letters, numbers and @/./+/-/_ characters.', 'invalid')], help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('address', models.TextField(null=True, verbose_name=b'Adres', blank=True)),
                ('phone', models.CharField(max_length=20, null=True, verbose_name=b'Telefon numaras\xc4\xb1', blank=True)),
                ('company', models.CharField(help_text=b'Kamu \xc3\xa7al\xc4\xb1\xc5\x9fanlar\xc4\xb1 ba\xc4\x9fl\xc4\xb1 olduklar\xc4\xb1 m\xc3\xbcd\xc3\xbcrl\xc3\xbc\xc4\x9f\xc3\xbc yazabilir.', max_length=255, null=True, verbose_name=b'\xc3\x87al\xc4\xb1\xc5\x9ft\xc4\xb1\xc4\x9f\xc4\xb1 \xc5\x9firket', blank=True)),
                ('public_officer', models.NullBooleanField(default=False, verbose_name=b'Kamu \xc3\xa7al\xc4\xb1\xc5\x9fan\xc4\xb1')),
                ('role', models.CharField(max_length=255, null=True, verbose_name=b'Ba\xc4\x9fl\xc4\xb1 olunan departman/b\xc3\xb6l\xc3\xbcm', blank=True)),
                ('birthdate', models.DateField(null=True, verbose_name=b'Do\xc4\x9fum tarihi', blank=True)),
                ('lkd_id', models.CharField(max_length=32, null=True, verbose_name=b'LKD \xc3\xbcye numaras\xc4\xb1', blank=True)),
                ('inetd_id', models.CharField(max_length=32, null=True, verbose_name=b'INETD \xc3\xbcye numaras\xc4\xb1', blank=True)),
                ('github_username', models.CharField(max_length=64, null=True, verbose_name=b'Github kullan\xc4\xb1c\xc4\xb1 ad\xc4\xb1', blank=True)),
                ('groups', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Kullan\u0131c\u0131 profili',
                'verbose_name_plural': 'Kullan\u0131c\u0131 profilleri',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AdministrativeNote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('note', models.TextField(verbose_name=b'Not')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('adder', models.ForeignKey(related_name='adder', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(related_name='notted_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'administrative_notes',
                'verbose_name': 'Y\xf6netimsel not',
                'verbose_name_plural': 'Y\xf6netimsel notlar',
            },
        ),
    ]
