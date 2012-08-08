# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Event.start_time'
        db.alter_column('events_event', 'start_time', self.gf('django.db.models.fields.DateTimeField')(null=True))

        # Changing field 'Event.end_time'
        db.alter_column('events_event', 'end_time', self.gf('django.db.models.fields.DateTimeField')(null=True))


    def backwards(self, orm):
        
        # Changing field 'Event.start_time'
        db.alter_column('events_event', 'start_time', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Event.end_time'
        db.alter_column('events_event', 'end_time', self.gf('django.db.models.fields.DateField')(null=True))


    models = {
        'events.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'end_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.School']"}),
            'start_time': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'})
        },
        'schools.school': {
            'Meta': {'object_name': 'School'},
            'address': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'lon': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.SchoolType']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'})
        },
        'schools.schooltype': {
            'Meta': {'object_name': 'SchoolType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['events']
