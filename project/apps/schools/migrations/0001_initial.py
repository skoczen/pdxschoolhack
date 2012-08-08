# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SchoolType'
        # db.create_table('schools_schooltype', (
        #     ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        # ))
        # db.send_create_signal('schools', ['SchoolType'])

        # # Adding model 'School'
        # db.create_table('schools_school', (
        #     ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        #     ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        #     ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
        #     ('lat', self.gf('django.db.models.fields.IntegerField')()),
        #     ('lon', self.gf('django.db.models.fields.IntegerField')()),
        #     ('school_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['schools.SchoolType'])),
        # ))
        # db.send_create_signal('schools', ['School'])
        pass

    def backwards(self, orm):
        
        pass
        # # Deleting model 'SchoolType'
        # db.delete_table('schools_schooltype')

        # # Deleting model 'School'
        # db.delete_table('schools_school')


    models = {
        'schools.school': {
            'Meta': {'object_name': 'School'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lat': ('django.db.models.fields.IntegerField', [], {}),
            'lon': ('django.db.models.fields.IntegerField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'school_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['schools.SchoolType']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'schools.schooltype': {
            'Meta': {'object_name': 'SchoolType'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['schools']
