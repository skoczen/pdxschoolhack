# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Person'
        db.create_table('my_schools_person', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('facebook_id', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
        ))
        db.send_create_signal('my_schools', ['Person'])

        # Adding model 'PersonSchool'
        db.create_table('my_schools_personschool', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('school', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.School'])),
        ))
        db.send_create_signal('my_schools', ['PersonSchool'])


    def backwards(self, orm):
        
        # Deleting model 'Person'
        db.delete_table('my_schools_person')

        # Deleting model 'PersonSchool'
        db.delete_table('my_schools_personschool')


    models = {
        'my_schools.person': {
            'Meta': {'object_name': 'Person'},
            'facebook_id': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'my_schools.personschool': {
            'Meta': {'object_name': 'PersonSchool'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'school': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.School']"})
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

    complete_apps = ['my_schools']
