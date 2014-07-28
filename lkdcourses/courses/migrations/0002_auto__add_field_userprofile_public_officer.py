# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'UserProfile.public_officer'
        db.add_column('user_profiles', 'public_officer',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'UserProfile.public_officer'
        db.delete_column('user_profiles', 'public_officer')


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
            'public_officer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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