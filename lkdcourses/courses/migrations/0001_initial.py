# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Instructor'
        db.create_table('instructors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fullname', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('avatar', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'courses', ['Instructor'])

        # Adding model 'Sponsor'
        db.create_table('sponsors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'courses', ['Sponsor'])

        # Adding model 'Venue'
        db.create_table('venues', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('directions', self.gf('django.db.models.fields.TextField')()),
            ('accommodation', self.gf('django.db.models.fields.TextField')()),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=3)),
        ))
        db.send_create_signal(u'courses', ['Venue'])

        # Adding model 'Event'
        db.create_table('events', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('cover_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('allowed_course_count', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('faq', self.gf('django.db.models.fields.TextField')()),
            ('venue', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Venue'])),
        ))
        db.send_create_signal(u'courses', ['Event'])

        # Adding model 'EventSponsor'
        db.create_table('event_sponsors', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Event'])),
            ('sponsor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Sponsor'])),
            ('type', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'courses', ['EventSponsor'])

        # Adding model 'Course'
        db.create_table('courses', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Event'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('participation_rules', self.gf('django.db.models.fields.TextField')()),
            ('covered_topics', self.gf('django.db.models.fields.TextField')()),
            ('deadline_date', self.gf('django.db.models.fields.DateField')()),
            ('quota', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'courses', ['Course'])

        # Adding M2M table for field instructors on 'Course'
        m2m_table_name = db.shorten_name('courses_instructors')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('course', models.ForeignKey(orm[u'courses.course'], null=False)),
            ('instructor', models.ForeignKey(orm[u'courses.instructor'], null=False))
        ))
        db.create_unique(m2m_table_name, ['course_id', 'instructor_id'])

        # Adding model 'UserChoice'
        db.create_table('user_choices', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Event'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Course'])),
            ('priority', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'courses', ['UserChoice'])

        # Adding model 'Application'
        db.create_table('applications', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='application_user', to=orm['auth.User'])),
            ('course', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['courses.Event'])),
            ('application_date', self.gf('django.db.models.fields.DateTimeField')()),
            ('approved', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('approved_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('approve_date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('permit_file', self.gf('django.db.models.fields.files.FileField')(max_length=100, null=True, blank=True)),
            ('need_accommodation', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('notes', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'courses', ['Application'])

        # Adding M2M table for field choices on 'Application'
        m2m_table_name = db.shorten_name('applications_choices')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('application', models.ForeignKey(orm[u'courses.application'], null=False)),
            ('userchoice', models.ForeignKey(orm[u'courses.userchoice'], null=False))
        ))
        db.create_unique(m2m_table_name, ['application_id', 'userchoice_id'])

        # Adding model 'AdministrativeNote'
        db.create_table('administrative_notes', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='notted_user', to=orm['auth.User'])),
            ('adder', self.gf('django.db.models.fields.related.ForeignKey')(related_name='adder', to=orm['auth.User'])),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'courses', ['AdministrativeNote'])

        # Adding model 'UserProfile'
        db.create_table('user_profiles', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('address', self.gf('django.db.models.fields.TextField')()),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('company', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('role', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('birthdate', self.gf('django.db.models.fields.DateField')()),
            ('lkd_id', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('inetd_id', self.gf('django.db.models.fields.CharField')(max_length=32, null=True, blank=True)),
            ('github_username', self.gf('django.db.models.fields.CharField')(max_length=64)),
        ))
        db.send_create_signal(u'courses', ['UserProfile'])


    def backwards(self, orm):
        # Deleting model 'Instructor'
        db.delete_table('instructors')

        # Deleting model 'Sponsor'
        db.delete_table('sponsors')

        # Deleting model 'Venue'
        db.delete_table('venues')

        # Deleting model 'Event'
        db.delete_table('events')

        # Deleting model 'EventSponsor'
        db.delete_table('event_sponsors')

        # Deleting model 'Course'
        db.delete_table('courses')

        # Removing M2M table for field instructors on 'Course'
        db.delete_table(db.shorten_name('courses_instructors'))

        # Deleting model 'UserChoice'
        db.delete_table('user_choices')

        # Deleting model 'Application'
        db.delete_table('applications')

        # Removing M2M table for field choices on 'Application'
        db.delete_table(db.shorten_name('applications_choices'))

        # Deleting model 'AdministrativeNote'
        db.delete_table('administrative_notes')

        # Deleting model 'UserProfile'
        db.delete_table('user_profiles')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'courses.administrativenote': {
            'Meta': {'object_name': 'AdministrativeNote', 'db_table': "'administrative_notes'"},
            'adder': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'adder'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'notted_user'", 'to': u"orm['auth.User']"})
        },
        u'courses.application': {
            'Meta': {'object_name': 'Application', 'db_table': "'applications'"},
            'application_date': ('django.db.models.fields.DateTimeField', [], {}),
            'approve_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'approved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'approved_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'choices': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.UserChoice']", 'symmetrical': 'False'}),
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'need_accommodation': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'notes': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'permit_file': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'application_user'", 'to': u"orm['auth.User']"})
        },
        u'courses.course': {
            'Meta': {'object_name': 'Course', 'db_table': "'courses'"},
            'covered_topics': ('django.db.models.fields.TextField', [], {}),
            'deadline_date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instructors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['courses.Instructor']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'participation_rules': ('django.db.models.fields.TextField', [], {}),
            'quota': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'courses.event': {
            'Meta': {'object_name': 'Event', 'db_table': "'events'"},
            'allowed_course_count': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'faq': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'venue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Venue']"})
        },
        u'courses.eventsponsor': {
            'Meta': {'object_name': 'EventSponsor', 'db_table': "'event_sponsors'"},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sponsor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Sponsor']"}),
            'type': ('django.db.models.fields.IntegerField', [], {})
        },
        u'courses.instructor': {
            'Meta': {'object_name': 'Instructor', 'db_table': "'instructors'"},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'fullname': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'courses.sponsor': {
            'Meta': {'object_name': 'Sponsor', 'db_table': "'sponsors'"},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'courses.userchoice': {
            'Meta': {'object_name': 'UserChoice', 'db_table': "'user_choices'"},
            'course': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Course']"}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['courses.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'priority': ('django.db.models.fields.IntegerField', [], {}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'courses.userprofile': {
            'Meta': {'object_name': 'UserProfile', 'db_table': "'user_profiles'"},
            'address': ('django.db.models.fields.TextField', [], {}),
            'birthdate': ('django.db.models.fields.DateField', [], {}),
            'company': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'github_username': ('django.db.models.fields.CharField', [], {'max_length': '64'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'inetd_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'lkd_id': ('django.db.models.fields.CharField', [], {'max_length': '32', 'null': 'True', 'blank': 'True'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'role': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']"})
        },
        u'courses.venue': {
            'Meta': {'object_name': 'Venue', 'db_table': "'venues'"},
            'accommodation': ('django.db.models.fields.TextField', [], {}),
            'address': ('django.db.models.fields.TextField', [], {}),
            'directions': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '3'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['courses']