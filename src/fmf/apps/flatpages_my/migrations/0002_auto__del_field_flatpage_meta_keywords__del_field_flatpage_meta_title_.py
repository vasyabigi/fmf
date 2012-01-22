# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Deleting field 'FlatPage.meta_keywords'
        db.delete_column('django_flatpage', 'meta_keywords')

        # Deleting field 'FlatPage.meta_title_uk'
        db.delete_column('django_flatpage', 'meta_title_uk')

        # Deleting field 'FlatPage.meta_keywords_en'
        db.delete_column('django_flatpage', 'meta_keywords_en')

        # Deleting field 'FlatPage.meta_keywords_uk'
        db.delete_column('django_flatpage', 'meta_keywords_uk')

        # Deleting field 'FlatPage.meta_description'
        db.delete_column('django_flatpage', 'meta_description')

        # Deleting field 'FlatPage.meta_description_en'
        db.delete_column('django_flatpage', 'meta_description_en')

        # Deleting field 'FlatPage.meta_title'
        db.delete_column('django_flatpage', 'meta_title')

        # Deleting field 'FlatPage.meta_description_uk'
        db.delete_column('django_flatpage', 'meta_description_uk')

        # Deleting field 'FlatPage.meta_title_en'
        db.delete_column('django_flatpage', 'meta_title_en')


    def backwards(self, orm):
        
        # Adding field 'FlatPage.meta_keywords'
        db.add_column('django_flatpage', 'meta_keywords', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'FlatPage.meta_title_uk'
        db.add_column('django_flatpage', 'meta_title_uk', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'FlatPage.meta_keywords_en'
        db.add_column('django_flatpage', 'meta_keywords_en', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'FlatPage.meta_keywords_uk'
        db.add_column('django_flatpage', 'meta_keywords_uk', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'FlatPage.meta_description'
        db.add_column('django_flatpage', 'meta_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FlatPage.meta_description_en'
        db.add_column('django_flatpage', 'meta_description_en', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FlatPage.meta_title'
        db.add_column('django_flatpage', 'meta_title', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)

        # Adding field 'FlatPage.meta_description_uk'
        db.add_column('django_flatpage', 'meta_description_uk', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FlatPage.meta_title_en'
        db.add_column('django_flatpage', 'meta_title_en', self.gf('django.db.models.fields.CharField')(max_length=128, null=True, blank=True), keep_default=False)


    models = {
        'flatpages_my.flatpage': {
            'Meta': {'ordering': "('title',)", 'object_name': 'FlatPage', 'db_table': "'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'content_en': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'content_uk': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'flatpages_my.flatpageimage': {
            'Meta': {'ordering': "('position',)", 'object_name': 'FlatPageImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'images'", 'to': "orm['flatpages_my.FlatPage']"}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '-1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_en': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'}),
            'title_uk': ('django.db.models.fields.CharField', [], {'max_length': '256', 'null': 'True', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flatpages_my']
