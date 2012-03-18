# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Seo.title_uk'
        db.add_column('seo_seo', 'title_uk', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Seo.title_en'
        db.add_column('seo_seo', 'title_en', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'Seo.description_uk'
        db.add_column('seo_seo', 'description_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Seo.description_en'
        db.add_column('seo_seo', 'description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Seo.keywords_uk'
        db.add_column('seo_seo', 'keywords_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'Seo.keywords_en'
        db.add_column('seo_seo', 'keywords_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Seo.title_uk'
        db.delete_column('seo_seo', 'title_uk')

        # Deleting field 'Seo.title_en'
        db.delete_column('seo_seo', 'title_en')

        # Deleting field 'Seo.description_uk'
        db.delete_column('seo_seo', 'description_uk')

        # Deleting field 'Seo.description_en'
        db.delete_column('seo_seo', 'description_en')

        # Deleting field 'Seo.keywords_uk'
        db.delete_column('seo_seo', 'keywords_uk')

        # Deleting field 'Seo.keywords_en'
        db.delete_column('seo_seo', 'keywords_en')


    models = {
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'seo.seo': {
            'Meta': {'unique_together': "(('content_type', 'object_id'),)", 'object_name': 'Seo'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'description_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'keywords_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'keywords_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'seo.url': {
            'Meta': {'object_name': 'Url'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'})
        }
    }

    complete_apps = ['seo']
