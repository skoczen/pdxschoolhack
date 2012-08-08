# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'School.address'
        db.add_column('schools_school', 'address', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'School.city'
        db.add_column('schools_school', 'city', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'School.zip_code'
        db.add_column('schools_school', 'zip_code', self.gf('django.db.models.fields.CharField')(max_length=5, null=True, blank=True), keep_default=False)

        # Changing field 'School.lon'
        db.alter_column('schools_school', 'lon', self.gf('django.db.models.fields.FloatField')(null=True))

        # Changing field 'School.lat'
        db.alter_column('schools_school', 'lat', self.gf('django.db.models.fields.FloatField')(null=True))


    def backwards(self, orm):
        
        # Deleting field 'School.address'
        db.delete_column('schools_school', 'address')

        # Deleting field 'School.city'
        db.delete_column('schools_school', 'city')

        # Deleting field 'School.zip_code'
        db.delete_column('schools_school', 'zip_code')

        # User chose to not deal with backwards NULL issues for 'School.lon'
        raise RuntimeError("Cannot reverse this migration. 'School.lon' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'School.lat'
        raise RuntimeError("Cannot reverse this migration. 'School.lat' and its values cannot be restored.")


    models = {
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

    complete_apps = ['schools']
